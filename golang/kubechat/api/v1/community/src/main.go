package main

import (
	"github.com/julienschmidt/httprouter"
	"log"
	"net/http"
	"shared"
)

func main() {
	shared.DbMigrate(&shared.Community{})
	shared.DbMigrate(&shared.CommunityUser{})
	shared.GetPubKey()
	InitValidators()

	router := httprouter.New()
	router.GET("/community/get/:name", CommunityGet)
	router.GET("/community/get/:name/members", CommunityGetMembers)
	router.POST("/community/create", CommunityCreate)
	router.PATCH("/community/update", CommunityUpdate)

	router.POST("/community/join", CommunityJoin)
	router.POST("/community/invite", CommunityInvite)

	log.Printf("starting server")
	err := http.ListenAndServe(":8081", router)
	if err != nil {
		log.Fatalf("server encountered an error", err)
	}
	log.Printf("server stopped")
}
