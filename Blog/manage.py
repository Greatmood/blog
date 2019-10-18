from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from blopApp.models import db
from blopApp import create_app

app = create_app()
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()