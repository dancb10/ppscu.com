package shared

import "os"

var DATABASE_DIALECT = os.Getenv("DATABASE_DIALECT")
var DATABASE_HOST = os.Getenv("DATABASE_HOST")
//var DATABASE_PORT = os.Getenv("DATABASE_PORT")
var DATABASE_DB = os.Getenv("DATABASE_DB")
var DATABASE_USERNAME = os.Getenv("DATABASE_USERNAME")
var DATABASE_PASSWORD = os.Getenv("DATABASE_PASSWORD")

var RSA_PRIVATE_KEY = os.Getenv("RSA_PRIVATE_KEY")
var RSA_PUBLIC_KEY = os.Getenv("RSA_PUBLIC_KEY")


var CASSANDRA_HOST = os.Getenv("CASSANDRA_HOST")
var CASSANDRA_KEYSPACE = os.Getenv("CASSANDRA_KEYSPACE")
