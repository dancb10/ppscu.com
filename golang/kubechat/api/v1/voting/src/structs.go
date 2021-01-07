package main

import "time"

type Votes struct {
	VID 	 		string	`json:"primary_key"`
	GID 	 		string
	UID 	 		string
	Name 				string	`json:"name"`
	Content	    		string	`json:"content"`
	Attachments	    	string	`json:"attachments"`
	Votes				int64	`json:"votes"`
	PercentageOfVoters	int64	`json:"percentageofvoters"`
	CreateDate		time.Time	`json:"createDate"`
	ExpiryDate		time.Time	`json:"expirydate"`
	Type			string		`json:"type"`
}
