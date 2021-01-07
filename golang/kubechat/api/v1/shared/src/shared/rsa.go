package shared

import (
	"crypto/rsa"
	"github.com/dgrijalva/jwt-go"
	"io/ioutil"
	"log"
)

var (
	VerifyKey *rsa.PublicKey
	SignKey   *rsa.PrivateKey
)

func GetPubKey() {
	verifyBytes, err := ioutil.ReadFile(RSA_PUBLIC_KEY)
	if err != nil {
		log.Fatal(err)
	}
	VerifyKey, err = jwt.ParseRSAPublicKeyFromPEM(verifyBytes)
	if err != nil {
		log.Fatal(err)
	}
}
func GetPrivKey() {
	signBytes, err := ioutil.ReadFile(RSA_PRIVATE_KEY)
	if err != nil {
		log.Fatal(err)
	}
	SignKey, err = jwt.ParseRSAPrivateKeyFromPEM(signBytes)
	if err != nil {
		log.Fatal(err)
	}
}