from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

@api.route("/")
def get_data():
    return jsonify({
        "message": "Hello from Flask API 🚀",
        "status": "success"
    })