# IPL Insight Engine Architecture

```text
                +----------------------+
                |  Cricsheet IPL JSON  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Ingestion Pipeline  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Validation Layer     |
                | - Missing fields     |
                | - Fault handling     |
                | - Safe parsing       |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Transformation Layer |
                | - Structured dataset |
                | - Metadata extraction|
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Processed CSV Store  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Analytics Engine     |
                | - Team DNA           |
                | - Pressure Meter     |
                | - Venue Intelligence |
                | - Match Story AI     |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Streamlit Dashboard  |
                | - Plotly Charts      |
                | - Heatmaps           |
                | - Radar Visuals      |
                | - AI Insight Panels  |
                +----------------------+
```