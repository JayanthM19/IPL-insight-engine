import pandas as pd
import logging
from ingest import load_match_files
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def extract_match_data(match):
    try:
        info = match.get("info", {})

        teams = info.get("teams", [])

        outcome = info.get("outcome", {})
        winner = outcome.get("winner", "No Result")

        toss = info.get("toss", {})
        toss_winner = toss.get("winner", "Unknown")
        toss_decision = toss.get("decision", "Unknown")

        return {
            "season": info.get("season", "Unknown"),
            "city": info.get("city", "Unknown"),
            "venue": info.get("venue", "Unknown"),
            "date": info.get("dates", ["Unknown"])[0],
            "team1": teams[0] if len(teams) > 0 else "Unknown",
            "team2": teams[1] if len(teams) > 1 else "Unknown",
            "winner": winner,
            "toss_winner": toss_winner,
            "toss_decision": toss_decision
        }

    except Exception as e:
        logging.error(f"Transformation failed: {e}")
        return None


def build_matches_dataframe():
    raw_matches = load_match_files()

    processed_matches = []
    skipped_matches = 0

    for match in raw_matches:
        transformed = extract_match_data(match)

        if transformed:
            processed_matches.append(transformed)
        else:
            skipped_matches += 1

    df = pd.DataFrame(processed_matches)

    logging.info(f"Processed matches: {len(df)}")
    logging.info(f"Skipped matches: {skipped_matches}")

    return df


if __name__ == "__main__":
    df = build_matches_dataframe()

    print(df.head())

    BASE_DIR = Path(__file__).resolve().parent.parent

    output_path = BASE_DIR / "data" / "processed" / "matches.csv"

    df.to_csv(output_path, index=False)

    print("Processed dataset saved.")