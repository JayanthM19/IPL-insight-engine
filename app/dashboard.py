
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_DIR))
import plotly.graph_objects as go
import sys
from pathlib import Path
from analytics.pressure_meter import pressure_score

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

.stApp {
    background-color: #0B0F19;
    color: white;
}

h1, h2, h3 {
    color: #F8FAFC;
    font-weight: 700;
}

.metric-card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    border-radius: 18px;
    padding: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

.insight-box {
    background: linear-gradient(
        135deg,
        rgba(0,255,200,0.08),
        rgba(0,120,255,0.08)
    );

    padding: 18px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-top: 10px;
}

.sidebar .sidebar-content {
    background-color: #111827;
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
        "Pressure Meter",
        "Team DNA"
    ]
)


# -----------------------------
# OVERVIEW
# -----------------------------

if section == "Overview":
    st.markdown("## AI Match Intelligence")

    st.markdown("""
    <div class="insight-box">

    ### Strategic Observation

    Teams winning the toss and choosing to field
    show significantly stronger win percentages
    across high-scoring venues.

    Death-over acceleration appears strongly
    correlated with successful chases.

    </div>
    """, unsafe_allow_html=True)


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
    metrics = dna["metrics"]

    categories = list(metrics.keys())
    values = list(metrics.values())

    categories.append(categories[0])
    values.append(values[0])

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=selected_team
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False,
        template="plotly_dark",
        title="Team Strategy Fingerprint"
    )

    st.plotly_chart(fig, use_container_width=True)

elif section == "Pressure Meter":

    st.header("Player Pressure Analytics")

    player = st.text_input(
        "Enter Player Name",
        "Virat Kohli"
    )

    result = pressure_score(player)

    score = result["pressure_score"]

    st.metric(
        "Pressure Score",
        f"{score}/10"
    )

    st.markdown(f"""
    <div class="insight-box">

    ### Pressure Profile

    {result["profile"]}

    This player demonstrates strong adaptability
    during high-pressure chase situations and
    maintains stable scoring patterns.

    </div>
    """, unsafe_allow_html=True)