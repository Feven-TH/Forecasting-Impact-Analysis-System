# Ethiopia Financial Inclusion Forecasting System (2025-2027)

## Overview
This project, developed for **Selam Analytics**, provides an end-to-end analytical framework to forecast Ethiopia's digital financial transformation. By integrating historical Findex data with modern "policy shocks" (Digital ID, Telecom liberalization), the system projects inclusion rates through 2027 to assess progress against national targets.

## Key Findings & Results
- **2027 Projection**: The model predicts a **72.60%** account ownership rate under the Base Case.
- **Target Assessment**: Ethiopia is currently **on track** to exceed the National Financial Inclusion Strategy (NFIS II) target of 70% by **2.60%**.
- **The Digital Crossover**: Analysis confirms a structural shift where mobile P2P transaction frequency has surpassed traditional ATM cash withdrawals.

---

## Folder Structure
- `notebooks/`:
    - `01_data_exploration.ipynb`: Initial cleaning and long-to-wide transformation.
    - `02_eda_visualizations.ipynb`: Historical trend analysis and crossover detection.
    - `03_impact_matrix.ipynb`: Association matrix linking events (Fayda, Safaricom) to KPIs.
    - `04_forecasting.ipynb`: Event-augmented linear regression and scenario generation.
- `data/processed/`: Contains the critical `forecast_results.csv` and `ethiopia_fi_cleaned.csv`.
- `dashboard/`:
    - `app.py`: Main overview and KPI hub.
    - `pages/`: Multi-page directory for Trends, Forecasts, and Target tracking.
- `reports/figures/`: Exported visualizations for stakeholder presentations.

---

## Technical Requirements
To run this system, you need Python 3.10+ and the following libraries:
- `streamlit` (Dashboard framework)
- `pandas` (Data manipulation)
- `plotly` (Interactive visualizations)
- `scikit-learn` (Trend modeling)

---

## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/Feven-TH/Forecasting-Impact-Analysis-System.git
dc Ethiopia-Forecasting-System
```

### 2. Set Up Virtual Environment
```bash
ython3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Running the Dashboard
The interactive dashboard is the primary interface for stakeholders. Run it using:
```bash
streamlit run dashboard/app.py
```
# Dashboard Sections

### Overview Page
- Summary cards for current account ownership and the P2P/ATM crossover indicator.

### Trends Page
- Interactive time-series explorer with a date range slider and channel comparison tools.

### Forecasts Page
- Visualizes the 2027 "Fan Chart" with Base, Optimistic, and Pessimistic scenarios.

### Inclusion Projections
- Direct answers to consortium questions regarding the 60% and 70% milestones.

### Data Download
- The dashboard includes built-in functionality on the Forecasts page allowing users to export the raw projection data as a CSV for further external analysis.
