import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Solar Panel ROI Calculator for US Homeowners 2026")

st.markdown("""
Estimate payback period and savings for solar installation.  
*Based on 2026 average data — adjust inputs as needed.*
""")

# 输入部分
col1, col2 = st.columns(2)
with col1:
    system_size_kw = st.number_input("System size (kW)", min_value=1.0, max_value=20.0, value=6.0, step=0.5)
    cost_per_kw = st.number_input("Cost per kW (after incentives)", min_value=1000, max_value=4000, value=2500, step=100)
with col2:
    annual_production_kwh_per_kw = st.number_input("Annual kWh per kW (depends on location)", 800, 1800, 1300, 50)
    electricity_rate = st.number_input("Electricity rate ($/kWh)", 0.08, 0.50, 0.16, 0.01)
    annual_escalation = st.slider("Annual electricity price increase (%)", 0.0, 5.0, 3.0, 0.5) / 100

total_cost = system_size_kw * cost_per_kw
annual_production = system_size_kw * annual_production_kwh_per_kw
annual_savings_year1 = annual_production * electricity_rate

# 简单计算回本期（忽略维护、折现等）
years = np.arange(1, 26)
cumulative_savings = np.cumsum([annual_savings_year1 * (1 + annual_escalation)**y for y in years-1])

payback_year = next((y for y, s in zip(years, cumulative_savings) if s >= total_cost), None)

st.subheader("Results")
st.metric("Estimated total cost", f"${total_cost:,.0f}")
st.metric("First year savings", f"${annual_savings_year1:,.0f}")
if payback_year:
    st.metric("Estimated payback period", f"{payback_year} years")
else:
    st.metric("Payback period", "More than 25 years")

# 图表
fig, ax = plt.subplots()
ax.plot(years, cumulative_savings, label="Cumulative savings")
ax.axhline(total_cost, color='r', linestyle='--', label="Installation cost")
ax.set_xlabel("Years")
ax.set_ylabel("USD")
ax.legend()
st.pyplot(fig)

st.markdown("---")
st.caption("This is a simplified model. Actual results vary by location, incentives, financing, etc.")