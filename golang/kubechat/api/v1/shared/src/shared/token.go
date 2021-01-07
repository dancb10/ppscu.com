package shared

import (
	"fmt"
	"github.com/dgrijalva/jwt-go"
	"github.com/julienschmidt/httprouter"
	"log"
	"net/http"
)

type Token struct {
	Token string `json:"token"`
}

type Claims struct {
	Email string `json:"email"`
	UserId string `json:"user_id"`
	FirstName string `json:"firstname"`
	LastName string `json:"lastname"`
	jwt.StandardClaims
}

func TokenValidate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) Claims {
	w.Header().Set("Content-Type","application/json")
	reqToken := r.Header.Get("Authorization")
	if reqToken == "" {
		msg := GenerateResponseMessage(fmt.Sprintf("no authorization header provided "))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return Claims{}
	}
	claims := &Claims{}
	token, err := jwt.ParseWithClaims(reqToken, claims, func(token *jwt.Token) (interface{}, error) {
		return VerifyKey, nil
	})

	switch err.(type) {
	case nil:
		if !token.Valid {
			msg := GenerateResponseMessage("token not valid")
			w.WriteHeader(http.StatusUnauthorized)
			w.Write(msg)
			return Claims{}
		}
		return *claims

	case *jwt.ValidationError:
		vErr := err.(*jwt.ValidationError)
		switch vErr.Errors {
		case jwt.ValidationErrorExpired:
			msg := GenerateResponseMessage("token expired, get a new one")
			w.WriteHeader(http.StatusUnauthorized)
			w.Write(msg)
			return Claims{}
		default:
			msg := GenerateResponseMessage(fmt.Sprintf("error while parsing token!, err: %+v", vErr.Errors))
			w.WriteHeader(http.StatusInternalServerError)
			log.Printf("validationError error: %+v\n", vErr.Errors)
			w.Write(msg)
			return Claims{}
		}

	default:
		msg := GenerateResponseMessage(fmt.Sprintf("error while parsing token!, err: %+v", err))
		w.WriteHeader(http.StatusInternalServerError)
		log.Printf("token parse error: %v\n", err)
		w.Write(msg)
		return Claims{}
	}
}
