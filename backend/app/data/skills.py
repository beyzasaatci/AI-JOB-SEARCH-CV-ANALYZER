SKILL_MAP = {
    "js": "JavaScript",
    "javascript": "JavaScript",
    "reactjs": "React",
    "react.js": "React",
    "react": "React",
    "py": "Python",
    "python": "Python",
    "cpp": "C++",
    "c++": "C++",
    "nodejs": "Node.js",
    "node": "Node.js",
}


def normalize_skill(skill: str):
    return SKILL_MAP.get(skill.lower().strip(), skill)