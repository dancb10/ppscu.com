import os
basedir = os.path.abspath(os.path.dirname(__file__))

#Database Config
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://flaskadmin:flaskadmin@localhost/flaskapi"

#Token secret key
TOKEN_SECRET_KEY = "TaseRalucaElena"
TOKEN_MAX_AGE = 6000

#Encryption key
ENCRYPTION_KEY = "/I02fMuSSvnouuu+/vyyD7NuSEVDB/0gte/z50dM0b4="

