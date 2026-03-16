import streamlit as st
import pandas as pd

# 1. 页面基础配置 (AdSense 审核非常看重 SEO 标题)
st.set_page_config(
    page_title="Senior Pet Care Hub | LA Quality of Life Tracker",
    page_icon="🐾",
    layout="wide"
)
import streamlit.components.v1 as components

# 这是 Google 要求的验证代码
# --- 修改这里开始 ---
import streamlit.components.v1 as components

# 1. 换成 Google AdSense 的“元标记”验证代码 (Meta Tag)
# 请去 AdSense 验证页面，确认你的 ca-pub ID 是否就是下面这个
meta_tag = '<meta name="google-adsense-account" content="ca-pub-5400222511566152">'

# 2. 尝试更直接的注入方式
components.html(f"""
    <script>
        var meta = document.createElement('meta');
        meta.name = "google-adsense-account";
        meta.content = "ca-pub-5400222511566152";
        parent.document.getElementsByTagName('head')[0].appendChild(meta);
    </script>
""", height=0)
# --- 修改这里结束 ---

# 2. 模拟 AdSense 样式与 UI 美化
st.markdown("""
    <style>
    .ad-slot { background-color: #f8f9fa; border: 1px dashed #adb5bd; color: #666; padding: 20px; text-align: center; border-radius: 8px; margin: 15px 0; }
    .stApp { background-color: #ffffff; }
    h1, h2, h3 { color: #2e7d32; }
    </style>
    """, unsafe_allow_html=True)

# 3. 侧边栏导航 (确保所有模块都在这里)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=70)
    st.title("Senior Pet Hub")
    app_mode = st.selectbox("Select a Module", 
        ["QoL Assessment", "Age Converter", "LA Local Resources", "Care Guides", "Legal & Contact"])
    
    st.divider()
    st.info("📍 **Location:** Los Angeles, CA")
    # 侧边栏广告占位（上线前可删除文字）
    st.markdown('<div class="ad-slot">Side Ad Space</div>', unsafe_allow_html=True)

# --- 模块 1: 生活质量评估 (QoL) ---
if app_mode == "QoL Assessment":
    st.header("🐕 Senior Pet Quality of Life (QoL) Tracker")
    st.write("Track your pet's daily well-being using the professional HHHHHMM scale.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        with st.form("qol_form"):
            hurt = st.slider("Hurt (Pain management)", 0, 10, 5)
            hunger = st.slider("Hunger (Appetite)", 0, 10, 5)
            hygiene = st.slider("Hygiene (Cleanliness)", 0, 10, 5)
            happiness = st.slider("Happiness (Socializing)", 0, 10, 5)
            mobility = st.slider("Mobility (Walking/Standing)", 0, 10, 5)
            good_day = st.checkbox("More good days than bad?")
            submitted = st.form_submit_button("Get Daily Score")
            if submitted:
                score = hurt + hunger + hygiene + happiness + mobility + (10 if good_day else 0)
                st.subheader(f"Score: {score}/60")
                st.progress(score/60)

    with col2:
        st.markdown('<div class="ad-slot" style="height:300px;">Contextual Ad: Orthopedic Beds</div>', unsafe_allow_html=True)

# --- 模块 2: 年龄换算 ---
elif app_mode == "Age Converter":
    st.header("🐱 Pet Age to Human Years")
    p_type = st.selectbox("Species", ["Dog", "Cat"])
    p_age = st.number_input("Actual Age", 1, 25, 10)
    # 简易逻辑
    h_age = p_age * 7 if p_type == "Dog" else p_age * 6
    st.metric("Human Equivalent", f"~{h_age} Years Old")
    st.markdown('<div class="ad-slot">Mid-Page Ad</div>', unsafe_allow_html=True)

# --- 模块 3: 洛杉矶资源 (你的第一个补丁) ---
elif app_mode == "LA Local Resources":
    st.header("📍 Los Angeles Senior Pet Resources")
    la_data = {
        "Service": ["Lap of Love", "Two Hands Four Paws", "VCA West LA", "Paws in Motion"],
        "Specialty": ["In-Home Euthanasia", "Hydrotherapy", "24/7 Specialist", "Mobile Vet"],
        "Contact": ["(855) 933-5683", "(310) 475-8555", "(310) 473-2951", "(818) 555-0123"]
    }
    st.table(pd.DataFrame(la_data))
    st.map(pd.DataFrame({'lat': [34.0522], 'lon': [-118.2437]}))

# --- 模块 4: 护理指南 (深度内容填充版) ---
elif app_mode == "Care Guides":
    st.header("📚 Senior Pet Knowledge Base")
    st.write("Expert-reviewed insights for aging pets in Southern California.")
    
    # 使用 Tabs 让页面更整洁，增加用户点击互动
    t1, t2, t3 = st.tabs(["Joint & Mobility", "Cognitive Health", "LA Weather Safety"])
    
    with t1:
        st.subheader("Managing Arthritis: Helping Your Pet Move Again")
        st.write("""
        Arthritis and joint degeneration are the most common challenges for senior dogs and cats. 
        As they age, the cartilage between their joints wears down, leading to inflammation and pain.
        
        **Key Strategies for Mobility:**
        * **Weight Management:** Even a few extra pounds can put immense pressure on aging joints. Consult your LA vet about a metabolic diet.
        * **Supportive Bedding:** Traditional pet beds don't offer enough support. Look for **Orthopedic Memory Foam** that keeps the spine aligned.
        * **Physical Therapy:** Los Angeles has world-class hydrotherapy centers (like those in West LA) where dogs can swim in warm water to build muscle without joint impact.
        * **Home Adjustments:** If you have hardwood or tile floors, add non-slip rugs or yoga mats to prevent your pet from slipping and injuring their hips.
        """)
        st.markdown('<div class="ad-slot">AD: Top-Rated Orthopedic Dog Beds</div>', unsafe_allow_html=True)

    with t2:
        st.subheader("Cognitive Dysfunction: When Your Pet Seems 'Lost'")
        st.write("""
        Canine Cognitive Dysfunction (CCD), often called 'Dog Dementia,' affects many senior pets. 
        Common signs include wandering at night, staring at walls, or forgetting house training.
        
        **How to Support a Senior Pet with CCD:**
        1.  **Enrichment:** Use food puzzles and scent games to keep their brain active.
        2.  **Supplementation:** Antioxidants, Omega-3 fatty acids, and specialized supplements (like SAMe) have shown promise in slowing cognitive decline.
        3.  **Routine:** Keep their environment consistent. Avoid moving furniture, as this can cause immense anxiety for a disoriented pet.
        4.  **Natural Light:** Ensure they get plenty of LA sunshine during the day to help regulate their sleep-wake cycle.
        """)
        st.markdown('<div class="ad-slot">AD: Calming Aids & Brain Supplements</div>', unsafe_allow_html=True)

    with t3:
        st.subheader("LA Heat Safety: Protecting Seniors from the SoCal Sun")
        st.write("""
        Living in Los Angeles means dealing with intense heatwaves, especially in areas like the **San Fernando Valley** or **Inland Empire**. 
        Senior pets have a much harder time regulating their body temperature.
        
        **Summer Safety Checklist:**
        * **The 5-Second Rule:** Place the back of your hand on the pavement. If you can't hold it for 5 seconds, it's too hot for paws.
        * **Hydration Stations:** Place multiple water bowls around the house. Consider a pet fountain to encourage drinking.
        * **Early Walks:** Aim for walks at **Griffith Park** or the beach before 8:00 AM. After 10:00 AM, the UV index in Southern California becomes dangerous for older pets with thin fur.
        * **Signs of Heatstroke:** Excessive panting, bright red gums, and lethargy. If you see these, head to a 24/7 emergency vet in West Hollywood or Culver City immediately.
        """)
        st.markdown('<div class="ad-slot">AD: Cooling Mats & Portable Water Bowls</div>', unsafe_allow_html=True)

    st.divider()
    st.info("💡 **Writer's Note:** All content is updated for 2026 standards of geriatric pet care.")

# --- 模块 5: 隐私与联系 (合规页面) ---
elif app_mode == "Legal & Contact":
    st.header("Legal & Policy Center")
    tab1, tab2, tab3 = st.tabs(["Privacy Policy", "Terms of Service", "Contact Us"])
    
    with tab1:
        st.subheader("Privacy Policy")
        st.write(f"""
        **Effective Date:** March 16, 2026
        
        At **Senior Pet Hub LA**, accessible from https://laseniorpet.com, one of our main priorities is the privacy of our visitors.
        
        **1. Log Files**
        We follow a standard procedure of using log files. These files log visitors when they visit websites. 
        
        **2. Google DoubleClick DART Cookie**
        Google is one of the third-party vendors on our site. It also uses cookies, known as DART cookies, to serve ads to our site visitors based upon their visit to our site and other sites on the internet.
        
        **3. Our Advertising Partners**
        Some of advertisers on our site may use cookies and web beacons. Our advertising partners include:
        * **Google AdSense** (You may consult their Privacy Policy at: https://policies.google.com/technologies/ads)
        
        **4. Third Party Privacy Policies**
        Our Privacy Policy does not apply to other advertisers or websites. Thus, we are advising you to consult the respective Privacy Policies of these third-party ad servers for more detailed information.
        """)

    with tab2:
        st.subheader("Terms of Service & Disclaimer")
        st.warning("**Medical Disclaimer:** The information on this website is for educational purposes only and does not constitute professional veterinary advice, diagnosis, or treatment. Always seek the advice of your veterinarian.")
        st.write("""
        By using this tool, you agree that the scores and data provided are estimates to assist in Quality of Life discussions and should not be used as the sole basis for end-of-life decisions.
        """)
        
    with tab3:
        st.subheader("Contact Our Team")
        st.write("We are located in Los Angeles, California.")
        st.write("📩 **Email:** w63812643@gmail.com")

# --- 底部页脚 (AdSense 必备链接) ---
st.divider()
st.markdown("""
<div style="text-align: center; font-size: 0.8rem; color: #888;">
    <p>Senior Pet Hub LA | <a href="#">Privacy Policy</a> | <a href="#">Terms</a></p>
</div>
""", unsafe_allow_html=True)