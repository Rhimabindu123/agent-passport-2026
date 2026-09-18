import json
from pathlib import Path


def load_passport():
    passport_path = Path(__file__).parent / "passport.json"

    with open(passport_path, "r", encoding="utf-8") as file:
        return json.load(file)