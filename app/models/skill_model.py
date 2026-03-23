import json
from datetime import datetime, UTC
from pathlib import Path


class SkillStore:
    _data_file = None
    _default_skills = [
        {
            "name": "AI Assistant",
            "description": "Helps users with general tasks and answers questions.",
        },
        {
            "name": "Content Writer",
            "description": "Creates blog drafts, captions, and marketing copy.",
        },
        {
            "name": "Code Reviewer",
            "description": "Reviews pull requests and suggests improvements.",
        },
        {
            "name": "Data Analyst",
            "description": "Summarizes datasets and highlights useful trends.",
        },
    ]

    @classmethod
    def configure(cls, data_file):
        cls._data_file = Path(data_file)
        cls._data_file.parent.mkdir(parents=True, exist_ok=True)

        if not cls._data_file.exists():
            cls._write_skills([])

    @classmethod
    def _read_skills(cls):
        if cls._data_file is None:
            raise RuntimeError("SkillStore is not configured.")

        if not cls._data_file.exists():
            return []

        try:
            return json.loads(cls._data_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            cls._write_skills([])
            return []

    @classmethod
    def _write_skills(cls, skills):
        if cls._data_file is None:
            raise RuntimeError("SkillStore is not configured.")

        cls._data_file.write_text(
            json.dumps(skills, indent=2),
            encoding="utf-8",
        )

    @classmethod
    def _next_id(cls, skills):
        if not skills:
            return 1
        return max(skill["id"] for skill in skills) + 1

    @classmethod
    def create_skill(cls, name, description):
        skills = cls._read_skills()
        skill = {
            "id": cls._next_id(skills),
            "name": name,
            "description": description,
            "created_at": datetime.now(UTC).isoformat(),
        }
        skills.append(skill)
        cls._write_skills(skills)
        return skill

    @classmethod
    def get_all_skills(cls):
        return cls._read_skills()

    @classmethod
    def seed_dummy_skills(cls):
        skills = cls._read_skills()
        if skills:
            return []

        created_skills = []
        for default_skill in cls._default_skills:
            skill = {
                "id": cls._next_id(skills),
                "name": default_skill["name"],
                "description": default_skill["description"],
                "created_at": datetime.now(UTC).isoformat(),
            }
            skills.append(skill)
            created_skills.append(skill)

        cls._write_skills(skills)
        return created_skills

    @classmethod
    def get_skill_by_id(cls, skill_id):
        skills = cls._read_skills()
        return next((skill for skill in skills if skill["id"] == skill_id), None)

    @classmethod
    def update_skill(cls, skill_id, name=None, description=None):
        skills = cls._read_skills()
        skill = next((item for item in skills if item["id"] == skill_id), None)
        if not skill:
            return None

        if name is not None:
            skill["name"] = name
        if description is not None:
            skill["description"] = description

        skill["updated_at"] = datetime.now(UTC).isoformat()
        cls._write_skills(skills)
        return skill

    @classmethod
    def delete_skill(cls, skill_id):
        skills = cls._read_skills()
        skill = next((item for item in skills if item["id"] == skill_id), None)
        if not skill:
            return None

        cls._write_skills([item for item in skills if item["id"] != skill_id])
        return skill
