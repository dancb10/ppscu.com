package shared

import (
	"time"
)

var rolesList = []string{"president", "affiliate","member"}


// POSTGRESQL STRUCTS
//
//type Community struct {
//	CID         string `gorm:"primary_key"`
//	CreatedAt   time.Time
//	UpdatedAt   time.Time
//	DeletedAt   *time.Time
//	Name   		string	 `json:"name" valid:"alphanum~ name: only alphanum characters allowed, optional, stringlength(1|30)~ name: 1 < characters < 30"`
//	Description string   `json:"description" valid:"ascii~ description: only ascii characters allowed, optional, stringlength(1|100)~ description: 1 < length < 100"`
//	Location 	string   `json:"location" valid:"alpha~ location: only alpha characters allowed, optional, stringlength(1|20)~ country: 1 < name < 20"`
//	Labels      pq.StringArray `gorm:"type:text[]" json:"labels" valid:"alphanum~ labels: only alphanum characters allowed, optional, length(1|10)~ labels: 1 < number < 10"`
//	Visibility     string 	 `json:"visibility" valid:"communityType~ communityType: public/closed/invite, optional"` // public, closed, invite
//	GroupCreation  string 	 `json:"groupCreation" valid:"groupCreation~groupCreation: anyone/admins/members, optional"` // anyone, admins, members
//}
//
//type CommunityUser struct {
//	CUID	string `gorm:"primary_key"`
//	CID		string
//	UID		string
//	Role	string
//	CreatedAt   time.Time
//	UpdatedAt   time.Time
//	DeletedAt   *time.Time
//}

type User struct {
	UID        	string	`gorm:"primary_key"`
	CreatedAt 	time.Time
	UpdatedAt 	time.Time
	DeletedAt 	*time.Time
	FirstName   string	`gorm:"not null" json:"firstname" valid:"alpha~ firstname: only alpha characters allowed, required, stringlength(1|30)~ firstname: 1 < characters < 30"`
	LastName	string	`gorm:"not null" json:"lastname" valid:"alpha~ lastname: only alpha characters allowed, required, stringlength(1|30)~ lastname: 1 < characters < 30"`
	Password	string	`gorm:"not null" json:"password" valid:"ascii~ password: only ascii characters allowed, required, stringlength(7|30)~ password: 7 < length < 30"`
	Email       string  `gorm:"not null" json:"email" valid:"email~wrong email format, required"`
}

type UserDetails struct {
	UID        	string 		`gorm:"primary_key" valid:"checkUUID~ group_id: only UUIDv4 type allowed, required"`
	Nickname	string		`json:"nickname" valid:"alphanum~ nickname: only alphanumeric characters allowed, optional, stringlength(1|30)~ nickname: 1 < characters < 30"`
	Gender	    string		`json:"gender" valid:"alpha~ gender: only alpha characters allowed, optional, stringlength(1|20)~ gender: 1 < characters < 20"` // validate
	Phone       int64   	`json:"phone" valid:"numeric~ phone: only numeric characters allowed, optional, range(6|20)~ phone: 6 < characters < 20"` // validate
	Age         int64   	`json:"age" valid:"numeric~ age: only numeric characters allowed, optional, range(18|150)~ age: 18 < years < 150"`
	Country     string		`json:"country" valid:"ISO3166Alpha2~ country: code of two letters wrong, optional, stringlength(2|2)~ country: 2 < name < 2"`
}

type UserCredentials struct {
	Password	string	`gorm:"not null" json:"password" valid:"ascii~ password: only ascii characters allowed, required, stringlength(7|30)~ password: 7 < length < 30"`
	Email       string  `gorm:"not null" json:"email" valid:"email~wrong email format, required"`
}

//type Replays struct {
//	RID 	 		string	`gorm:"primary_key"`
//	TID 	 		string
//	UID 	 		string
//	CreatedAt 	time.Time
//	UpdatedAt 	time.Time
//	DeletedAt 	*time.Time
//	Name 			string	`gorm:"name"`
//	Content	    	string	`gorm:"content"`
//	Attachments	    string	`gorm:"attachments"`
//	Likes			int64	`gorm:"likes"`
//}

// CASSANDRA STRUCTS

type Group struct {
	GroupId   	   string
	CommunityId    string	`json:"community_id" valid:"checkUUID~ group_id: only UUIDv4 type allowed, required"`
	CreateDate 	   time.Time
	Day		       string	`valid:"checkDay~ day: only YYYY-MM-DD type allowed, required"`
	Description    string	`json:"description" valid:"ascii~ description: only ascii characters allowed, required, stringlength(1|500)~ name: 1 < summary < 500"`
	Labels         []string	`json:"labels" valid:"alphanum~ labels: only alphanum characters allowed, required, length(1|20)~ labels: 1 < number < 20"`
	Name       	   string 	`json:"name" valid:"ascii~ name: only ascii characters allowed, required, stringlength(1|100)~ name: 1 < characters < 100"`
	Plabels        []string	`json:"plabels" valid:"alphanum~ plabels: only alphanum characters allowed, required, length(1|20)~ plabels: 1 < number < 20"`
	Type		   string	`json:"type" valid:"groupType~ groupType: democratic/totalitarian/semi-democratic/full-totalitarian, required"` // democratic / totalitarian / semi-democratic / full-totalitarian
	UpdateDate	   time.Time
	Visibility     string 	`json:"visibility" valid:"groupVisibility~ groupVisibility: public/closed/invite, required"` // public, closed, invite
}
// Plabels MUST never change from parent
type GroupUpdate struct {
	GroupId   	   string	`json:"group_id" valid:"checkUUID~ group_id: only UUIDv4 type allowed, required"`
	CommunityId    string	`json:"community_id" valid:"checkUUID~ community_id: only UUIDv4 type allowed, required"`
	CreateDate 	   time.Time
	Description    string	`json:"description" valid:"ascii~ description: only ascii characters allowed, required, stringlength(1|500)~ name: 1 < summary < 500"`
	Labels         []string	`json:"labels" valid:"alphanum~ labels: only alphanum characters allowed, required, length(1|20)~ labels: 1 < number < 20"`
	Name       	   string 	`json:"name" valid:"ascii~ name: only ascii characters allowed, required, stringlength(1|100)~ name: 1 < characters < 100"`
	Type		   string	`json:"type" valid:"groupType~ groupType: democratic/totalitarian/semi-democratic/full-totalitarian, required"` // democratic / totalitarian / semi-democratic / full-totalitarian
	UpdateDate	   time.Time
	Visibility     string 	`json:"visibility" valid:"groupVisibility~ groupVisibility: public/closed/invite, required"` // public, closed, invite
}

type GroupGet struct {
	GroupId   	   string 	`json:"group_id" valid:"checkUUID~ group_id: only UUIDv4 type allowed, required"`
	CommunityId    string	`json:"community_id" valid:"checkUUID~ community_id: only UUIDv4 type allowed, required"`
}

type GroupGetByCommunityCreateDate struct {
	CommunityId    string	`json:"community_id" valid:"checkUUID~ community_id: only UUIDv4 type allowed, required"`
	Day		   	   string	`json:"day" valid:"checkDay~ day: only YYYY-MM-DD type allowed, required"`
}

type GroupsByCommunityTypeSelect struct {
	CommunityId    string	`json:"community_id" valid:"checkUUID~ community_id: only UUIDv4 type allowed, required"`
	Type		   string	`json:"type" valid:"groupType~ groupType: democratic/totalitarian/semi-democratic/full-totalitarian, required"` // democratic / totalitarian / semi-democratic / full-totalitarian
}

type GroupsByCommunityVisibilitySelect struct {
	CommunityId    string	`json:"community_id" valid:"checkUUID~ community_id: only UUIDv4 type allowed, required"`
	Visibility     string 	`json:"visibility" valid:"groupVisibility~ groupVisibility: public/closed/invite, required"` // public, closed, invite
}

//type GroupUser struct {
//	GUID	string `gorm:"primary_key"`
//	GID		string
//	UID		string
//	Role	string
//	CreatedAt   time.Time
//	UpdatedAt   time.Time
//	DeletedAt   *time.Time
//}

type Thread struct {
	ThreadId   string
	CreateDate time.Time
	Day		   string		`valid:"checkDay~ day: only YYYY-MM-DD type allowed, required"`
	GroupId    string		`json:"group_id" valid:"checkUUID~ group_id: only UUIDv4 type allowed, required"`
	UserId    string
	UpdateDate time.Time
	Name       string 		`json:"name" valid:"ascii~ name: only ascii characters allowed, required, stringlength(1|100)~ name: 1 < characters < 100"`
	Summary    string		`json:"summary" valid:"ascii~ summary: only ascii characters allowed, required, stringlength(1|500)~ name: 1 < summary < 500"`
	Content    string		`json:"content" valid:"ascii~ content: only ascii characters allowed, required, stringlength(1|50000)~ content: 1 < characters < 50000"`
	Labels     []string		`json:"labels" valid:"alphanum~ labels: only alphanum characters allowed, required, length(1|20)~ labels: 1 < number < 20"`
	Plabels    []string		`json:"plabels" valid:"alphanum~ plabels: only alphanum characters allowed, required, length(1|20)~ plabels: 1 < number < 20"`
}

type ThreadGet struct {
	ThreadId   string 	`json:"thread_id" valid:"checkUUID~ thread_id: only UUIDv4 type allowed, required"`
	GroupId    string	`json:"group_id" valid:"checkUUID~ group_id: only UUIDv4 type allowed, required"`
}

type ThreadVote struct {
	ThreadId	string 	`json:"thread_id" valid:"checkUUID~ thread_id: only UUIDv4 type allowed, required"`
	UserId		string 	`valid:"checkUUID~ user_id: only UUIDv4 type allowed, required"`
	Day		    string	`valid:"checkDay~ day: only YYYY-MM-DD type allowed, required"`
	Email       string  `valid:"email~wrong email format"`
	FirstName   string	`valid:"alpha~ firstname: only alpha characters allowed, optional, stringlength(1|30)~ firstname: 1 < characters < 30"`
	LastName	string	`valid:"alpha~ lastname: only alpha characters allowed, optional, stringlength(1|30)~ lastname: 1 < characters < 30"`
	Nickname	string	`valid:"alphanum~ nickname: only alphanumeric characters allowed, optional, stringlength(1|30)~ nickname: 1 < characters < 30"`
	VoteDate	time.Time
}

type ThreadVotesGet struct {
	ThreadId   string 	`json:"thread_id" valid:"checkUUID~ thread_id: only UUIDv4 type allowed, required"`
	Day		   string	`json:"day" valid:"checkDay~ day: only YYYY-MM-DD type allowed, required"`
}

type ThreadGetByGroupCreateDate struct {
	GroupId    string		`json:"group_id" valid:"checkUUID~ group_id: only UUIDv4 type allowed, required"`
	Day		   string		`json:"day" valid:"checkDay~ day: only YYYY-MM-DD type allowed, required"`
}

// COMMON STRUCTS

type ResponseMessage struct {
	Msg	string
}

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