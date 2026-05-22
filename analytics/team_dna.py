import pandas as pd
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

    toss_wins = len(
        team_matches[
            team_matches["toss_winner"] == team_name
        ]
    )

    win_rate = round((wins / total_matches) * 100, 2)

    toss_dependency = round(
        (toss_wins / total_matches) * 100,
        2
    )

    if win_rate > 55:
        profile = "Dominant Competitive Team"
    elif win_rate > 48:
        profile = "Balanced Tactical Team"
    else:
        profile = "Unstable Performance Team"

    if toss_dependency > 60:
        toss_profile = "High Toss Dependency"
    else:
        toss_profile = "Low Toss Dependency"

    return {
        "team": team_name,
        "matches": total_matches,
        "wins": wins,
        "win_rate": win_rate,
        "profile": profile,
        "toss_dependency": toss_profile
    }


if __name__ == "__main__":

    team = "Mumbai Indians"

    dna = generate_team_dna(team)

    print("\nTEAM DNA REPORT\n")

    for key, value in dna.items():
        print(f"{key}: {value}")