from flask import jsonify, request

from app.models.skill_model import SkillStore


def create_skill():
    payload = request.get_json(silent=True) or {}
    name = str(payload.get("name", "")).strip()
    description = str(payload.get("description", "")).strip()

    if not name:
        return jsonify({"error": "Field 'name' is required."}), 400

    skill = SkillStore.create_skill(name=name, description=description)
    return jsonify({"message": "Skill created successfully.", "skill": skill}), 201


def list_skills():
    skills = SkillStore.get_all_skills()
    return jsonify({"count": len(skills), "skills": skills}), 200


def seed_dummy_skills():
    created_skills = SkillStore.seed_dummy_skills()
    if not created_skills:
        skills = SkillStore.get_all_skills()
        return (
            jsonify(
                {
                    "message": "Dummy skills already exist.",
                    "count": len(skills),
                    "skills": skills,
                }
            ),
            200,
        )

    return (
        jsonify(
            {
                "message": "Dummy skills created successfully.",
                "count": len(created_skills),
                "skills": created_skills,
            }
        ),
        201,
    )


def get_skill(skill_id):
    skill = SkillStore.get_skill_by_id(skill_id)
    if not skill:
        return jsonify({"error": "Skill not found."}), 404

    return jsonify({"skill": skill}), 200


def update_skill(skill_id):
    payload = request.get_json(silent=True) or {}
    name = payload.get("name")
    description = payload.get("description")

    if name is not None and not str(name).strip():
        return jsonify({"error": "Field 'name' cannot be empty."}), 400

    updated_skill = SkillStore.update_skill(
        skill_id=skill_id,
        name=str(name).strip() if name is not None else None,
        description=str(description).strip() if description is not None else None,
    )

    if not updated_skill:
        return jsonify({"error": "Skill not found."}), 404

    return jsonify({"message": "Skill updated successfully.", "skill": updated_skill}), 200


def delete_skill(skill_id):
    deleted_skill = SkillStore.delete_skill(skill_id)
    if not deleted_skill:
        return jsonify({"error": "Skill not found."}), 404

    return jsonify({"message": "Skill deleted successfully.", "skill": deleted_skill}), 200
