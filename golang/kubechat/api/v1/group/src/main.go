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
	router.GET("/group/get/:group_id", GroupGet)
	router.POST("/group/create", GroupCreate)
	router.PATCH("/group/update", GroupUpdate)
	router.DELETE("/group/delete", GroupDelete)

	router.GET("/groups/get/bycommunitycreatedate", GroupsByCommunityCreateDate)
	router.GET("/groups/get/bycommunitytype", GroupsByCommunityType)
	router.GET("/groups/get/bycommunityvisibility", GroupsByCommunityVisibility)

	log.Printf("starting server")
	err := http.ListenAndServe(":8082", router)
	if err != nil {
		log.Fatalf("server encountered an error", err)
	}
	log.Printf("server stopped")
}
