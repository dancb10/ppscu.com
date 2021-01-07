package main

import (
	"github.com/julienschmidt/httprouter"
	"log"
	"net/http"
	"shared"
)

func main() {
	shared.GetPubKey()
	router := httprouter.New()

	log.Printf("starting server")
	err := http.ListenAndServe(":8099", router)
	if err != nil {
		log.Fatalf("server encountered an error", err)
	}
	log.Printf("server stopped")
}
