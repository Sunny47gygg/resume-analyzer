from skill import SKILL_SET

def extract_skills(text):
    text = text.lower()
    found = set()

    for skill in SKILL_SET:
        if skill in text:
            found.add(skill)

    return found