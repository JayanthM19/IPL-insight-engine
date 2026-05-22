import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "matches.csv"


df = pd.read_csv(DATA_PATH)


def overall_team_win_rates():
    wins = df["winner"].value_counts().reset_index()

    wins.columns = ["team", "wins"]

    total_matches = pd.concat(
        [df["team1"], df["team2"]]
    ).value_counts().reset_index()

    total_matches.columns = ["team", "matches"]

    merged = pd.merge(wins, total_matches, on="team")

    merged["win_rate"] = (
        merged["wins"] / merged["matches"] * 100
    ).round(2)

    return merged.sort_values(
        by="win_rate",
        ascending=False
    )


def toss_impact_analysis():
    toss_win_match_win = df[
        df["toss_winner"] == df["winner"]
    ]

    percentage = (
        len(toss_win_match_win) / len(df)
    ) * 100

    return round(percentage, 2)


def venue_win_patterns():
    venue_stats = df.groupby("venue")["winner"] \
        .value_counts() \
        .reset_index(name="wins")

    return venue_stats.sort_values(
        by="wins",
        ascending=False
    )


if __name__ == "__main__":

    print("\nOVERALL TEAM WIN RATES\n")
    print(overall_team_win_rates().head())

    print("\nTOSS IMPACT\n")
    print(
        f"{toss_impact_analysis()}% matches won after winning toss"
    )

    print("\nVENUE PATTERNS\n")
    print(venue_win_patterns().head())