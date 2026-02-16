import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Historical Trends", layout="wide")

st.title("📈 Historical Usage Trends")
st.markdown("Explore how different financial channels have evolved over the last decade.")

# --- DATA TRANSFORMATION FUNCTION ---
@st.cache_data
def get_transformed_data():
    raw_df = pd.read_csv('data/processed/ethiopia_fi_cleaned.csv')
    if 'Year' not in raw_df.columns:
        raw_df['Year'] = pd.to_datetime(raw_df['observation_date']).dt.year
    
    # This turns values in the 'indicator' column into their own actual columns
    df_wide = raw_df.pivot_table(
        index='Year', 
        columns='indicator', 
        values='value_numeric', 
        aggfunc='mean'
    ).reset_index()
    
    df_wide.columns = [str(c).lower().replace(' ', '_') for c in df_wide.columns]
    return df_wide


df = get_transformed_data()


st.sidebar.header("Filter Data")
min_yr, max_yr = int(df['year'].min()), int(df['year'].max())
year_range = st.sidebar.slider("Select Year Range", min_yr, max_yr, (min_yr, max_yr))

filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

#CHANNEL COMPARISON VIEW
st.subheader("Comparison of Digital vs. Traditional Channels")

# Dynamically find available columns that aren't 'year'
available_indicators = [c for c in df.columns if c != 'year']
default_selections = [c for c in ['p2p_usage', 'atm_usage'] if c in available_indicators]

channels = st.multiselect(
    "Select Channels to Compare", 
    options=available_indicators,
    default=default_selections
)

if channels:
    fig = px.line(
        filtered_df, 
        x='year', 
        y=channels, 
        title=f"Usage Trends ({year_range[0]} - {year_range[1]})",
        markers=True
    )
    # Using width='stretch' to address the 2026 deprecation warning
    st.plotly_chart(fig, width='stretch')
else:
    st.warning("Please select at least one channel to view the trend.")

# GROWTH RATE HIGHLIGHT 
st.subheader("Growth Rate Highlights")

if 'p2p_usage' in df.columns:
    # Calculate growth based on first and last available non-null rows
    first_val = df['p2p_usage'].dropna().iloc[0]
    last_val = df['p2p_usage'].dropna().iloc[-1]
    total_growth = ((last_val - first_val) / first_val) * 100
    st.write(f"Total P2P usage growth in recorded data: **{total_growth:.1f}%**")
else:
    st.write("Growth metrics for P2P are unavailable in this dataset.")