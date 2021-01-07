package main

import (
	"github.com/julienschmidt/httprouter"
	"log"
	"net/http"
	"shared"
)

func main() {
shared.DbMigrate(&shared.Community{})
shared.GetPubKey()
InitValidators()

router := httprouter.New()
router.GET("/community/get", CommunityGet)
router.POST("/community/create", CommunityCreate)
router.PATCH("/community/update", CommunityUpdate)

router.PATCH("/community/join", CommunityJoin)

log.Printf("starting server")
err := http.ListenAndServe(":8081", router)
if err != nil {
	log.Fatalf("server encountered an ")
}
	log.Printf("server stopped")
}
