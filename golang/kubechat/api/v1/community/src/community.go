package main

import (
	"encoding/json"
	"fmt"
	"github.com/asaskevich/govalidator"
	"github.com/jinzhu/gorm"
	"github.com/julienschmidt/httprouter"
	uuid "github.com/satori/go.uuid"
	"log"
	"net/http"
	"shared"
	"time"
)

var communityType = []string{"public", "closed", "invite"}
var groupCreation = []string{"anyone", "admins", "members"}

func InitValidators() {
	govalidator.TagMap["communityType"] = func(community string) bool {
		for _, value := range communityType {
			if value == community {
				return true
			}
		}
		return false
	}

	govalidator.TagMap["groupCreation"] = func(community string) bool {
		for _, value := range groupCreation {
			if value == community {
				return true
			}
		}
		return false
	}
}

func CommunityGet(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps)
	if uid == "" {
		return
	}

	communityName := ps.ByName("name")
	db := shared.DatabaseConn()
	queryCommunity := shared.Community{}
	queryCommunityUser := shared.CommunityUser{}
	db.Where("name = ?", communityName).First(&queryCommunity)
	if queryCommunity.Name != "" {
		log.Printf("community %s data requested: %#v", queryCommunity.Name, queryCommunity)
		if queryCommunity.Visibility != "public" {
			db.Where("c_id = ? AND uid = ?", queryCommunity.CID, uid).First(&queryCommunityUser)
			if queryCommunityUser.CUID != "" {
				w.WriteHeader(http.StatusOK)
				communityJson, err := json.Marshal(queryCommunity)
				if err != nil {
					log.Printf("cannot Marshal json: %s", err)
				}
				w.Write(communityJson)
				return
			} else {
				msg := shared.GenerateResponseMessage(fmt.Sprintf("cannot get %s community details, not allowed", communityName))
				w.WriteHeader(http.StatusBadRequest)
				w.Write(msg)
				return
			}
		}
		w.WriteHeader(http.StatusOK)
		communityJson, err := json.Marshal(queryCommunity)
		if err != nil {
			log.Printf("cannot Marshal json: %s", err)
		}
		w.Write(communityJson)
		return
	} else {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("community %s not found", communityName))
		w.WriteHeader(http.StatusNotFound)
		w.Write(msg)
	}
}

func CommunityCreate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps)
	if uid == "" {
		return
	}
	community := shared.Community{}
	err := json.NewDecoder(r.Body).Decode(&community)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	if govalidator.IsNull(community.Name) || !govalidator.IsAlphanumeric(community.Name) {
		msg := shared.GenerateResponseMessage("community name must contain only alphanum characters and cannot be null")
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}
	if !govalidator.StringLength(community.Name, "1", "30") {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("name: 1 < characters < 30"))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	if govalidator.IsNull(community.Visibility) {
		community.Visibility = "public"
	}

	if govalidator.IsNull(community.GroupCreation) {
		community.GroupCreation = "anyone"
	}

	community.Labels = append(community.Labels, community.Name)
	if !shared.CheckLabelLength(community.Labels, 30) {
		msg := shared.GenerateResponseMessage("labels cannot have more than 30 characters each")
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	_, err = govalidator.ValidateStruct(community)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	community.CreatedAt = time.Now().UTC()
	id, err := uuid.NewV4()
	if err != nil {
		log.Printf("could not generate UUID for community: %s", err)
		return
	}
	rid := "com-" + id.String()
	community.CID = rid

	db := shared.DatabaseConn()
	queryCommunity := shared.Community{}
	communityUser := shared.CommunityUser{}
	db.Where("name = ?", community.Name).First(&queryCommunity)
	if queryCommunity.Name != "" {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("community %s already exists", community.Name))
		w.WriteHeader(http.StatusConflict)
		w.Write(msg)
		return
	} else {
		db.Create(&community)
		CommunityAddUser(db, communityUser, uid, community.CID, "president")
		communityJson, err := json.Marshal(community)
		log.Printf("community created: %s", string(communityJson))
		if err != nil {
			log.Printf("cannot Marshal json: %s", err)
			return
		}

		msg := shared.GenerateResponseMessage(fmt.Sprintf("community %s created", community.Name))
		w.WriteHeader(http.StatusOK)
		w.Write(msg)
	}
}

func CommunityUpdate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps)
	if uid == "" {
		return
	}

	community := shared.Community{}
	err := json.NewDecoder(r.Body).Decode(&community)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}
	_, err = govalidator.ValidateStruct(community)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	queryCommunity := shared.Community{}
	db := shared.DatabaseConn()
	db.Where("name = ?", community.Name).First(&queryCommunity)
	if queryCommunity.Name != "" {
		db.Model(&community).Where("name = ?", community.Name).Update(community)
		log.Printf("community %s details modified: %#v", community.Name, community)
		msg := shared.GenerateResponseMessage("changes saved")
		w.WriteHeader(http.StatusOK)
		w.Write(msg)
	} else {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("community: %s not found", community.Name))
		w.WriteHeader(http.StatusNotFound)
		w.Write(msg)
	}
}

func CommunityDelete(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func CommunityJoin(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps)
	if uid == "" {
		return
	}

	community := shared.Community{}
	err := json.NewDecoder(r.Body).Decode(&community)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	queryCommunity := shared.Community{}
	communityUser := shared.CommunityUser{}
	db := shared.DatabaseConn()
	if CommunityCheckUser(db, uid, community.CID) {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("user: %s already part of community: %s", uid, community.Name))
		w.WriteHeader(http.StatusOK)
		w.Write(msg)
		return
	}
	db.Where("c_id = ? AND name = ?", community.CID, community.Name).First(&queryCommunity)
	if queryCommunity.Name != "" {
		if queryCommunity.Visibility != "public" {
			msg := shared.GenerateResponseMessage(fmt.Sprintf("cannot join community %s, not allowed", community.Name))
			w.WriteHeader(http.StatusBadRequest)
			w.Write(msg)
			return
		}

		CommunityAddUser(db, communityUser, uid, community.CID, "member")
		msg := shared.GenerateResponseMessage("joined community")
		w.WriteHeader(http.StatusOK)
		w.Write(msg)
	} else {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("community: %s not found", community.Name))
		w.WriteHeader(http.StatusNotFound)
		w.Write(msg)
	}
}

func CommunityCheckUser(db *gorm.DB, uid string, cid string) bool {
	queryCommunityUser := shared.CommunityUser{}
	db.Where("uid = ? AND c_id = ?", uid, cid).First(&queryCommunityUser)
	if queryCommunityUser.CUID != "" {
		log.Printf("user: %s is already part of this community: %s", uid, cid)
		return true
	}
	return false
}

func CommunityAddUser(db *gorm.DB, communityUser shared.CommunityUser, uid string, cid string, role string) {
	queryCommunityUser := shared.CommunityUser{}
	db.Where("uid = ? AND c_id = ?", uid, cid).First(&queryCommunityUser)
	if queryCommunityUser.CUID != "" {
		log.Printf("membership for user: %s and community: %s already exists", uid, cid)
		return
	} else {
		communityUser.Role = role
		communityUser.CID = cid
		communityUser.UID = uid
		id, err := uuid.NewV4()
		if err != nil {
			log.Printf("could not generate UUID for community user: %s", err)
			return
		}
		cuid := "cuid-" + id.String()
		communityUser.CUID = cuid
		db.Create(&communityUser)
		log.Printf("user: %s joined community: %s as: %s", uid, cid, role)
	}
}

func CommunityInvite(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps)
	if uid == "" {
		return
	}
}

func CommunityGetMembers(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps)
	if uid == "" {
		return
	}
	count := 0
	communityName := ps.ByName("name")
	db := shared.DatabaseConn()
	queryCommunity := shared.Community{}
	queryCommunityUser := shared.CommunityUser{}
	db.Where("name = ?", communityName).First(&queryCommunity)
	if queryCommunity.Name != "" {
		log.Printf("community %s data requested: %#v", queryCommunity.Name, queryCommunity)
		if queryCommunity.Visibility != "public" {
			db.Where("c_id = ? AND uid = ?", queryCommunity.CID, uid).First(&queryCommunityUser)
			if queryCommunityUser.CUID != "" {
				db.Model(&shared.CommunityUser{}).Where("c_id = ?", queryCommunity.CID).Count(&count)
				w.WriteHeader(http.StatusOK)
				communityCountJson, err := json.Marshal(count)
				if err != nil {
					log.Printf("cannot Marshal json: %s", err)
				}
				w.Write(communityCountJson)
				return
			} else {
				msg := shared.GenerateResponseMessage(fmt.Sprintf("cannot get %s community details, not allowed", communityName))
				w.WriteHeader(http.StatusBadRequest)
				w.Write(msg)
				return
			}
		}
		db.Model(&shared.CommunityUser{}).Where("c_id = ?", queryCommunity.CID).Count(&count)
		w.WriteHeader(http.StatusOK)
		communityCountJson, err := json.Marshal(count)
		if err != nil {
			log.Printf("cannot Marshal json: %s", err)
		}
		w.Write(communityCountJson)
		return
	} else {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("community %s not found", communityName))
		w.WriteHeader(http.StatusNotFound)
		w.Write(msg)
	}
}