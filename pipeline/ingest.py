import json
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DATA_PATH = Path("data/raw/ipl_json")


def load_match_files():
    matches = []

    json_files = list(DATA_PATH.glob("*.json"))

    logging.info(f"Found {len(json_files)} match files")

    for file in json_files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            matches.append(data)

        except Exception as e:
            logging.error(f"Failed to load {file.name}: {e}")

    logging.info(f"Successfully loaded {len(matches)} matches")

    return matches


if __name__ == "__main__":
    data = load_match_files()

    print(f"Loaded {len(data)} matches")