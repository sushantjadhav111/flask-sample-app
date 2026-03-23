from datetime import datetime, UTC


class SkillStore:
    _skills = []
    _next_id = 1

    @classmethod
    def create_skill(cls, name, description):
        skill = {
            "id": cls._next_id,
            "name": name,
            "description": description,
            "created_at": datetime.now(UTC).isoformat(),
        }
        cls._skills.append(skill)
        cls._next_id += 1
        return skill

    @classmethod
    def get_all_skills(cls):
        return cls._skills

    @classmethod
    def get_skill_by_id(cls, skill_id):
        return next((skill for skill in cls._skills if skill["id"] == skill_id), None)

    @classmethod
    def update_skill(cls, skill_id, name=None, description=None):
        skill = cls.get_skill_by_id(skill_id)
        if not skill:
            return None

        if name is not None:
            skill["name"] = name
        if description is not None:
            skill["description"] = description

        skill["updated_at"] = datetime.now(UTC).isoformat()
        return skill

    @classmethod
    def delete_skill(cls, skill_id):
        skill = cls.get_skill_by_id(skill_id)
        if not skill:
            return None

        cls._skills = [item for item in cls._skills if item["id"] != skill_id]
        return skill
