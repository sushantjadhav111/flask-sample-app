from flask import Blueprint

from app.controllers.skill_controller import (
    create_skill,
    delete_skill,
    get_skill,
    list_skills,
    update_skill,
)

skill_bp = Blueprint("skill_bp", __name__)

skill_bp.add_url_rule("/create-skill", view_func=create_skill, methods=["POST"])
skill_bp.add_url_rule("/skills", view_func=list_skills, methods=["GET"])
skill_bp.add_url_rule("/skills/<int:skill_id>", view_func=get_skill, methods=["GET"])
skill_bp.add_url_rule("/skills/<int:skill_id>", view_func=update_skill, methods=["PUT"])
skill_bp.add_url_rule("/skills/<int:skill_id>", view_func=delete_skill, methods=["DELETE"])
