package shared

import (
	"fmt"
	"github.com/gocql/gocql"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
	//"gopkg.in/yaml.v2"
	"log"
	"reflect"
)

//func ReadConfig(cfg *Config, fileName string) {
//	f, err := os.Open(fileName)
//	if err != nil {
//		log.Printf("error with file: %v ; error: %v", f.Name, err)
//	}
//
//	decoder := yaml.NewDecoder(f)
//	err = decoder.Decode(cfg)
//	if err != nil {
//		log.Fatal("Unmarshall: ", err)
//	}
//}

//func DatabaseConn() *gorm.DB {
//	if _, err := os.Stat("conf/auth.yaml"); os.IsNotExist(err) {
//		db := ConnectToDatabaseEnv()
//		return db
//	} else {
//		var cfg Config
//		ReadConfig(&cfg, "conf/auth.yaml")
//		db := ConnectToDatabaseCfg(&cfg)
//		return db
//	}
//}

func DatabaseConn() *gorm.DB {
	databaseUrl := fmt.Sprintf("host=%s user=%s password=%s dbname=%s sslmode=disable",
		DATABASE_HOST,
		DATABASE_USERNAME,
		DATABASE_PASSWORD,
		DATABASE_DB)

	db, err := gorm.Open(DATABASE_DIALECT, databaseUrl)
	if err != nil {
		log.Fatal("db err: ", err)
	}
	db.LogMode(true)
	return db
}

//func ConnectToDatabaseCfg(cfg *Config) *gorm.DB {
//	databaseUrl := fmt.Sprintf("host=%s user=%s password=%s dbname=%s sslmode=disable",
//		cfg.Database.Host,
//		cfg.Database.Username,
//		cfg.Database.Password,
//		cfg.Database.Db)
//	db, err := gorm.Open(cfg.Database.Dialect, databaseUrl)
//	if err != nil {
//		log.Fatal("db err: ", err)
//	}
//	db.LogMode(true)
//	return db
//}

func DbMigrate(m interface{}) {
	db := DatabaseConn()
	log.Printf("Migrating %s", reflect.TypeOf(m))
	migrate := db.AutoMigrate(m)
	if migrate != nil && db.Error != nil {
		log.Printf("could not perform migration, err: %s", db.Error)
	}
}

func DatabaseConnCassandra() *gocql.Session {
	cluster := gocql.NewCluster(CASSANDRA_HOST)
	cluster.Keyspace = CASSANDRA_KEYSPACE
	session, err := cluster.CreateSession()
	cluster.Consistency = gocql.Quorum
	if err != nil {
		panic(err)
	}
	fmt.Printf("cassandra connection established host: %s, keyspace: %s \n", CASSANDRA_HOST, CASSANDRA_KEYSPACE)
	return session
}