# IPL Insight Engine

AI-powered IPL analytics and cricket intelligence platform built using fault-tolerant data pipelines, interactive visualizations, and AI-assisted insights.

---

## Features

- Interactive IPL analytics dashboard
- Team win-rate analysis
- Toss impact intelligence
- Venue trend analysis
- Team DNA profiling
- Pressure meter analytics
- AI-generated match insights
- Match story engine
- Downloadable reports
- Fault-tolerant ETL pipeline

---

## Tech Stack

- Python
- Streamlit
- Plotly
- Pandas
- Pydantic
- DuckDB
- Pytest

---

## Project Structure

```text
ipl-insight-engine/
│
├── app/
├── analytics/
├── pipeline/
├── data/
├── outputs/
├── tests/
├── README.md
├── REPORT.md
└── requirements.txt
```

---

## Dataset

This project uses the IPL dataset from Cricsheet.

Download dataset from:

https://cricsheet.org/downloads/

Place extracted JSON files inside:

```text
data/raw/
```

---

## Installation

```bash
git clone <repo-url>

cd ipl-insight-engine

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## Run Pipeline

```bash
python pipeline/transform.py
```

---

## Run Dashboard

```bash
streamlit run app/dashboard.py
```

---

## Key Innovations

### Team DNA Engine
Generates strategic fingerprints for IPL teams using multi-dimensional performance indicators.

### Pressure Meter
Evaluates player adaptability under pressure scenarios.

### AI Match Story Engine
Transforms statistical insights into narrative match intelligence.

### Fault-Tolerant Pipeline
Gracefully handles incomplete and malformed match records.

---

## License

MIT License