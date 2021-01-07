package main

import (
	"github.com/julienschmidt/httprouter"
	"log"
	"net/http"
	"shared"
)

func main() {
	shared.GetPubKey()
	InitValidators()
	router := httprouter.New()
	router.GET("/thread/get", ThreadGet)
	router.POST("/thread/create", ThreadCreate)
	router.PATCH("/thread/update", ThreadUpdate)
	router.DELETE("/thread/delete", ThreadDelete)

	router.GET("/thread/get/votes", ThreadVotes)
	router.POST("/thread/vote/create", ThreadVoteUp)
	router.DELETE("/thread/vote/delete", ThreadVoteDown)

	router.GET("/threads/get/bygroupcreatedate", ThreadsByGroupCreateDate)

	log.Printf("starting server")
	err := http.ListenAndServe(":8090", router)
	if err != nil {
		log.Fatalf("server encountered an error", err)
	}
	log.Printf("server stopped")
}
