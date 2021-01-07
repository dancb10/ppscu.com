package main

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"github.com/asaskevich/govalidator"
	"github.com/dgrijalva/jwt-go"
	"github.com/julienschmidt/httprouter"
	"github.com/satori/go.uuid"
	"log"
	"net/http"
	"shared"
	"time"
)

func InitValidators() {
	govalidator.TagMap["checkUUID"] = func(thread string) bool {
		if govalidator.IsUUIDv4(thread) {
			return true
		}
		return false
	}
}

func UserCreate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	user := shared.User{}
	err := json.NewDecoder(r.Body).Decode(&user)

	_, err = govalidator.ValidateStruct(user)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}
	password := sha256.Sum256([]byte(user.Password))
	user.Password = hex.EncodeToString(password[:])
	user.CreatedAt = time.Now().UTC()
	id, err := uuid.NewV4()
	if err != nil {
		log.Printf("could not generate UUID for user: %s", err)
		return
	}
	uid := id.String()
	user.UID = uid

	db := shared.DatabaseConn()
	queryUser := shared.User{}
	detailsUser := shared.UserDetails{UID:uid}
	db.Where("email = ?", user.Email).First(&queryUser)
	if queryUser.Email != "" {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("user %s already exists", user.Email))
		w.WriteHeader(http.StatusConflict)
		w.Write(msg)
		return
	} else {
		db.Create(&user)
		db.Create(&detailsUser)
		userJson, err := json.Marshal(user)
		log.Printf("user created: %s", string(userJson))
		if err != nil {
			log.Printf("cannot Marshal json: %s", err)
			return
		}
		msg := shared.GenerateResponseMessage(fmt.Sprintf("user %s created", user.Email))
		w.WriteHeader(http.StatusOK)
		w.Write(msg)
	}
}

func UserUpdate(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}
	currentEmail := shared.TokenValidate(w, r, ps).Email

	user := shared.User{}
	err := json.NewDecoder(r.Body).Decode(&user)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	_, err = govalidator.ValidateStruct(user)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}
	password := sha256.Sum256([]byte(user.Password))
	user.Password = hex.EncodeToString(password[:])

	db := shared.DatabaseConn()
	queryEmail := shared.User{}
	if (user.Email != "") && (user.Email != currentEmail) {
		db.Where("email = ?", user.Email).First(&queryEmail)
		if queryEmail.Email != "" {
			msg := shared.GenerateResponseMessage(fmt.Sprintf("cannot use this email %s", user.Email))
			w.WriteHeader(http.StatusConflict)
			w.Write(msg)
			return
		}
	}

	queryUser := shared.User{}
	db.Where("uid = ?", uid).First(&queryUser)
	if queryUser.Email != "" {
		db.Model(&user).Where("uid = ?", uid).Update(user)
		log.Printf("user %s, uid: %s modified its details: %#v", queryUser.Email, uid, user)
		msg := shared.GenerateResponseMessage("changes saved")
		w.WriteHeader(http.StatusOK)
		w.Write(msg)
	} else {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("user: %s not found", currentEmail))
		w.WriteHeader(http.StatusNotFound)
		w.Write(msg)
	}
}

func UserUpdateDetails(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}
	currentEmail := shared.TokenValidate(w, r, ps).Email

	user := shared.UserDetails{}
	user.UID = uid
	err := json.NewDecoder(r.Body).Decode(&user)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	_, err = govalidator.ValidateStruct(user)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("%s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	db := shared.DatabaseConn()
	queryUser := shared.UserDetails{}
	db.Where("uid = ?", uid).First(&queryUser)
	if queryUser.UID != "" {
		db.Model(&user).Where("uid = ?", uid).Update(user)
		log.Printf("user %s, modified its details: %#v", queryUser.UID, user)
		msg := shared.GenerateResponseMessage("changes saved")
		w.WriteHeader(http.StatusOK)
		w.Write(msg)
	} else {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("user: %s details not found", currentEmail))
		w.WriteHeader(http.StatusNotFound)
		w.Write(msg)
	}
}

func UserGet(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}

	db := shared.DatabaseConn()
	queryUser := shared.User{}
	db.Where("uid = ?", uid).First(&queryUser)
	if queryUser.Email != "" {
		log.Printf("user %s data requested: %#v", queryUser.Email)
		queryUser.Password = ""
		queryUser.UID = ""
		w.WriteHeader(http.StatusOK)
		userJson, err := json.Marshal(queryUser)
		if err != nil {
			log.Printf("cannot Marshal json: %s", err)
		}
		w.Write(userJson)
		return
	} else {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("user %s not found", queryUser.Email))
		w.WriteHeader(http.StatusNotFound)
		w.Write(msg)
	}
}

func UserGetDetails(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	w.Header().Set("Content-Type","application/json")
	uid := shared.TokenValidate(w, r, ps).UserId
	if uid == "" {
		return
	}

	db := shared.DatabaseConn()
	queryUser := shared.UserDetails{}
	db.Where("uid = ?", uid).First(&queryUser)
	if queryUser.UID != "" {
		log.Printf("user %s details requested: %#v", queryUser.UID)
		queryUser.UID = ""
		w.WriteHeader(http.StatusOK)
		userJson, err := json.Marshal(queryUser)
		if err != nil {
			log.Printf("cannot Marshal json: %s", err)
		}
		w.Write(userJson)
		return
	} else {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("user details not found"))
		w.WriteHeader(http.StatusNotFound)
		w.Write(msg)
	}
}

func UserLogin(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	var cred shared.UserCredentials
	w.Header().Set("Content-Type","application/json")
	err := json.NewDecoder(r.Body).Decode(&cred)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("json not correct %s ", err))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	db := shared.DatabaseConn()
	queryUser := shared.User{}
	db.Where("email = ?", cred.Email).First(&queryUser)
	db.Close()

	password := sha256.Sum256([]byte(cred.Password))
	cred.Password = hex.EncodeToString(password[:])
	if queryUser.Password != cred.Password {
		msg := shared.GenerateResponseMessage("credentials not correct")
		w.WriteHeader(http.StatusUnauthorized)
		w.Write(msg)
		return
	}

	tokenStruct, err := TokenCreate(queryUser)
	if err != nil {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("could not generate jwt %s ", err))
		w.WriteHeader(http.StatusInternalServerError)
		w.Write(msg)
		return
	}
	tokenJson, err := json.Marshal(tokenStruct)
	log.Printf("user: %s logged in with id: %s", queryUser.Email, queryUser.UID)
	w.WriteHeader(http.StatusOK)
	w.Write(tokenJson)
}

func UserRefresh(w http.ResponseWriter, r *http.Request, ps httprouter.Params)  {
	w.Header().Set("Content-Type", "application/json")
	reqToken := r.Header.Get("Authorization")
	if reqToken == "" {
		msg := shared.GenerateResponseMessage(fmt.Sprintf("no authorization header provided "))
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}
	claims := &shared.Claims{}
	currentToken, err := jwt.ParseWithClaims(reqToken, claims, func(token *jwt.Token) (interface{}, error) {
		return shared.VerifyKey, nil
	})

	switch err.(type) {
	case nil:
		if !currentToken.Valid {
			msg := shared.GenerateResponseMessage("current token not valid, get a new one")
			w.WriteHeader(http.StatusUnauthorized)
			w.Write(msg)
			return
		}

	case *jwt.ValidationError:
		vErr := err.(*jwt.ValidationError)
		switch vErr.Errors {
		case jwt.ValidationErrorExpired:
			msg := shared.GenerateResponseMessage("token expired, get a new one")
			w.WriteHeader(http.StatusUnauthorized)
			w.Write(msg)
			return
		default:
			msg := shared.GenerateResponseMessage(fmt.Sprintf("error while parsing token!, err: %+v", vErr.Errors))
			w.WriteHeader(http.StatusInternalServerError)
			log.Printf("validationError error: %+v\n", vErr.Errors)
			w.Write(msg)
			return
		}

	default:
		msg := shared.GenerateResponseMessage(fmt.Sprintf("error while parsing token!, err: %+v", err))
		w.WriteHeader(http.StatusInternalServerError)
		log.Printf("token parse error: %v\n", err)
		w.Write(msg)
		return
	}

	if time.Unix(claims.ExpiresAt, 0).Sub(time.Now()) > 9 * time.Minute {
		msg := shared.GenerateResponseMessage("too early to regenerate token, try again later")
		w.WriteHeader(http.StatusBadRequest)
		w.Write(msg)
		return
	}

	expirationTime := time.Now().Add(10 * time.Minute)
	claims.ExpiresAt = expirationTime.Unix()
	token := jwt.NewWithClaims(jwt.SigningMethodRS256, claims)
	tokenString, err := token.SignedString(shared.SignKey)
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		return
	}
	tokenStruct := shared.Token{Token:tokenString}
	userJson, err := json.Marshal(tokenStruct)
	log.Printf("token refresh for user %s and id: %s", claims.Email, claims.Id)
	w.WriteHeader(http.StatusOK)
	w.Write(userJson)
}

func TokenCreate(queryUser shared.User) (shared.Token, error) {
	// set expiration time from variable
	expirationTime := time.Now().Add(10 * time.Minute)
	claims := &shared.Claims{
		Email: queryUser.Email,
		UserId: queryUser.UID,
		FirstName: queryUser.FirstName,
		LastName: queryUser.LastName,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: expirationTime.Unix(),
		},
	}
	token := jwt.NewWithClaims(jwt.SigningMethodRS256, claims)
	tokenString, err := token.SignedString(shared.SignKey)
	tokenStruct := shared.Token{Token: tokenString}
	return tokenStruct, err
}
