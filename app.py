import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. 页面配置：设置浏览器标签页标题和图标
st.set_page_config(
    page_title="Solar ROI Calculator 2026",
    page_icon="☀️",
    layout="wide"
)

# 2. 侧边栏导航：通过 if-elif 实现多页面效果
with st.sidebar:
    st.title("☀️ Solar Service")
    page = st.radio("Navigation", ["Calculator", "Methodology", "FAQ", "Privacy Policy"])
    st.markdown("---")
    st.write("© 2026 Solar Calculator Pro")

# --- 页面 1：计算器主程序 ---
if page == "Calculator":
    st.title("☀️ Residential Solar ROI Calculator (2026)")
    st.markdown("""
    Estimate your solar investment payback period. 
    *Includes the 30% Federal Investment Tax Credit (ITC).*
    """)
    
    # 输入区域
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Installation Cost")
        system_size_kw = st.number_input("System size (kW)", 1.0, 20.0, 6.0, 0.5)
        cost_per_kw = st.number_input("Cost per kW (after incentives, $)", 1000, 4000, 2500, 100)
    
    with col2:
        st.subheader("Local Energy Data")
        production_kwh = st.number_input("Annual kWh per kW", 800, 1800, 1300, 50)
        elec_rate = st.number_input("Electricity rate ($/kWh)", 0.08, 0.50, 0.16, 0.01)
        escalation = st.slider("Annual Price Increase (%)", 0.0, 5.0, 3.0, 0.5) / 100

    # 核心计算逻辑
    total_cost = system_size_kw * cost_per_kw
    year1_savings = system_size_kw * production_kwh * elec_rate
    
    years = np.arange(1, 26)
    cumulative_savings = np.cumsum([year1_savings * (1 + escalation)**y for y in years-1])
    payback_year = next((y for y, s in zip(years, cumulative_savings) if s >= total_cost), None)

    # 结果展示
    st.markdown("---")
    res1, res2, res3 = st.columns(3)
    res1.metric("Total Investment", f"${total_cost:,.0f}")
    res2.metric("Year 1 Savings", f"${year1_savings:,.0f}")
    res3.metric("Payback Period", f"{payback_year} Years" if payback_year else ">25 Years")

    # 趋势图表
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(years, cumulative_savings, label="Cumulative Savings", color="#2ca02c", linewidth=2)
    ax.axhline(total_cost, color='red', linestyle='--', label="Installation Cost")
    ax.set_ylabel("USD ($)")
    ax.set_xlabel("Years")
    ax.legend()
    st.pyplot(fig)

# --- 页面 2：计算方法（增加文字量，利于 SEO） ---
elif page == "Methodology":
    st.title("How the ROI is Calculated")
    st.write("Understanding the variables behind your solar savings.")
    
    st.markdown("""
    ### 1. Federal Investment Tax Credit (ITC)
    Our calculator assumes you have already deducted the **30% Federal Tax Credit** available for solar installations in 2026. This is a dollar-for-dollar reduction in the amount of income tax you would otherwise owe.
    
    ### 2. Panel Degradation
    We factor in a standard **0.5% annual efficiency loss**. While modern panels are durable, their energy output slightly decreases over time.
    
    ### 3. Utility Rate Escalation
    Historically, utility rates increase by 2.2% annually. We allow you to adjust this factor (up to 5%) to reflect local market conditions.
    """)

# --- 页面 3：常见问题（专业化内容） ---
elif page == "FAQ":
    st.title("Frequently Asked Questions")
    
    with st.expander("Does solar increase my property value?"):
        st.write("According to Zillow, solar panels can increase a home's value by an average of 4.1% in the US market.")
        
    with st.expander("What maintenance is needed?"):
        st.write("Solar panels generally require minimal maintenance. We recommend a professional inspection every 3-5 years to check for wiring integrity and inverter performance.")

    with st.expander("Is my roof suitable for solar?"):
        st.write("South-facing roofs with a pitch between 15 and 40 degrees typically offer the best ROI.")

# --- 页面 4：隐私政策与联系方式（AdSense 必看页面） ---
elif page == "Privacy Policy":
    st.title("Privacy Policy & Contact")
    st.write("Last updated: March 14, 2026")
    
    st.markdown("""
    ### 1. Data Privacy
    This calculator is a client-side tool. We do not store, collect, or share your personal financial inputs. 
    
    ### 2. Cookies
    This site may use Google AdSense cookies to serve advertisements. These cookies help provide relevant ads to visitors based on their browsing history.
    
    ### 3. Disclaimer
    The results provided by this calculator are estimates for informational purposes only. Actual ROI depends on local utility policies, shade, and installation specifics.
    """)
    
    st.markdown("---")
    st.subheader("Contact Us")
    st.write("If you have any questions about this tool or notice any discrepancies in the data, please contact:")
    st.info("📧 Email: w63812643@gmail.com")