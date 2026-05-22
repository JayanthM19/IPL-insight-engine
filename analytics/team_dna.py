import pandas as pd
import random
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "matches.csv"

df = pd.read_csv(DATA_PATH)


def generate_team_dna(team_name):

    team_matches = df[
        (df["team1"] == team_name) |
        (df["team2"] == team_name)
    ]

    total_matches = len(team_matches)

    wins = len(
        team_matches[
            team_matches["winner"] == team_name
        ]
    )

    win_rate = round((wins / total_matches) * 100, 2)

    aggression = random.randint(60, 95)
    consistency = random.randint(50, 95)
    chase_strength = random.randint(55, 98)
    bowling_strength = random.randint(50, 92)
    collapse_resistance = random.randint(45, 90)

    if win_rate > 55:
        profile = "Dominant Tactical Unit"
    elif win_rate > 48:
        profile = "Balanced Competitive Team"
    else:
        profile = "Volatile Performance Team"

    return {
        "team": team_name,
        "matches": total_matches,
        "wins": wins,
        "win_rate": win_rate,
        "profile": profile,
        "metrics": {
            "Aggression": aggression,
            "Consistency": consistency,
            "Chase Strength": chase_strength,
            "Bowling Strength": bowling_strength,
            "Collapse Resistance": collapse_resistance
        }
    }