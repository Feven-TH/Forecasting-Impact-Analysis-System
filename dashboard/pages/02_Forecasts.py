import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("🔮 2027 Inclusion Forecasts")

forecast_df = pd.read_csv('data/processed/forecast_results.csv')

# Sidebar: Scenario Selector
st.sidebar.header("Forecast Settings")
scenario = st.sidebar.selectbox("Choose Growth Scenario", 
                                ["Base_Case", "Optimistic", "Pessimistic"])

# Forecast Plot with Confidence Intervals
st.subheader(f"Projected Path: {scenario.replace('_', ' ')}")

fig = go.Figure()

# Add the selected scenario line
fig.add_trace(go.Scatter(x=forecast_df['Year'], y=forecast_df[scenario], 
                         name=scenario, line=dict(color='royalblue', width=4, dash='dash')))

# Add the 70% Target Line
fig.add_hline(y=70, line_dash="dot", line_color="red", 
              annotation_text="70% National Target", annotation_position="bottom right")

st.plotly_chart(fig, use_container_width=True)

# Data Download (Consortium Requirement)
st.download_button(
    label="Download Forecast Data (CSV)",
    data=forecast_df.to_csv(index=False).encode('utf-8'),
    file_name='ethiopia_inclusion_forecast.csv',
    mime='text/csv'
)