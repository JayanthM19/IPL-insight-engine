import random


summaries = [
    "This team demonstrates aggressive chase-oriented gameplay with strong death-over acceleration.",

    "The team relies heavily on bowling consistency and middle-over control to secure victories.",

    "Tactical toss decisions and stable batting partnerships define this team's success profile.",

    "The team exhibits high variance performance with explosive batting but inconsistent bowling execution.",

    "Balanced tactical adaptability across venues makes this team strategically resilient."
]


def generate_team_summary(team_name):

    summary = random.choice(summaries)

    return f"{team_name}: {summary}"