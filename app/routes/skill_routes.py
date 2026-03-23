from flask import Blueprint

from app.controllers.skill_controller import (
    create_skill,
    get_skill,
    list_skills,
    seed_dummy_skills,
    update_skill,
)

skill_bp = Blueprint("skill_bp", __name__)

skill_bp.add_url_rule("/create-skill", view_func=create_skill, methods=["POST"])
skill_bp.add_url_rule("/seed-skills", view_func=seed_dummy_skills, methods=["POST"])
skill_bp.add_url_rule("/skills", view_func=list_skills, methods=["GET"])
skill_bp.add_url_rule("/skills/<int:skill_id>", view_func=get_skill, methods=["GET"])
skill_bp.add_url_rule("/skills/<int:skill_id>", view_func=update_skill, methods=["PUT"])
# Removed the delete endpoint
