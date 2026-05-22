import random


stories = [
    "A dramatic middle-order collapse shifted momentum entirely during the second innings.",

    "Death-over acceleration created a decisive advantage in a high-scoring thriller.",

    "Bowling discipline during powerplay overs became the defining factor of the match.",

    "A strong chase under scoreboard pressure demonstrated exceptional batting composure.",

    "Strategic fielding and wicket timing heavily influenced the match outcome."
]


def generate_match_story():
    return random.choice(stories)