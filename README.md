# Nigeria_Lassa_fever_surveillance_Platform
Interactive infectious disease surveillance dashboard analyzing NCDC data to explore temporal trends, state-level disease burden, mortality, and case fatality patterns in Nigeria.
🌐 **Live Demo:** <img width="2559" height="1371" alt="image" src="https://github.com/user-attachments/assets/f096bdce-f92f-4f7f-afa7-0729fc77cf48" /> (https://nigerialassafeversurveillanceplatform-vycfshqusghc9xc7qcrqqe.streamlit.app/)
📊 **Current MVP:** Lassa Fever, 2026
STREAMLIT APP LINK: https://nigerialassafeversurveillanceplatform-vycfshqusghc9xc7qcrqqe.streamlit.app/

## Overview

The **Nigeria Infectious Disease Surveillance Dashboard** is a data-driven public health surveillance project designed to explore infectious disease patterns across Nigeria using publicly available surveillance reports from the **Nigeria Centre for Disease Control and Prevention (NCDC)**.

The long-term goal of the project is to develop a multi-disease surveillance platform capable of presenting temporal trends, geographic disease burden, mortality patterns, case fatality rates, and potential outbreak signals in an accessible and interactive format.

The current MVP focuses on **Lassa fever surveillance data for 2026**.

The MVP was built with Python, Pandas, Plotly, and Streamlit. A more advanced version is planned as a full web application with a modern frontend, database integration, interactive geographic visualisation, and more advanced surveillance analytics.

---

# Project Motivation

Nigeria publishes valuable infectious disease surveillance information through weekly epidemiological reports and disease-specific situation reports.

However, much of this information is distributed across individual PDF reports.

This project explores how publicly available surveillance information can be transformed into structured datasets and interactive visualisations that make it easier to:

* monitor disease activity over time
* identify high-burden states
* compare confirmed cases and mortality
* examine case fatality rates
* understand geographic disease patterns
* support data exploration for public health research

The dashboard is not intended to replace official NCDC surveillance systems or provide clinical guidance.

It is an independent data-analysis and visualisation project built from publicly available reports.

---

# Current MVP Scope

The current MVP focuses on:

**Disease:** Lassa Fever
**Country:** Nigeria
**Year:** 2026
**Weekly national data:** Epidemiological Weeks 20–30
**State-level reference dataset:** Epidemiological Week 27

The application currently provides:

* weekly confirmed case trends
* weekly suspected case trends
* weekly case fatality rate
* latest epidemiological week indicators
* confirmed cases
* deaths
* states affected
* state-level disease burden
* state-level CFR analysis
* configurable CFR case thresholds
* state ranking
* downloadable surveillance data
* interactive Plotly visualisations
* filters for disease, year, epidemiological week, state and ranking metric

The application architecture has been designed so additional diseases can later be added.

---

# Data Source

The data used in the project comes from publicly available situation reports published by the:

**Nigeria Centre for Disease Control and Prevention — NCDC**

The current MVP uses Lassa fever situation reports covering Epidemiological Weeks 20–30 of 2026.

The NCDC situation reports include information such as:

* suspected cases
* confirmed cases
* probable cases
* deaths among confirmed cases
* case fatality rate
* states affected
* LGAs affected
* healthcare worker infections
* cumulative disease burden
* age distribution
* sex distribution
* geographic distribution

The original reports are retained in:

```text
data/raw/
```

Processed datasets used by the application are stored in:

```text
data/processed/
```

---

# Data Provenance

Data provenance was treated as an important part of the project.

The original NCDC reports were retained rather than overwritten or modified.

The workflow therefore separates data into:

```text
data/raw/
```

Original source reports.

and:

```text
data/processed/
```

Structured datasets created for analysis and visualisation.

This allows the processed values to be traced back to the source material.

---

# Data Quality Considerations

During data extraction, some discrepancies were observed between sections of individual NCDC reports.

For example, a national summary table and a state-level table may occasionally report slightly different totals.

To maintain consistency, this project applies the following rule:

> For national weekly surveillance indicators, the "Current Week" values from Table 1 of each NCDC situation report are treated as the primary source.

State-level analysis is derived from the state-level surveillance table.

Data discrepancies are not silently reconciled or altered.

They should instead be documented and investigated where necessary.

This is an important consideration when working with real-world public health surveillance data.

---

# Project Development Process

## Stage 1 — Project Structure

The project was first organised into separate directories for:

* raw data
* processed data
* exploratory analysis
* data-processing scripts
* application code
* documentation

The structure was designed to separate source data from transformed data and application logic.

```text
nigeria-disease-surveillance/
│
├── app/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── scripts/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Stage 2 — Initial NCDC Report

A Lassa fever situation report was selected as the first test dataset.

The report contained both national surveillance indicators and state-level data.

The state-level table contained fields including:

* state
* suspected cases
* confirmed cases
* probable cases
* healthcare worker cases
* deaths
* cumulative suspected cases
* cumulative confirmed cases
* cumulative probable cases
* cumulative healthcare worker cases
* cumulative deaths

This structure was used to design the first processed dataset.

---

# Stage 3 — State-Level Dataset

The first processing script was created:

```text
scripts/extract_surveillance_data.py
```

This script structured the state-level surveillance information into a Pandas DataFrame.

The processed dataset was saved as:

```text
data/processed/lassa_surveillance_2026.csv
```

Important validation checks were performed after processing.

The resulting dataset contained **37 state/FCT rows**.

The cumulative totals were checked against the NCDC national report:

```text
Confirmed cases: 936
Deaths: 224
```

The processed dataset reproduced those reported totals.

This validation step was performed before moving to visualisation.

---

# Stage 4 — Exploratory Data Analysis

Exploratory analysis was performed in:

```text
notebooks/01_data_exploration.ipynb
```

The analysis included:

* inspecting dataset dimensions
* reviewing data types
* checking summary statistics
* ranking states by confirmed cases
* ranking states by deaths
* calculating state-level case fatality rates
* identifying high-burden states

Initial analysis showed that the distribution of confirmed Lassa fever cases was concentrated in a relatively small number of states.

The highest cumulative burdens in the reference dataset were seen in states including:

* Ondo
* Bauchi
* Taraba
* Edo
* Benue

---

# Case Fatality Rate

Case Fatality Rate was calculated as:

```text
CFR = deaths / confirmed cases × 100
```

One important observation during analysis was that CFR can become misleading when calculated using very small numbers of confirmed cases.

For example, a state with two confirmed cases and two deaths would have a CFR of 100%, despite having a very small absolute disease burden.

To reduce misleading comparisons, the analysis introduced a configurable minimum-case threshold when ranking states by CFR.

The Streamlit application currently defaults to a minimum confirmed-case threshold of 10 cases for state-level CFR comparisons.

---

# Stage 5 — Weekly Surveillance Dataset

To analyse temporal patterns, additional NCDC Lassa fever reports were collected covering Epidemiological Weeks 20–30.

A second processing script was created:

```text
scripts/build_weekly_lassa_dataset.py
```

The script produced:

```text
data/processed/lassa_weekly_national_2026.csv
```

Each row represents one epidemiological week.

The dataset contains:

```text
disease
year
epi_week
suspected_cases
confirmed_cases
probable_cases
deaths
weekly_cfr
states_affected
lgas_affected
```

---

# Weekly Confirmed Cases

The extracted weekly confirmed cases were:

| Epidemiological Week | Confirmed Cases |
| -------------------: | --------------: |
|                   20 |              24 |
|                   21 |              11 |
|                   22 |              13 |
|                   23 |              13 |
|                   24 |              13 |
|                   25 |              22 |
|                   26 |              31 |
|                   27 |              14 |
|                   28 |              25 |
|                   29 |              20 |
|                   30 |              17 |

This allowed the project to move from static state-level analysis to actual time-series surveillance.

---

# Weekly Surveillance Findings

Within Epidemiological Weeks 20–30:

* confirmed cases peaked at Week 26
* confirmed cases dropped sharply in Week 27
* cases increased again in Week 28
* confirmed cases subsequently declined through Weeks 29 and 30
* suspected cases remained variable and increased toward the end of the observation period
* weekly CFR was highly volatile because weekly confirmed case counts were relatively small

These findings demonstrate why multiple indicators should be interpreted together.

---

# Stage 6 — Streamlit MVP

After validating the processed datasets, the first dashboard MVP was developed using Streamlit.

Application entry point:

```text
app/app.py
```

The first version contained:

* national KPI cards
* confirmed case time series
* state disease burden chart

The application was subsequently expanded with interactive controls.

---

# Dashboard Filters

The current MVP contains filters for:

### Disease

Currently:

```text
Lassa Fever
```

The application architecture is designed to support additional diseases later.

### Year

Currently:

```text
2026
```

### Epidemiological Week

Allows the user to select the surveillance week to display.

### State

Allows users to view all states or select an individual state.

### Ranking Metric

Users can rank states using metrics including:

* confirmed cases
* suspected cases
* deaths
* case fatality rate

### Number of States

Users can choose how many states appear in ranking charts.

---

# Dashboard Indicators

The application currently displays four headline surveillance metrics:

* Confirmed Cases
* Deaths
* Weekly Case Fatality Rate
* States Affected

These values update based on the selected epidemiological week.

---

# Visualisations

The MVP currently includes:

## Weekly Confirmed Cases
<img width="2036" height="751" alt="image" src="https://github.com/user-attachments/assets/143d314b-d50d-469d-b6a5-5f8db3529896" />


An interactive line chart displaying changes in laboratory-confirmed cases by epidemiological week.

## Weekly Suspected Cases

<img width="1977" height="883" alt="image" src="https://github.com/user-attachments/assets/1f0c86b5-9a26-472a-88de-858efa58e122" />

Shows changes in suspected case reports.

## State Disease Burden

Ranks states according to the selected surveillance metric.

## Case Fatality Rate by State

<img width="1947" height="854" alt="image" src="https://github.com/user-attachments/assets/c6ec7125-10cb-4f91-9ec7-ceb8ea2cf83c" />


Compares state-level CFR while allowing the user to specify a minimum confirmed-case threshold.

---

# Data Download

The MVP allows users to download filtered surveillance data as a CSV file.

This makes the dashboard useful not only for viewing data but also for further analysis.

---

# Technology Stack

## Data Analysis

* Python
* Pandas
* NumPy
* Jupyter Notebook

## Visualisation

* Plotly

## MVP Application

* Streamlit

## Source Control

* Git
* GitHub

## Deployment

* Streamlit Community Cloud

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Enter the project directory:

```bash
cd nigeria-disease-surveillance
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

From the root project directory:

```bash
streamlit run app/app.py
```

The Streamlit application should open automatically in the browser.

---

# Project Architecture

```text
nigeria-disease-surveillance/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── Original NCDC situation reports
│   │
│   └── processed/
│       ├── lassa_surveillance_2026.csv
│       └── lassa_weekly_national_2026.csv
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── scripts/
│   ├── extract_surveillance_data.py
│   └── build_weekly_lassa_dataset.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---


# Limitations

The project currently has several important limitations.

1. The MVP currently focuses only on Lassa fever.

2. Weekly temporal analysis currently covers Epidemiological Weeks 20–30 of 2026.

3. The state-level dataset currently represents one reference epidemiological week.

4. Data is extracted from public surveillance reports rather than a live NCDC API.

5. Report formats may change over time.

6. Some reports contain inconsistencies between summary and detailed tables.

7. The dashboard does not provide clinical diagnosis, treatment recommendations or official outbreak declarations.

8. Surveillance figures may be revised by the original data publisher.

---

# Disclaimer

This is an independent educational, research, data-analysis and portfolio project.

It is **not an official NCDC application** and is not affiliated with or endorsed by the Nigeria Centre for Disease Control and Prevention.

The dashboard should not be used as a substitute for official public health surveillance systems, epidemiological guidance, clinical diagnosis or medical decision-making.

Users should consult the original NCDC publications for authoritative surveillance information.

---

# Data Attribution

Surveillance data used in this project originates from publicly available reports published by the:

**Nigeria Centre for Disease Control and Prevention (NCDC)**

Original source reports should be consulted when interpreting the processed datasets or dashboard outputs.

---

# Author

**Micaiah Adeoluwa Adedeji**

Bioinformatician and computational biologist working across genomics, biomedical data science, artificial intelligence, and infectious disease research.

---

# Project Status

**Current stage:** MVP

**Current disease:** Lassa Fever

**Current platform:** Streamlit

**Next milestones:**

* deploy MVP
* add Nigeria state map
* improve dashboard navigation
* add outbreak signal indicators
* expand to additional diseases
* build advanced full-stack web application
