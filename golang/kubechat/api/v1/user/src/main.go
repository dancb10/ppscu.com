package main

import (
	"github.com/julienschmidt/httprouter"
	"log"
	"net/http"
	"shared"
)

func main() {
	shared.DbMigrate(&shared.User{})
	shared.DbMigrate(&shared.UserDetails{})
	shared.GetPrivKey()
	shared.GetPubKey()
	InitValidators()

	router := httprouter.New()
	router.POST("/user/create", UserCreate)
	router.GET("/user/get", UserGet)
	router.GET("/user/get/details", UserGetDetails)
	router.PATCH("/user/update", UserUpdate)
	router.PATCH("/user/update/details", UserUpdateDetails)

	router.POST("/user/login", UserLogin)
	router.POST("/user/refresh", UserRefresh)

	log.Printf("starting server")
	err := http.ListenAndServe(":8080", router)
	if err != nil {
		log.Fatalf("server encountered an error", err)
	}
	log.Printf("server stopped")
}
