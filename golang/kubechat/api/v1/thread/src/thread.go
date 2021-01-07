package main

import (
	"encoding/json"
	"fmt"
	"github.com/asaskevich/govalidator"
	"github.com/gocql/gocql"
	"github.com/julienschmidt/httprouter"
	uuid "github.com/satori/go.uuid"
	"log"
	"net/http"
	"regexp"
	"shared"
	"time"
)

func InitValidators() {
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

var ThreadsInsert = fmt.Sprintf("INSERT INTO threads (thread_id,create_date,group_id,update_date,name,summary,content,labels,plabels) VALUES (?,?,?,?,?,?,?,?,?)")
var ThreadsByGroupInsert = fmt.Sprintf("INSERT INTO threads_by_group (group_id,name,create_date,labels,plabels,summary,thread_id) VALUES (?,?,?,?,?,?,?)")
var ThreadsByGroupSelect = fmt.Sprintf("SELECT group_id,name FROM threads_by_group WHERE group_id = ? AND name = ? LIMIT 1")

var ThreadsByGroupCreateDateInsert = fmt.Sprintf("INSERT INTO threads_by_group_create_date (group_id,day,create_date,labels,name,plabels,summary,thread_id) VALUES (?,?,?,?,?,?,?,?)")
var ThreadsByGroupCreateDateSelect = fmt.Sprintf("SELECT * FROM threads_by_group_create_date WHERE group_id = ? AND day = ?")

var ThreadGetSingle = fmt.Sprintf("SELECT * FROM threads WHERE thread_id = ? AND group_id = ? LIMIT 1")
var ThreadVoteInsert = fmt.Sprintf("INSERT INTO thread_votes (thread_id,user_id,day,email,first_name,last_name,nick_name,vote_date) VALUES (?,?,?,?,?,?,?,?)")
var ThreadVoteDelete = fmt.Sprintf("DELETE FROM thread_votes WHERE thread_id = ? AND user_id = ?")
var ThreadVoteSelect = fmt.Sprintf("SELECT * FROM thread_votes WHERE thread_id = ? AND user_id = ?")
var ThreadVotesByTimeInsert = fmt.Sprintf("INSERT INTO thread_votes_by_time (thread_id,user_id,day,email,first_name,last_name,nick_name,vote_date) VALUES (?,?,?,?,?,?,?,?)")
var ThreadVotesByTimeSelect = fmt.Sprintf("SELECT * FROM thread_votes_by_time WHERE thread_id = ? AND day = ?")
var ThreadVotesByTimeDelete = fmt.Sprintf("DELETE FROM thread_votes_by_time WHERE thread_id = ? AND day = ? AND user_id = ?")

func ThreadCreate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}

	thread := shared.Thread{}
	err := json.NewDecoder(r.Body).Decode(&thread)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	id, err := uuid.NewV4()
	if err != nil {
		log.Printf("could not generate UUID for thread: %s", err)
		return
	}

	currentTime := time.Now()
	year := currentTime.Year()
	month := currentTime.Month()
	day := currentTime.Day()

	thread.UserId = uid
	thread.ThreadId = id.String()
	thread.Day = fmt.Sprintf("%d-%d-%d", year, month, day)
	thread.CreateDate =	currentTime
	thread.UpdateDate = currentTime

	_, err = govalidator.ValidateStruct(thread)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}
	var queryThread shared.Thread
	db := shared.DatabaseConnCassandra()
	log.Printf("Executing query: %s", ThreadsByGroupSelect)
	if err := db.Query(ThreadsByGroupSelect, thread.GroupId, thread.Name).Consistency(gocql.One).Scan(&queryThread.GroupId, &queryThread.Name); err != nil {
		switch err {
		case nil:
			// do nothing
		case gocql.ErrNotFound:
			log.Printf("thread: '%s' not found in the group: %s, creating it...", thread.Name, thread.GroupId)
		default:
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage(fmt.Sprintf("error occured: %s", err))
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}

	if queryThread.Name != "" {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("thread: '%s' already exists in group: %s", thread.Name, thread.GroupId))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	go func() {
		log.Printf("Executing query: %s", ThreadsInsert)
		if err := db.Query(ThreadsInsert, thread.ThreadId, thread.CreateDate, thread.GroupId, thread.UpdateDate,
			thread.Name, thread.Summary, thread.Content, thread.Labels, thread.Plabels).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()

	go func() {
		log.Printf("Executing query: %s", ThreadsByGroupInsert)
		if err := db.Query(ThreadsByGroupInsert, thread.GroupId, thread.Name, thread.CreateDate, thread.Labels,
			thread.Plabels, thread.Summary, thread.ThreadId).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()
	go func() {
		log.Printf("Executing query: %s", ThreadsByGroupCreateDateInsert)
		if err := db.Query(ThreadsByGroupCreateDateInsert, thread.GroupId, thread.Day, thread.CreateDate,
			thread.Labels, thread.Name, thread.Plabels,thread.Summary, thread.ThreadId).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()

	threadJson, err := json.Marshal(thread)
	log.Printf("thread created: %s", string(threadJson))
	if err != nil {
		log.Printf("cannot Marshal json: %s", err)
		return
	}
	msg := shared.GenerateResponseMessage(fmt.Sprintf("thread: '%s' created in group: %s", thread.Name, thread.GroupId))
	w.WriteHeader(http.StatusOK)
	w.Write(msg)
}

func ThreadUpdate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func ThreadDelete(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func ThreadVoteUp(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	token := shared.TokenValidate(w, r, ps)
	uid := token.UserId
	if uid == "" {
		return
	}

	thread := shared.ThreadVote{}
	err := json.NewDecoder(r.Body).Decode(&thread)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	currentTime := time.Now()
	thread.VoteDate = currentTime
	year := currentTime.Year()
	month := currentTime.Month()
	day := currentTime.Day()
	thread.Day = fmt.Sprintf("%d-%d-%d", year, month, day)
	thread.FirstName = token.FirstName
	thread.LastName = token.LastName
	thread.UserId = uid
	thread.Email = token.Email
	fmt.Println(thread)

	_, err = govalidator.ValidateStruct(thread)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	db := shared.DatabaseConnCassandra()
	go func() {
		log.Printf("Executing query: %s", ThreadVoteInsert)
		if err := db.Query(ThreadVoteInsert, thread.ThreadId, thread.UserId, thread.Day, thread.Email, thread.FirstName, thread.LastName,
			thread.Nickname, thread.VoteDate).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()
	go func() {
		log.Printf("Executing query: %s", ThreadVotesByTimeInsert)
		if err := db.Query(ThreadVotesByTimeInsert, thread.ThreadId, thread.UserId, thread.Day, thread.Email, thread.FirstName, thread.LastName,
			thread.Nickname, thread.VoteDate).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()

	msg := shared.GenerateResponseMessage(fmt.Sprintf("user: %s voted up thread: %s", thread.Email, thread.ThreadId))
	w.WriteHeader(http.StatusOK)
	w.Write(msg)
}

func ThreadVoteDown(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	token := shared.TokenValidate(w, r, ps)
	uid := token.UserId
	if uid == "" {
		return
	}

	thread := shared.ThreadVote{}
	err := json.NewDecoder(r.Body).Decode(&thread)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	thread.UserId = uid
	//dummy day
	thread.Day = "1900-01-01"
	_, err = govalidator.ValidateStruct(thread)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	db := shared.DatabaseConnCassandra()
	var queryThread shared.ThreadVote
	log.Printf("Executing query: %s", ThreadVoteSelect)
	if err := db.Query(ThreadVoteSelect, thread.ThreadId, thread.UserId).Consistency(gocql.One).Scan(&queryThread.ThreadId,
		&queryThread.UserId, &queryThread.Day, &queryThread.Email, &queryThread.FirstName, &queryThread.LastName,
		&queryThread.Nickname, &queryThread.VoteDate); err != nil {
		switch err {
		case nil:
			// do nothing
		case gocql.ErrNotFound:
			log.Printf("thread: user %s didn't vote in thread %s", thread.ThreadId, thread.UserId)
		default:
			log.Printf("an error has occured: %s", err)
			return
		}
	}
	thread.Day = queryThread.Day

	go func() {
		log.Printf("Executing query: %s", ThreadVoteDelete)
		if err := db.Query(ThreadVoteDelete, thread.ThreadId, thread.UserId).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()
	go func() {
		log.Printf("Executing query: %s with %s %s %s", ThreadVotesByTimeDelete, thread.ThreadId, thread.Day, thread.UserId)
		if err := db.Query(ThreadVotesByTimeDelete, thread.ThreadId, thread.Day, thread.UserId).Exec(); err != nil {
			log.Printf("an error has occured: %s", err)
			msg := shared.GenerateResponseMessage("server has encountered an error")
			w.WriteHeader(http.StatusInternalServerError)
			w.Write(msg)
			return
		}
	}()

	msg := shared.GenerateResponseMessage(fmt.Sprintf("user: %s voted down thread: %s", thread.Email, thread.ThreadId))
	w.WriteHeader(http.StatusOK)
	w.Write(msg)
}

func ThreadGet(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}

	queryValues := r.URL.Query()
	var queryThreadGet shared.ThreadGet
	queryThreadGet.ThreadId = queryValues.Get("thread_id")
	queryThreadGet.GroupId = queryValues.Get("group_id")

	_, err := govalidator.ValidateStruct(queryThreadGet)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	var queryThread shared.Thread
	db := shared.DatabaseConnCassandra()
	log.Printf("Executing query: %s", ThreadGetSingle)
	if err := db.Query(ThreadGetSingle, queryThreadGet.ThreadId, queryThreadGet.GroupId).Consistency(gocql.One).Scan(&queryThread.ThreadId,
		&queryThread.GroupId, &queryThread.Content, &queryThread.CreateDate, &queryThread.Labels,
		&queryThread.Name, &queryThread.Plabels, &queryThread.Summary, &queryThread.UpdateDate); err != nil {
		switch err {
		case nil:
			// do nothing
		case gocql.ErrNotFound:
			log.Printf("thread: '%s' not found in the group: %s", queryThreadGet.ThreadId, queryThreadGet.GroupId)
			msg := shared.GenerateResponseMessage("thread not found in group")
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

	threadJson, err := json.Marshal(queryThread)
	log.Printf("thread fetched: %s", string(threadJson))
	if err != nil {
		log.Printf("cannot Marshal json: %s", err)
		return
	}
	w.WriteHeader(http.StatusOK)
	w.Write(threadJson)
}

func ThreadVotes(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}

	queryValues := r.URL.Query()
	threadId := queryValues.Get("thread_id")
	day := queryValues.Get("day")
	threadGetVotes := shared.ThreadVotesGet{ThreadId: threadId, Day: day}
	_, err := govalidator.ValidateStruct(threadGetVotes)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	var queryThreadVote shared.ThreadVote
	var queryThreadVoteList []shared.ThreadVote
	db := shared.DatabaseConnCassandra()
	log.Printf("Executing query: %s", ThreadVotesByTimeSelect)
	iter := db.Query(ThreadVotesByTimeSelect, threadId, day).Iter()
	for iter.Scan(&queryThreadVote.ThreadId, &queryThreadVote.Day, &queryThreadVote.UserId, &queryThreadVote.Email,
		&queryThreadVote.FirstName, &queryThreadVote.LastName, &queryThreadVote.Nickname, &queryThreadVote.VoteDate) {
		queryThreadVoteList = append(queryThreadVoteList, queryThreadVote)
	}

	if err := iter.Close(); err != nil {
		log.Fatal(err)
	}
	if queryThreadVoteList == nil {
		log.Printf("no votes found for thread: %s for day: %s", threadId, day)
		msg := shared.GenerateResponseMessage(fmt.Sprintf("no votes found for thread: %s for day: %s", threadId, day))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	threadVotesJson, err := json.Marshal(queryThreadVoteList)
	log.Printf("thread votes fetched: %s", string(threadVotesJson))
	if err != nil {
		log.Printf("cannot Marshal json: %s", err)
		return
	}
	w.WriteHeader(http.StatusOK)
	w.Write(threadVotesJson)
}

func ThreadsByGroupCreateDate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}

	queryValues := r.URL.Query()
	groupId := queryValues.Get("group_id")
	day := queryValues.Get("day")
	threadGetByGroupCreateDate := shared.ThreadGetByGroupCreateDate{GroupId: groupId, Day: day}
	_, err := govalidator.ValidateStruct(threadGetByGroupCreateDate)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	var queryThread shared.Thread
	var queryThreadList []shared.Thread
	db := shared.DatabaseConnCassandra()
	log.Printf("Executing query: %s", ThreadsByGroupCreateDateSelect)
	iter := db.Query(ThreadsByGroupCreateDateSelect, groupId, day).Iter()
	for iter.Scan(&queryThread.GroupId, &queryThread.Day, &queryThread.CreateDate, &queryThread.Labels, &queryThread.Name,
		&queryThread.Plabels, &queryThread.Summary, &queryThread.ThreadId) {
		queryThreadList = append(queryThreadList, queryThread)
	}
	if err := iter.Close(); err != nil {
		log.Fatal(err)
	}
	if queryThreadList == nil {
		log.Printf("no threads found in the group: %s for day: %s", groupId, day)
		msg := shared.GenerateResponseMessage(fmt.Sprintf("no threads found in the group: %s for day: %s", groupId, day))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	threadsJson, err := json.Marshal(queryThreadList)
	log.Printf("threads fetched: %s", string(threadsJson))
	if err != nil {
		log.Printf("cannot Marshal json: %s", err)
		return
	}
	w.WriteHeader(http.StatusOK)
	w.Write(threadsJson)
}
