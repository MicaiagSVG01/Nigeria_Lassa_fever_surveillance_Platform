from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="Nigeria Disease Surveillance",
    page_icon="🦠",
    layout="wide"
)


# ---------------------------------------------------
# FILE PATHS
# ---------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

STATE_DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "lassa_surveillance_2026.csv"
)

WEEKLY_DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "lassa_weekly_national_2026.csv"
)


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
state_df = pd.read_csv(STATE_DATA_PATH)
weekly_df = pd.read_csv(WEEKLY_DATA_PATH)


# ---------------------------------------------------
# APP HEADER
# ---------------------------------------------------
st.title("Nigeria Infectious Disease Surveillance Dashboard")

st.caption(
    "Interactive surveillance dashboard using publicly available "
    "Nigeria Centre for Disease Control and Prevention data."
)


# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------
st.sidebar.header("Surveillance Filters")

disease_options = sorted(
    weekly_df["disease"].dropna().unique()
)

selected_disease = st.sidebar.selectbox(
    "Disease",
    disease_options
)

year_options = sorted(
    weekly_df["year"].dropna().unique(),
    reverse=True
)

selected_year = st.sidebar.selectbox(
    "Year",
    year_options
)

week_options = sorted(
    weekly_df[
        (weekly_df["disease"] == selected_disease)
        & (weekly_df["year"] == selected_year)
    ]["epi_week"].unique(),
    reverse=True
)

selected_week = st.sidebar.selectbox(
    "Epidemiological Week",
    week_options
)

state_options = ["All States"] + sorted(
    state_df["state"].dropna().unique().tolist()
)

selected_state = st.sidebar.selectbox(
    "State",
    state_options
)

metric_options = {
    "Confirmed Cases": "cumulative_confirmed",
    "Suspected Cases": "cumulative_suspected",
    "Deaths": "cumulative_deaths",
    "Case Fatality Rate": "cumulative_cfr",
}

selected_metric_label = st.sidebar.selectbox(
    "State Ranking Metric",
    list(metric_options.keys())
)

selected_metric = metric_options[selected_metric_label]

top_n = st.sidebar.slider(
    "Number of states to display",
    min_value=5,
    max_value=20,
    value=10
)


# ---------------------------------------------------
# FILTER DATA
# ---------------------------------------------------
filtered_weekly = weekly_df[
    (weekly_df["disease"] == selected_disease)
    & (weekly_df["year"] == selected_year)
].copy()

latest_row = filtered_weekly[
    filtered_weekly["epi_week"] == selected_week
].iloc[0]

filtered_state = state_df[
    (state_df["disease"] == selected_disease)
    & (state_df["year"] == selected_year)
].copy()

if selected_state != "All States":
    filtered_state = filtered_state[
        filtered_state["state"] == selected_state
    ]


# ---------------------------------------------------
# KPI VALUES
# ---------------------------------------------------
confirmed_cases = int(
    latest_row["confirmed_cases"]
)

deaths = int(
    latest_row["deaths"]
)

weekly_cfr = float(
    latest_row["weekly_cfr"]
)

states_affected = int(
    latest_row["states_affected"]
)


# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------
st.subheader(
    f"{selected_disease} — Epi Week {selected_week}, {selected_year}"
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Confirmed Cases",
    confirmed_cases
)

col2.metric(
    "Deaths",
    deaths
)

col3.metric(
    "Weekly CFR",
    f"{weekly_cfr:.1f}%"
)

col4.metric(
    "States Affected",
    states_affected
)


# ---------------------------------------------------
# WEEKLY TREND
# ---------------------------------------------------
st.subheader("Weekly Confirmed Cases")

fig_weekly = px.line(
    filtered_weekly,
    x="epi_week",
    y="confirmed_cases",
    markers=True,
    labels={
        "epi_week": "Epidemiological Week",
        "confirmed_cases": "Confirmed Cases"
    }
)

fig_weekly.update_layout(
    xaxis=dict(dtick=1)
)

st.plotly_chart(
    fig_weekly,
    use_container_width=True
)


# ---------------------------------------------------
# SUSPECTED CASE TREND
# ---------------------------------------------------
st.subheader("Weekly Suspected Cases")

fig_suspected = px.line(
    filtered_weekly,
    x="epi_week",
    y="suspected_cases",
    markers=True,
    labels={
        "epi_week": "Epidemiological Week",
        "suspected_cases": "Suspected Cases"
    }
)

fig_suspected.update_layout(
    xaxis=dict(dtick=1)
)

st.plotly_chart(
    fig_suspected,
    use_container_width=True
)


# ---------------------------------------------------
# STATE RANKING
# ---------------------------------------------------
st.subheader(
    f"Top States by {selected_metric_label}"
)

ranking_df = (
    filtered_state
    .sort_values(
        selected_metric,
        ascending=False
    )
    .head(top_n)
)

fig_states = px.bar(
    ranking_df,
    x="state",
    y=selected_metric,
    labels={
        "state": "State",
        selected_metric: selected_metric_label
    }
)

st.plotly_chart(
    fig_states,
    use_container_width=True
)


# ---------------------------------------------------
# CFR ANALYSIS
# ---------------------------------------------------
st.subheader("Case Fatality Rate by State")

min_cases = st.slider(
    "Minimum confirmed cases for CFR comparison",
    min_value=1,
    max_value=50,
    value=10
)

cfr_df = state_df[
    (
        state_df["disease"] == selected_disease
    )
    & (
        state_df["year"] == selected_year
    )
    & (
        state_df["cumulative_confirmed"] >= min_cases
    )
].copy()

cfr_df = cfr_df.sort_values(
    "cumulative_cfr",
    ascending=False
)

fig_cfr = px.bar(
    cfr_df,
    x="state",
    y="cumulative_cfr",
    labels={
        "state": "State",
        "cumulative_cfr": "CFR (%)"
    }
)

st.plotly_chart(
    fig_cfr,
    use_container_width=True
)


# ---------------------------------------------------
# DATA TABLE
# ---------------------------------------------------
st.subheader("Surveillance Data")

st.dataframe(
    filtered_state,
    use_container_width=True
)


# ---------------------------------------------------
# DOWNLOAD
# ---------------------------------------------------
csv_data = filtered_state.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Filtered Surveillance Data",
    data=csv_data,
    file_name="nigeria_surveillance_data.csv",
    mime="text/csv"
)


# ---------------------------------------------------
# SOURCE NOTE
# ---------------------------------------------------
st.divider()

st.caption(
    "Data source: Nigeria Centre for Disease Control and Prevention "
    "(NCDC) publicly available situation reports."
)