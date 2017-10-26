from flask import Flask 
from flaskrouter import flaskrouter

import models

def create_app():
	app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:groupPassword@35.193.209.24/postgres'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        models.db.init_app(app)
        app.register_blueprint(flaskrouter)
	return app

if __name__ == "__main__":
    app = create_app()
    app.run()
