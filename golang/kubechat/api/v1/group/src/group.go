package main

import (
	"encoding/json"
	"fmt"
	"github.com/asaskevich/govalidator"
	"github.com/gocql/gocql"
	"github.com/julienschmidt/httprouter"
	"github.com/satori/go.uuid"
	"log"
	"net/http"
	"regexp"
	"shared"
	"time"
)

var groupType = []string{"democratic", "totalitarian", "semi-democratic", "semi-totalitarian"}
var groupVisibility = []string{"public", "closed", "invite"}
func InitValidators() {
	govalidator.TagMap["groupType"] = func(group string) bool {
		for _, value := range groupType {
			if value == group {
				return true
			}
		}
		return false
	}

	govalidator.TagMap["groupVisibility"] = func(group string) bool {
		for _, value := range groupVisibility {
			if value == group {
				return true
			}
		}
		return false
	}

	govalidator.TagMap["checkUUID"] = func(thread string) bool {
		if govalidator.IsUUIDv4(thread) {
			return true
		}
		return false
	}

	govalidator.TagMap["checkDay"] = func(day string) bool {
		re := regexp.MustCompile(`\d{4}-\d{2}-\d{2}`)
		if re.MatchString(day) {
			return true
		}
		return false
	}
}

var GroupsInsert = fmt.Sprintf("INSERT INTO groups (group_id,community_id,create_date,description,labels,name,plabels,type,update_date,visibility) VALUES (?,?,?,?,?,?,?,?,?,?)")
var GroupGetSingle = fmt.Sprintf("SELECT * FROM groups WHERE group_id = ? AND community_id = ? LIMIT 1")
var GroupUpdateSingle = fmt.Sprintf("UPDATE groups SET description = ?, labels = ?, name = ?, plabels = ?, type = ?, update_date = ?, visibility = ? WHERE group_id = ? AND community_id = ?")

var GroupsByCommunityInsert = fmt.Sprintf("INSERT INTO groups_by_community (community_id,name,create_date,description,group_id,labels,plabels,type,visibility) VALUES (?,?,?,?,?,?,?,?,?)")
var GroupsByCommunitySelect = fmt.Sprintf("SELECT community_id,name FROM groups_by_community WHERE community_id = ? AND name = ? LIMIT 1")
var GroupsByCommunityUpdate = fmt.Sprintf("UPDATE groups_by_community SET name = ?, description = ?, labels = ?, plabels = ?, type = ?, visibility = ? WHERE community_id = ? AND name = ?")

var GroupsByCommunityCreateDateInsert = fmt.Sprintf("INSERT INTO groups_by_community_create_date (community_id,day,create_date,description,group_id,labels,name,plabels,type,visibility) VALUES (?,?,?,?,?,?,?,?,?,?)")
var GroupsByCommunityCreateDateSelect = fmt.Sprintf("SELECT * FROM groups_by_community_create_date WHERE community_id = ? AND day = ?")

var GroupsByCommunityTypeInsert = fmt.Sprintf("INSERT INTO groups_by_community_type (community_id,type,create_date,day,description,group_id,labels,name,plabels,visibility) VALUES (?,?,?,?,?,?,?,?,?,?)")
var GroupsByCommunityTypeSelect = fmt.Sprintf("SELECT * FROM groups_by_community_type WHERE community_id = ? AND type = ?")

var GroupsByCommunityVisibilityInsert = fmt.Sprintf("INSERT INTO groups_by_community_visibility (community_id,visibility,create_date,day,description,group_id,labels,name,plabels,type) VALUES (?,?,?,?,?,?,?,?,?,?)")
var GroupsByCommunityVisibilitySelect = fmt.Sprintf("SELECT * FROM groups_by_community_visibility WHERE community_id = ? AND visibility = ?")

func GroupCreate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}

	group := shared.Group{}
	err := json.NewDecoder(r.Body).Decode(&group)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	id, err := uuid.NewV4()
	if err != nil {
		log.Printf("could not generate UUID for group: %s", err)
		return
	}

	currentTime := time.Now()
	year := currentTime.Year()
	month := currentTime.Month()
	day := currentTime.Day()

	group.GroupId = id.String()
	group.Day = fmt.Sprintf("%d-%d-%d", year, month, day)
	group.CreateDate =	currentTime
	group.UpdateDate = currentTime
	_, err = govalidator.ValidateStruct(group)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	var queryGroup shared.Group
	db := shared.DatabaseConnCassandra()
	log.Printf("Executing query: %s", GroupsByCommunitySelect)
	if err := db.Query(GroupsByCommunitySelect, group.CommunityId, group.Name).Consistency(gocql.One).Scan(&queryGroup.CommunityId, &queryGroup.Name); err != nil {
		switch err {
		case nil:
			// do nothing
		case gocql.ErrNotFound:
			log.Printf("group: '%s' not found in the community: %s, creating it...", group.Name, group.CommunityId)
		default:
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage(fmt.Sprintf("error occured: %s", err))
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}

	if queryGroup.Name != "" {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("group: '%s' already exists in community: %s", group.Name, group.CommunityId))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	go func() {
		log.Printf("Executing query: %s", GroupsInsert)
		if err := db.Query(GroupsInsert, group.GroupId, group.CommunityId, group.CreateDate, group.Description,
			group.Labels, group.Name, group.Plabels, group.Type, group.UpdateDate, group.Visibility).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()
	go func() {
		log.Printf("Executing query: %s", GroupsByCommunityInsert)
		if err := db.Query(GroupsByCommunityInsert, group.CommunityId, group.Name, group.CreateDate, group.Description,
			group.GroupId, group.Labels, group.Plabels, group.Type, group.Visibility).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()
	go func() {
		log.Printf("Executing query: %s", GroupsByCommunityCreateDateInsert)
		if err := db.Query(GroupsByCommunityCreateDateInsert, group.CommunityId, group.Day, group.CreateDate,
			group.Description, group.GroupId, group.Labels, group.Name, group.Plabels, group.Type, group.Visibility).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()
	go func() {
		log.Printf("Executing query: %s", GroupsByCommunityTypeInsert)
		if err := db.Query(GroupsByCommunityTypeInsert, group.CommunityId, group.Type, group.CreateDate, group.Day,
			group.Description, group.GroupId, group.Labels, group.Name, group.Plabels, group.Visibility).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()
	go func() {
		log.Printf("Executing query: %s", GroupsByCommunityVisibilityInsert)
		if err := db.Query(GroupsByCommunityVisibilityInsert, group.CommunityId, group.Visibility, group.CreateDate,
			group.Day, group.Description, group.GroupId, group.Labels, group.Name, group.Plabels, group.Type).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()

	groupJson, err := json.Marshal(group)
	log.Printf("group created: %s", string(groupJson))
	if err != nil {
		log.Printf("cannot Marshal json: %s", err)
		return
	}
	msg := shared.GenerateResponseMessage(fmt.Sprintf("group: '%s' created in community: %s", group.Name, group.CommunityId))
	w.WriteHeader(http.StatusOK)
	w.Write(msg)
}

func GroupUpdate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}

	groupUpdate := shared.GroupUpdate{}
	err := json.NewDecoder(r.Body).Decode(&groupUpdate)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}
	currentTime := time.Now()
	groupUpdate.UpdateDate = currentTime
	_, err = govalidator.ValidateStruct(groupUpdate)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	var queryGroup shared.Group
	db := shared.DatabaseConnCassandra()
	log.Printf("Executing query: %s", GroupGetSingle)
	if err := db.Query(GroupGetSingle, groupUpdate.GroupId, groupUpdate.CommunityId).Consistency(gocql.One).Scan(&queryGroup.GroupId,
		&queryGroup.CommunityId, &queryGroup.CreateDate, &queryGroup.Description, &queryGroup.Labels, &queryGroup.Name,
		&queryGroup.Plabels, &queryGroup.Type, &queryGroup.UpdateDate, &queryGroup.Visibility); err != nil {
		switch err {
		case nil:
			// do nothing
		case gocql.ErrNotFound:
			log.Printf("group: '%s' not found in the community: %s", queryGroup.GroupId, queryGroup.CommunityId)
			msg := shared.GenerateResponseMessage("group not found in community")
			w.WriteHeader(http.StatusBadRequest)
			w.Write(msg)
			return
		default:
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage(fmt.Sprintf("error occured: %s", err))
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}

	updatedGroup := queryGroup
	updatedGroup.Description = groupUpdate.Description
	updatedGroup.Labels = groupUpdate.Labels
	updatedGroup.Name = groupUpdate.Name
	updatedGroup.Type = groupUpdate.Type
	updatedGroup.UpdateDate = groupUpdate.UpdateDate
	updatedGroup.Visibility = groupUpdate.Visibility

	// DELETE THAN WRITE
	go func() {
		log.Printf("Executing query: %s", GroupUpdateSingle)
		if err := db.Query(GroupUpdateSingle, updatedGroup.Description, updatedGroup.Labels, updatedGroup.Name, updatedGroup.Plabels, updatedGroup.Type,
			updatedGroup.UpdateDate, updatedGroup.Visibility, updatedGroup.GroupId, updatedGroup.CommunityId).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()
	go func() {
		log.Printf("Executing query: %s", GroupsByCommunityUpdate)
		if err := db.Query(GroupsByCommunityUpdate, updatedGroup.Name, updatedGroup.Description, updatedGroup.Labels,
			updatedGroup.Plabels, updatedGroup.Type, updatedGroup.Visibility, queryGroup.CommunityId, queryGroup.Name).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()

	groupJson, err := json.Marshal(queryGroup)
	log.Printf("group update: %s", string(groupJson))
	if err != nil {
		log.Printf("cannot Marshal json: %s", err)
		return
	}
	msg := shared.GenerateResponseMessage(fmt.Sprintf("group: '%s' updated in community: %s", groupUpdate.GroupId, groupUpdate.CommunityId))
	w.WriteHeader(http.StatusOK)
	w.Write(msg)
}

func GroupDelete(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func GroupGet(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}

	queryValues := r.URL.Query()
	var queryGroupGet shared.GroupGet
	queryGroupGet.GroupId = ps.ByName("group_id")
	queryGroupGet.CommunityId = queryValues.Get("community_id")
	fmt.Print(queryGroupGet)

	_, err := govalidator.ValidateStruct(queryGroupGet)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	var queryGroup shared.Group
	db := shared.DatabaseConnCassandra()
	log.Printf("Executing query: %s", GroupGetSingle)
	if err := db.Query(GroupGetSingle, queryGroupGet.GroupId, queryGroupGet.CommunityId).Consistency(gocql.One).Scan(&queryGroup.GroupId,
		&queryGroup.CommunityId, &queryGroup.CreateDate, &queryGroup.Description, &queryGroup.Labels, &queryGroup.Name,
		&queryGroup.Plabels, &queryGroup.Type, &queryGroup.UpdateDate, &queryGroup.Visibility); err != nil {
		switch err {
		case nil:
			// do nothing
		case gocql.ErrNotFound:
			log.Printf("group: '%s' not found in the community: %s", queryGroup.GroupId, queryGroup.CommunityId)
			msg := shared.GenerateResponseMessage("group not found in community")
			w.WriteHeader(http.StatusBadRequest)
			w.Write(msg)
			return
		default:
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage(fmt.Sprintf("error occured: %s", err))
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}

	groupJson, err := json.Marshal(queryGroup)
	log.Printf("group fetched: %s", string(groupJson))
	if err != nil {
		log.Printf("cannot Marshal json: %s", err)
		return
	}
	w.WriteHeader(http.StatusOK)
	w.Write(groupJson)
}

func GroupsByCommunityCreateDate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}

	queryValues := r.URL.Query()
	communityId := queryValues.Get("community_id")
	day := queryValues.Get("day")
	groupGetByCommunityCreateDate := shared.GroupGetByCommunityCreateDate{CommunityId: communityId, Day: day}
	_, err := govalidator.ValidateStruct(groupGetByCommunityCreateDate)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	var queryGroup shared.Group
	var queryGroupList []shared.Group
	db := shared.DatabaseConnCassandra()
	log.Printf("Executing query: %s", GroupsByCommunityCreateDateSelect)
	iter := db.Query(GroupsByCommunityCreateDateSelect, communityId, day).Iter()
	for iter.Scan(&queryGroup.CommunityId, &queryGroup.Day, &queryGroup.CreateDate, &queryGroup.Description,
		&queryGroup.GroupId, &queryGroup.Labels, &queryGroup.Name, &queryGroup.Labels, &queryGroup.Type, &queryGroup.Visibility) {
		queryGroupList = append(queryGroupList, queryGroup)
	}
	if err := iter.Close(); err != nil {
		log.Fatal(err)
	}
	if queryGroupList == nil {
		log.Printf("no groups found in the community: %s for day: %s", communityId, day)
		msg := shared.GenerateResponseMessage(fmt.Sprintf("no groups found in the community: %s for day: %s", communityId, day))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	groupsJson, err := json.Marshal(queryGroupList)
	log.Printf("groups fetched: %s", string(groupsJson))
	if err != nil {
		log.Printf("cannot Marshal json: %s", err)
		return
	}
	w.WriteHeader(http.StatusOK)
	w.Write(groupsJson)
}

func GroupsByCommunityType(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}

	queryValues := r.URL.Query()
	communityId := queryValues.Get("community_id")
	groupType := queryValues.Get("type")
	groupsByCommunityTypeSelect := shared.GroupsByCommunityTypeSelect{CommunityId: communityId, Type: groupType}
	_, err := govalidator.ValidateStruct(groupsByCommunityTypeSelect)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	var queryGroup shared.Group
	var queryGroupList []shared.Group
	db := shared.DatabaseConnCassandra()
	log.Printf("Executing query: %s", GroupsByCommunityTypeSelect)
	iter := db.Query(GroupsByCommunityTypeSelect, communityId, groupType).Iter()
	for iter.Scan(&queryGroup.CommunityId, &queryGroup.Type, &queryGroup.CreateDate, &queryGroup.Day, &queryGroup.Description,
		&queryGroup.GroupId, &queryGroup.Labels, &queryGroup.Name, &queryGroup.Plabels, &queryGroup.Visibility) {
		queryGroupList = append(queryGroupList, queryGroup)
	}
	if err := iter.Close(); err != nil {
		log.Fatal(err)
	}
	if queryGroupList == nil {
		log.Printf("no groups of type: %s found in the community: %s", groupType, communityId)
		msg := shared.GenerateResponseMessage(fmt.Sprintf("no groups of type: %s found in the community: %ss", groupType, communityId))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	groupsJson, err := json.Marshal(queryGroupList)
	log.Printf("groups fetched: %s", string(groupsJson))
	if err != nil {
		log.Printf("cannot Marshal json: %s", err)
		return
	}
	w.WriteHeader(http.StatusOK)
	w.Write(groupsJson)
}

func GroupsByCommunityVisibility(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}

	queryValues := r.URL.Query()
	communityId := queryValues.Get("community_id")
	groupVisibility := queryValues.Get("visibility")
	groupsByCommunityVisibilitySelect := shared.GroupsByCommunityVisibilitySelect{CommunityId: communityId, Visibility: groupVisibility}
	_, err := govalidator.ValidateStruct(groupsByCommunityVisibilitySelect)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	var queryGroup shared.Group
	var queryGroupList []shared.Group
	db := shared.DatabaseConnCassandra()
	log.Printf("Executing query: %s", GroupsByCommunityVisibilitySelect)
	iter := db.Query(GroupsByCommunityVisibilitySelect, communityId, groupVisibility).Iter()
	for iter.Scan(&queryGroup.CommunityId, &queryGroup.Visibility, &queryGroup.CreateDate, &queryGroup.Day, &queryGroup.Description,
		&queryGroup.GroupId, &queryGroup.Labels, &queryGroup.Name, &queryGroup.Plabels, &queryGroup.Type) {
		queryGroupList = append(queryGroupList, queryGroup)
	}
	if err := iter.Close(); err != nil {
		log.Fatal(err)
	}
	if queryGroupList == nil {
		log.Printf("no groups of visibility: %s found in the community: %s", groupVisibility, communityId)
		msg := shared.GenerateResponseMessage(fmt.Sprintf("no groups of visibility: %s found in the community: %s", groupVisibility, communityId))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	groupsJson, err := json.Marshal(queryGroupList)
	log.Printf("groups fetched: %s", string(groupsJson))
	if err != nil {
		log.Printf("cannot Marshal json: %s", err)
		return
	}
	w.WriteHeader(http.StatusOK)
	w.Write(groupsJson)
}
