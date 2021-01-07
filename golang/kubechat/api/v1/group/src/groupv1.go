package main
//
//import (
//	"encoding/json"
//	"fmt"
//	"github.com/asaskevich/govalidator"
//	"github.com/jinzhu/gorm"
//	"github.com/julienschmidt/httprouter"
//	uuid "github.com/satori/go.uuid"
//	"log"
//	"net/http"
//	"shared"
//	"time"
//)
//
//var groupType = []string{"democratic", "totalitarian", "semi-democratic", "semi-totalitarian"}
//var groupVisibility = []string{"public", "closed", "invite"}
//
//func InitValidators() {
//	govalidator.TagMap["groupType"] = func(group string) bool {
//		for _, value := range groupType {
//			if value == group {
//				return true
//			}
//		}
//		return false
//	}
//
//	govalidator.TagMap["groupVisibility"] = func(group string) bool {
//		for _, value := range groupVisibility {
//			if value == group {
//				return true
//			}
//		}
//		return false
//	}
//}
//
//func GroupGet(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
//	w.Header().Set("Content-Type","application/json")
//	uid := shared.TokenValidate(w, r, ps).UserId
//	if uid == "" {
//		return
//	}
//
//	queryValues := r.URL.Query()
//	groupName := ps.ByName("name")
//	cid := queryValues.Get("cid")
//	db := shared.DatabaseConn()
//	queryGroup := shared.Group{}
//	queryGroupUser := shared.GroupUser{}
//	db.Where("name = ? AND c_id = ?", groupName, cid).First(&queryGroup)
//	if queryGroup.Name != "" {
//		if queryGroup.Visibility != "public" {
//			db.Where("g_id = ? AND uid = ?", queryGroup.GID, uid).First(&queryGroupUser)
//			if queryGroupUser.GUID != "" {
//				w.WriteHeader(http.StatusOK)
//				groupJson, err := json.Marshal(queryGroup)
//				if err != nil {
//					log.Printf("cannot Marshal json: %s", err)
//				}
//				w.Write(groupJson)
//				return
//			} else {
//				msg := shared.GenerateResponseMessage(fmt.Sprintf("cannot get %s group details, not allowed", groupName))
//				w.WriteHeader(http.StatusBadRequest)
//				w.Write(msg)
//				return
//			}
//		}
//		w.WriteHeader(http.StatusOK)
//		groupJson, err := json.Marshal(queryGroup)
//		if err != nil {
//			log.Printf("cannot Marshal json: %s", err)
//		}
//		w.Write(groupJson)
//		return
//	} else {
//		msg := shared.GenerateResponseMessage(fmt.Sprintf("group %s not found", groupName))
//		w.WriteHeader(http.StatusNotFound)
//		w.Write(msg)
//	}
//}
//
//func GroupCreate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
//	w.Header().Set("Content-Type","application/json")
//	uid := shared.TokenValidate(w, r, ps).UserId
//	if uid == "" {
//		return
//	}
//
//	group := shared.Group{}
//	err := json.NewDecoder(r.Body).Decode(&group)
//	if err != nil {
//		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
//		w.WriteHeader(http.StatusBadRequest)
//		w.Write(msg)
//		return
//	}
//
//	if govalidator.IsNull(group.Name) || !govalidator.IsAlphanumeric(group.Name) {
//		msg := shared.GenerateResponseMessage("group name must contain only alphanum characters and cannot be null")
//		w.WriteHeader(http.StatusBadRequest)
//		w.Write(msg)
//		return
//	}
//	if !govalidator.StringLength(group.Name, "1", "30") {
//		msg := shared.GenerateResponseMessage(fmt.Sprintf("name: 1 < characters < 30"))
//		w.WriteHeader(http.StatusBadRequest)
//		w.Write(msg)
//		return
//	}
//
//	if govalidator.IsNull(group.Type) {
//		group.Type = "democratic"
//	}
//
//	if govalidator.IsNull(group.Visibility) {
//		group.Visibility = "public"
//	}
//
//	if govalidator.IsNull(group.CID) || !govalidator.IsASCII(group.CID) {
//		msg := shared.GenerateResponseMessage("group CID doesn't have correct format")
//		w.WriteHeader(http.StatusBadRequest)
//		w.Write(msg)
//		return
//	}
//
//	if !shared.CheckLabelLength(group.Labels, 30) {
//		msg := shared.GenerateResponseMessage("labels cannot have more than 30 characters each")
//		w.WriteHeader(http.StatusBadRequest)
//		w.Write(msg)
//		return
//	}
//
//	if len(group.CommunityLabels) == 0 {
//		msg := shared.GenerateResponseMessage("must specify community labels")
//		w.WriteHeader(http.StatusBadRequest)
//		w.Write(msg)
//		return
//	}
//
//	if !shared.CheckLabelLength(group.CommunityLabels, 30) {
//		msg := shared.GenerateResponseMessage("labels cannot have more than 30 characters each")
//		w.WriteHeader(http.StatusBadRequest)
//		w.Write(msg)
//		return
//	}
//
//	group.CreatedAt = time.Now().UTC()
//	id, err := uuid.NewV4()
//	if err != nil {
//		log.Printf("could not generate UUID for group: %s", err)
//		return
//	}
//	rid := "grp-" + id.String()
//	group.GID = rid
//
//	_, err = govalidator.ValidateStruct(group)
//	if err != nil {
//		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
//		w.WriteHeader(http.StatusBadRequest)
//		w.Write(msg)
//		return
//	}
//
//	db := shared.DatabaseConn()
//	queryGroup := shared.Group{}
//	groupUser := shared.GroupUser{}
//	db.Where("name = ? AND c_id = ?", group.Name, group.CID).First(&queryGroup)
//	if queryGroup.Name != "" {
//		msg := shared.GenerateResponseMessage(fmt.Sprintf("group %s already exists in %s community ", group.Name, group.CID))
//		w.WriteHeader(http.StatusConflict)
//		w.Write(msg)
//		return
//	} else {
//		fmt.Println(group)
//		db.Create(&group)
//		GroupAddUser(db, groupUser, uid, group.GID, "president")
//		groupJson, err := json.Marshal(group)
//		log.Printf("group created: %s", string(groupJson))
//		if err != nil {
//			log.Printf("cannot Marshal json: %s", err)
//			return
//		}
//		msg := shared.GenerateResponseMessage(fmt.Sprintf("group %s created", group.Name))
//		w.WriteHeader(http.StatusOK)
//		w.Write(msg)
//	}
//}
//
//func GroupUpdate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
//	w.Header().Set("Content-Type","application/json")
//	uid := shared.TokenValidate(w, r, ps).UserId
//	if uid == "" {
//		return
//	}
//
//	group := shared.Group{}
//	err := json.NewDecoder(r.Body).Decode(&group)
//	if err != nil {
//		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
//		w.WriteHeader(http.StatusBadRequest)
//		w.Write(msg)
//		return
//	}
//
//	if govalidator.IsNull(group.Name) || !govalidator.IsAlphanumeric(group.Name) {
//		msg := shared.GenerateResponseMessage("group name must contain only alphanum characters and cannot be null")
//		w.WriteHeader(http.StatusBadRequest)
//		w.Write(msg)
//		return
//	}
//	if !govalidator.StringLength(group.Name, "1", "30") {
//		msg := shared.GenerateResponseMessage(fmt.Sprintf("name: 1 < characters < 30"))
//		w.WriteHeader(http.StatusBadRequest)
//		w.Write(msg)
//		return
//	}
//
//	if govalidator.IsNull(group.GID) || !govalidator.IsAlphanumeric(group.GID) {
//		msg := shared.GenerateResponseMessage("group GID doesn't have correct format")
//		w.WriteHeader(http.StatusBadRequest)
//		w.Write(msg)
//		return
//	}
//
//	db := shared.DatabaseConn()
//	queryGroup := shared.Group{}
//	db.Where("name = ? AND cid = ?", group.Name, group.CID).First(&queryGroup)
//	if queryGroup.Name != "" {
//		db.Model(&group).Where("cid = ?", group.CID).Update(group)
//		log.Printf("group %s, gid: %s was modified: %#v", group.Name, group.CID, group)
//		msg := shared.GenerateResponseMessage("changes saved")
//		w.WriteHeader(http.StatusOK)
//		w.Write(msg)
//	} else {
//		msg := shared.GenerateResponseMessage(fmt.Sprintf("group: %s not found", group.Name))
//		w.WriteHeader(http.StatusNotFound)
//		w.Write(msg)
//	}
//}
//
//func GroupJoin(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
//	w.Header().Set("Content-Type","application/json")
//	uid := shared.TokenValidate(w, r, ps).UserId
//	if uid == "" {
//		return
//	}
//
//	group := shared.Group{}
//	err := json.NewDecoder(r.Body).Decode(&group)
//	if err != nil {
//		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
//		w.WriteHeader(http.StatusBadRequest)
//		w.Write(msg)
//		return
//	}
//
//	queryGroup := shared.Group{}
//	groupUser := shared.GroupUser{}
//	db := shared.DatabaseConn()
//	if GroupCheckUser(db, uid, group.GID) {
//		msg := shared.GenerateResponseMessage(fmt.Sprintf("user: %s already part of group: %s", uid, group.Name))
//		w.WriteHeader(http.StatusOK)
//		w.Write(msg)
//		return
//	}
//	db.Where("g_id = ? AND name = ?", group.GID, group.Name).First(&queryGroup)
//	if queryGroup.Name != "" {
//		if queryGroup.Visibility != "public" {
//			msg := shared.GenerateResponseMessage(fmt.Sprintf("cannot join group %s, not allowed", queryGroup.Name))
//			w.WriteHeader(http.StatusBadRequest)
//			w.Write(msg)
//			return
//		}
//
//		GroupAddUser(db, groupUser, uid, group.GID, "member")
//		msg := shared.GenerateResponseMessage("joined group")
//		w.WriteHeader(http.StatusOK)
//		w.Write(msg)
//	} else {
//		msg := shared.GenerateResponseMessage(fmt.Sprintf("group: %s not found", group.Name))
//		w.WriteHeader(http.StatusNotFound)
//		w.Write(msg)
//	}
//}
//
//func GroupCheckUser(db *gorm.DB, uid string, gid string) bool {
//	queryGroupUser := shared.GroupUser{}
//	db.Where("uid = ? AND g_id = ?", uid, gid).First(&queryGroupUser)
//	if queryGroupUser.GUID != "" {
//		log.Printf("user: %s is already part of this group: %s", uid, gid)
//		return true
//	}
//	return false
//}
//
//func GroupAddUser(db *gorm.DB, groupUser shared.GroupUser, uid string, gid string, role string) {
//	queryGroupUser := shared.GroupUser{}
//	db.Where("uid = ? AND g_id = ?", uid, gid).First(&queryGroupUser)
//	if queryGroupUser.GUID != "" {
//		log.Printf("membership for user: %s and group: %s already exists", uid, gid)
//		return
//	} else {
//		groupUser.Role = role
//		groupUser.GID = gid
//		groupUser.UID = uid
//		id, err := uuid.NewV4()
//		if err != nil {
//			log.Printf("could not generate UUID for group user: %s", err)
//			return
//		}
//		guid := "guid-" + id.String()
//		groupUser.GUID = guid
//		db.Create(&groupUser)
//		log.Printf("user: %s joined group: %s as: %s", uid, gid, role)
//	}
//}
//
//func GroupInvite(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
//	w.Header().Set("Content-Type","application/json")
//	uid := shared.TokenValidate(w, r, ps).UserId
//	if uid == "" {
//		return
//	}
//}
//
//func GroupGetMembers(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
//	w.Header().Set("Content-Type","application/json")
//	uid := shared.TokenValidate(w, r, ps).UserId
//	if uid == "" {
//		return
//	}
//
//	count := 0
//	queryValues := r.URL.Query()
//	groupName := ps.ByName("name")
//	cid := queryValues.Get("cid")
//	db := shared.DatabaseConn()
//	queryGroup := shared.Group{}
//	queryGroupUser := shared.GroupUser{}
//	db.Where("name = ? AND c_id = ?", groupName, cid).First(&queryGroup)
//	if queryGroup.Name != "" {
//		if queryGroup.Visibility != "public" {
//			db.Where("g_id = ? AND uid = ?", queryGroup.GID, uid).First(&queryGroupUser)
//			if queryGroupUser.GUID != "" {
//				db.Model(&shared.GroupUser{}).Where("g_id = ?", queryGroup.GID).Count(&count)
//				w.WriteHeader(http.StatusOK)
//				fmt.Println(count)
//				groupCountJson, err := json.Marshal(count)
//				if err != nil {
//					log.Printf("cannot Marshal json: %s", err)
//				}
//				w.Write(groupCountJson)
//				return
//			} else {
//				msg := shared.GenerateResponseMessage(fmt.Sprintf("cannot get %s group details, not allowed", groupName))
//				w.WriteHeader(http.StatusBadRequest)
//				w.Write(msg)
//				return
//			}
//		}
//		db.Model(&shared.GroupUser{}).Where("g_id = ?", queryGroup.GID).Count(&count)
//		w.WriteHeader(http.StatusOK)
//		groupCountJson, err := json.Marshal(count)
//		if err != nil {
//			log.Printf("cannot Marshal json: %s", err)
//		}
//		w.Write(groupCountJson)
//		return
//	} else {
//		msg := shared.GenerateResponseMessage(fmt.Sprintf("group %s not found", groupName))
//		w.WriteHeader(http.StatusNotFound)
//		w.Write(msg)
//	}
//}
//
//func GroupsGet(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
//	w.Header().Set("Content-Type","application/json")
//	uid := shared.TokenValidate(w, r, ps).UserId
//	if uid == "" {
//		return
//	}
//
//	db := shared.DatabaseConn()
//	groups := []shared.GroupUser{}
//	db.Where("uid = ?", uid).Find(&groups)
//	if len(groups) != 0 {
//		w.WriteHeader(http.StatusOK)
//		groupsJson, err := json.Marshal(groups)
//		if err != nil {
//			log.Printf("cannot Marshal json: %s", err)
//		}
//		w.Write(groupsJson)
//		return
//	} else {
//		msg := shared.GenerateResponseMessage("you are part of no groups yet")
//		w.WriteHeader(http.StatusNotFound)
//		w.Write(msg)
//	}
//}