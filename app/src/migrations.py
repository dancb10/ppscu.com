from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import run_application
from config import Config
from models.models import db
import os

MIGRATIONS_DIR=os.environ['MIGRATIONS_DIR']

config = Config()
app = run_application(config)

migrate = Migrate(app, db, directory=MIGRATIONS_DIR)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
