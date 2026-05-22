import random


def pressure_score(player_name):

    score = round(random.uniform(6.5, 9.8), 2)

    if score > 8.5:
        profile = "Elite Clutch Performer"
    elif score > 7.5:
        profile = "Reliable Under Pressure"
    else:
        profile = "Moderate Pressure Stability"

    return {
        "player": player_name,
        "pressure_score": score,
        "profile": profile
    }


if __name__ == "__main__":

    result = pressure_score("Virat Kohli")

    print("\nPRESSURE ANALYSIS\n")

    for key, value in result.items():
        print(f"{key}: {value}")