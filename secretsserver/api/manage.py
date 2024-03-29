from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db
from run import run_application

app = run_application('config')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
