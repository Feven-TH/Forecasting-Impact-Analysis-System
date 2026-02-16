import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Ethiopia FI Dashboard", layout="wide")

# Load and Transform Data
@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/ethiopia_fi_cleaned.csv')
    
    # 1. Convert date to Year if 'Year' column is missing
    if 'Year' not in df.columns:
        df['Year'] = pd.to_datetime(df['observation_date']).dt.year
    
    # 2. Pivot the data: Turn indicators into columns
    # This creates columns like 'p2p_usage', 'atm_usage', etc.
    df_pivoted = df.pivot_table(
        index='Year', 
        columns='indicator', 
        values='value_numeric', 
        aggfunc='mean'
    ).reset_index()
    
    # 3. Clean column names (lowercase and no spaces)
    df_pivoted.columns = [c.lower().replace(' ', '_') for c in df_pivoted.columns]
    return df_pivoted

df_hist = load_data()

st.title("🇪🇹 Ethiopia Financial Inclusion Dashboard")

# Check if columns exist before plotting to avoid errors
expected = ['p2p_usage', 'atm_usage']
available = [c for c in expected if c in df_hist.columns]

if len(available) > 0:
    fig = px.line(df_hist, x='year', y=available, 
                  title="The Digital Shift",
                  width='stretch') # Fix for the 2026 deprecation warning
    st.plotly_chart(fig)
else:
    st.warning(f"Columns not found. Available: {list(df_hist.columns)}")