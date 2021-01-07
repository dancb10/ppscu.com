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
//InitValidators()

router := httprouter.New()
router.GET("/votes/get", VotesGet)

router.GET("/vote/get", VoteGet)
router.POST("/vote/create", VoteCreate)
router.POST("/vote/submit", VoteSubmit)
router.POST("/vote/delete", VoteDelete)




router.GET("/vote/rule/get", VoteGet)
router.GET("/vote/rule/create", VoteGet)
router.GET("/vote/rule/delete", VoteGet)

log.Printf("starting server")
err := http.ListenAndServe(":8081", router)
if err != nil {
	log.Fatalf("server encountered an ")
}
	log.Printf("server stopped")
}
