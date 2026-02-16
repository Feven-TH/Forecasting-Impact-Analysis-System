import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Inclusion Projections", layout="wide")

st.title("🎯 Target Progress & Projections")


forecast_df = pd.read_csv('data/processed/forecast_results.csv')

# Scenario Selector
scenario = st.radio("Select Strategy Scenario:", 
                    ("Base_Case", "Optimistic", "Pessimistic"), horizontal=True)

# Progress toward 60% and 70% Target Visualization
st.subheader(f"Path to National Goals ({scenario.replace('_', ' ')})")

fig = px.area(forecast_df, x='Year', y=scenario, 
              title="Projected Inclusion Rate vs. Strategic Targets",
              color_discrete_sequence=['#636EFA'])

# Add Strategic Target Lines
fig.add_hline(y=60, line_dash="dash", line_color="green", annotation_text="Initial Goal (60%)")
fig.add_hline(y=70, line_dash="dot", line_color="red", annotation_text="NFIS II Target (70%)")

st.plotly_chart(fig, use_container_width=True)

# Answers to Consortium's Key Questions
st.divider()
st.subheader("Consortium FAQ")

with st.expander("Will Ethiopia hit the 70% target by 2027?"):
    final_val = forecast_df.iloc[-1][scenario]
    if final_val >= 70:
        st.success(f"**Yes.** Under the {scenario} scenario, we reach {final_val:.1f}%.")
    else:
        st.error(f"**No.** Under the {scenario} scenario, we only reach {final_val:.1f}%.")

with st.expander("What is the biggest driver of this growth?"):
    st.write("According to our Task 3 Association Matrix, **Digital ID (Fayda)** and **Telecom Competition (Safaricom)** provide the highest impact weights for new account openings.")

with st.expander("When will we hit the 60% milestone?"):
    # Simple logic to find when it crosses 60
    year_60 = forecast_df[forecast_df[scenario] >= 60]['Year'].min()
    st.write(f"Estimated Milestone Year: **{year_60}**")