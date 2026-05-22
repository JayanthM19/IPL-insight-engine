import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_DIR))
import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

from analytics.team_analysis import (
    overall_team_win_rates,
    toss_impact_analysis,
    venue_win_patterns
)

from analytics.team_dna import generate_team_dna


st.set_page_config(
    page_title="IPL Insight Engine",
    page_icon="🏏",
    layout="wide"
)


# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: #F8F9FA;
}

.metric-card {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 0px 10px rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# TITLE
# -----------------------------

st.title("🏏 IPL Insight Engine")

st.markdown("""
AI-Powered Cricket Intelligence Platform  
Built with fault-tolerant pipelines and advanced analytics.
""")


# -----------------------------
# LOAD DATA
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "matches.csv"

df = pd.read_csv(DATA_PATH)


# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go To",
    [
        "Overview",
        "Team Analytics",
        "Venue Insights",
        "Team DNA"
    ]
)


# -----------------------------
# OVERVIEW
# -----------------------------

if section == "Overview":

    st.header("Tournament Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Matches", len(df))

    with col2:
        st.metric(
            "Total Teams",
            len(
                pd.concat([df["team1"], df["team2"]]).unique()
            )
        )

    with col3:
        st.metric(
            "Toss Impact %",
            toss_impact_analysis()
        )

    st.divider()

    win_rates = overall_team_win_rates()

    fig = px.bar(
        win_rates.head(10),
        x="team",
        y="win_rate",
        color="win_rate",
        title="Top Team Win Rates"
    )

    st.plotly_chart(fig, use_container_width=True)


# -----------------------------
# TEAM ANALYTICS
# -----------------------------

elif section == "Team Analytics":

    st.header("Team Performance Analytics")

    win_rates = overall_team_win_rates()

    fig = px.bar(
        win_rates,
        x="team",
        y="wins",
        color="win_rate",
        hover_data=["matches"],
        title="Team Wins Analysis"
    )

    st.plotly_chart(fig, use_container_width=True)


# -----------------------------
# VENUE INSIGHTS
# -----------------------------

elif section == "Venue Insights":

    st.header("Venue Intelligence")

    venue_data = venue_win_patterns()

    fig = px.bar(
        venue_data.head(20),
        x="venue",
        y="wins",
        color="wins",
        title="Venue Winning Trends"
    )

    st.plotly_chart(fig, use_container_width=True)


# -----------------------------
# TEAM DNA
# -----------------------------

elif section == "Team DNA":

    st.header("Team DNA Engine")

    teams = sorted(
        pd.concat([df["team1"], df["team2"]]).unique()
    )

    selected_team = st.selectbox(
        "Select Team",
        teams
    )

    dna = generate_team_dna(selected_team)

    st.subheader(f"{selected_team} DNA Profile")

    st.json(dna)