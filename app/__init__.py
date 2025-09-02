from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.secret_key = "supersecret"

    db.init_app(app)
    jwt.init_app(app)

    from app.routes.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app
