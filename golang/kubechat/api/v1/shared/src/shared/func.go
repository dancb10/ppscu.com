package shared

import (
	"encoding/json"
)

func GenerateResponseMessage(s string) []byte {
	msg := ResponseMessage{s}
	msgJson, _ := json.Marshal(msg)
	return msgJson
}

func CheckLabelLength(labels []string, labelLength int) bool {
	for _, value := range labels {
		if len(value) > labelLength {
			return false
		}
	}
	return true
}

func CheckRoleType(role string,roleList []string) bool {
	for _, value := range roleList {
		if value == role {
			return true
		}
	}
	return false
}