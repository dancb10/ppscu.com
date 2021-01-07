import os

import yaml


class Config:
    def __init__(self):
        self.basedir = os.path.dirname(os.path.abspath(__file__))
        self.config_file = os.getenv('CONFIG_FILE', os.path.join(self.basedir, 'app.yaml'))
        self.config_data = self.get_data()
        self.DEBUG = False
        self.PORT = self.config_data['listen']['port']
        self.HOST = self.config_data['listen']['address']
        self.SERVICES = self.config_data['services']

        self.SQLALCHEMY_ECHO = False
        self.SQLALCHEMY_TRACK_MODIFICATIONS = True
        self.SQLALCHEMY_DATABASE_URI = "postgresql://admin:password@postgres/app"

        self.TOKEN_SECRET_KEY = 'keyusedfortokengeneration'
        self.TOKEN_MAX_AGE = 6000
        self.AUTH_ENABLED = self.config_data['auth']

    def get_data(self):
        with open(self.config_file) as f:
            data = yaml.safe_load(f)
        return data["proxy"]
