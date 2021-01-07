package main

import (
	"github.com/julienschmidt/httprouter"
	"net/http"
)


// voteType = []string{"banUser","ruleCreate","promoteToAdmin","userOfTheMonth","ruleDelete","reportUser", "reportAdmin"
// "electAdmins", "impeachAdmin", "updateGroup", "createPoll", "generalElections"}
//

func VoteCreate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func VoteGet(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func VoteUpdate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func VoteDelete(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func VoteSubmit(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func VoteGetResults(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}




func ActionBanUser(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func ActionAddRule(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func ActionDeleteRule(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func ActionPromoteToAdmin(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func ActionDemoteAdmin(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func ActionUserOfTheMonth(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func ActionSetAdminVotePeriod(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func ActionGeneralElections(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func ActionReportUser(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func ActionReportAdmin(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}

func ActionImpeachAdmin(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
}