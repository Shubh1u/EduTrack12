from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    jwt.init_app(app)

    from app.routes import auth, student, achievement, validation, portfolio
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(student.bp)
    app.register_blueprint(achievement.bp)
    app.register_blueprint(validation.bp)
    app.register_blueprint(portfolio.bp)

    return app
