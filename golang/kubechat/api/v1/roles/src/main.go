package main

import (
	"encoding/json"
	"github.com/julienschmidt/httprouter"
	"log"
	"net/http"
	"os"
)

type Config struct {
	Port     string `yaml:"port"`
	Database struct {
		Dialect  string `yaml:"dialect"`
		Host     string `yaml:"host"`
		Port     string `yaml:"port"`
		Db 		 string `yaml:"db"`
		Username string `yaml:"username"`
		Password string `yaml:"password"`
	} `yaml:"database"`
}

type ResponseMessage struct {
	Msg	string
}

var AUTH_SERVER_PORT = os.Getenv("AUTH_SERVER_PORT")
var AUTH_DATABASE_DIALECT = os.Getenv("AUTH_DATABASE_DIALECT")
var AUTH_DATABASE_HOST = os.Getenv("AUTH_DATABASE_HOST")
var AUTH_DATABASE_PORT = os.Getenv("AUTH_DATABASE_PORT")
var AUTH_DATABASE_DB = os.Getenv("AUTH_DATABASE_DB")
var AUTH_DATABASE_USERNAME = os.Getenv("AUTH_DATABASE_USERNAME")
var AUTH_DATABASE_PASSWORD = os.Getenv("AUTH_DATABASE_PASSWORD")

func main() {
	DbMigrate(&Group{})

	router := httprouter.New()

	router.GET("/community/get",CommunityGet)
	router.POST("/community/create", CommunityCreate)
	router.POST("/community/update", CommunityUpdate)
	router.POST("/community/delete", CommunityDelete)
	router.POST("/community/join", CommunityJoin)

	router.GET("/group/get", GroupGet)
	router.POST("/group/create", GroupCreate)
	router.POST("/group/update", GroupUpdate)
	router.POST("/group/delete", GroupDelete)
	router.POST("/group/follow", GroupFollow)

	router.GET("/thread/get",ThreadGet)
	router.POST("/thread/create", ThreadCreate)
	router.POST("/thread/update", ThreadUpdate)
	router.POST("/thread/delete", ThreadDelete)
	router.POST("/thread/replay", ThreadReplay)
	router.POST("/thread/follow", ThreadFollow)

	log.Printf("starting server")
	err := http.ListenAndServe(":8081", router)
	if err != nil {
		log.Fatalf("server encountered an ")
	}
	log.Printf("server stopped")
}

func GenerateResponseMessage(s string) []byte {
	msg := ResponseMessage{s}
	msgJson, err := json.Marshal(msg)
	if err != nil {
		panic(err)
	}
	return msgJson
}
