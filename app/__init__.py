from flask import Flask, jsonify

from config import Config
from app.routes.skill_routes import skill_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.get("/")
    def index():
        return jsonify(
            {
                "message": "Welcome to the Flask Skill API",
                "version": "1.0.0",
                "endpoints": {
                    "health": "/health",
                    "create_skill": "/create-skill",
                    "get_skills": "/skills",
                },
            }
        )

    @app.get("/health")
    def health():
        return jsonify(
            {
                "status": "ok",
                "app_name": app.config["APP_NAME"],
                "environment": app.config["FLASK_ENV"],
            }
        )

    app.register_blueprint(skill_bp)
    return app
