import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# 1. Page Configuration (SEO Optimized)
st.set_page_config(
    page_title="Senior Pet Care Hub | LA Quality of Life Tracker",
    page_icon="🐾",
    layout="wide"
)

# --- Verification Headers (AdSense + Search Console) ---
components.html(f"""
    <script>
        // AdSense
        var adMeta = document.createElement('meta');
        adMeta.name = "google-adsense-account";
        adMeta.content = "ca-pub-5400322511960150";
        parent.document.getElementsByTagName('head')[0].appendChild(adMeta);

        // Google Search Console (把下面这一段换成你刚才复制的那个)
        var scMeta = document.createElement('meta');
        scMeta.name = "google-site-verification";
        scMeta.content = "<meta name="google-site-verification" content="XaMamVqx7TlaKL5YIaTHoF03tMVwKv3ASmPExNx5Uu8" />"; 
        parent.document.getElementsByTagName('head')[0].appendChild(scMeta);
    </script>
""", height=0)

# 2. UI Styling (Enhanced for AdSense Approval)
st.markdown("""
    <style>
    .ad-slot { background-color: #f8f9fa; border: 1px dashed #adb5bd; color: #666; padding: 20px; text-align: center; border-radius: 8px; margin: 15px 0; }
    .stApp { background-color: #ffffff; }
    h1, h2, h3 { color: #2e7d32; }
    .article-box { 
        background-color: #f9f9f9; 
        padding: 25px; 
        border-radius: 12px; 
        border-left: 6px solid #2e7d32;
        margin: 20px 0;
        line-height: 1.8;
        color: #333;
    }
    .article-title { color: #1b5e20; font-size: 1.5rem; font-weight: bold; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation & About Us
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=70)
    st.title("Senior Pet Hub")
    app_mode = st.selectbox("Select a Module", 
        ["QoL Assessment", "Age Converter", "LA Local Resources", "Care Guides", "Legal & Contact"])
    
    st.divider()
    st.write("### About Us")
    st.caption("Supporting the senior pet community in Los Angeles with expert-backed tools and insights.")
    st.info("📍 **Location:** Los Angeles, CA")
    st.markdown('<div class="ad-slot">Side Ad Space</div>', unsafe_allow_html=True)

# --- Function for Homepage Articles & FAQ ---
def display_home_content():
    st.write("---")
    st.header("📖 Geriatric Care Insights")
    
    # Article 1: Vision Care
    st.markdown("""
    <div class="article-box">
        <div class="article-title">Guarding the Soul: Caring for the Cloudy Eyes of Aging Pets</div>
        When our furry companions slow down and their eyes begin to cloud, it’s a sign they need us more than ever. 
        <br><br>
        <b>Environmental Adjustments:</b> Joint pain makes jumping difficult. Provide thick, supportive orthopedic beds to relieve pressure. If your pet sleeps on the sofa, add a small ramp or pet steps. Raising food and water bowls can also reduce strain on their neck.
        <br>
        <b>Quality Time:</b> Spend time gently brushing their fur—it’s a form of silent comfort. In those cloudy eyes, the unconditional trust they have in you still shines bright.
    </div>
    """, unsafe_allow_html=True)

    # Article 2: Health Decoding
    st.markdown("""
    <div class="article-box">
        <div class="article-title">Decoding Health Signals: More Than Just "Slowing Down"</div>
        Many owners assume lethargy is just aging. However, many signs of aging are actually early warning signals for treatable conditions.
        <br><br>
        <b>Behavioral Changes:</b> If a dog becomes irritable when touched, it may be due to chronic pain like arthritis. 
        <b>Sensory Decline:</b> Hearing and vision loss can make pets easily startled. We recommend that pets over 7 years old receive a comprehensive veterinary checkup at least once a year.
    </div>
    """, unsafe_allow_html=True)

    # FAQ Section for SEO
    st.write("---")
    st.header("❓ Frequently Asked Questions")
    with st.expander("When should my pet start senior wellness exams?"):
        st.write("For most breeds, pets are considered 'senior' at 7 years old. Large breeds may need geriatric focus as early as 5.")
    with st.expander("Where can I find 24/7 emergency vets in Los Angeles?"):
        st.write("Check our 'LA Local Resources' tab for a list of emergency clinics in West LA, Culver City, and Hollywood.")

# --- Module Logic ---

# 1. Quality of Life Assessment (HOMEPAGE)
if app_mode == "QoL Assessment":
    st.header("🐕 Senior Pet Quality of Life (QoL) Tracker")
    st.write("Assess your pet's well-being daily using the professional HHHHHMM scale.")
    
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
                st.subheader(f"Daily Score: {score}/60")
                st.progress(score/60)

    with col2:
        st.markdown('<div class="ad-slot" style="height:300px;">Contextual Ad Space</div>', unsafe_allow_html=True)
    
    # 首页调用文章和FAQ
    display_home_content()

# 2. Age Converter
elif app_mode == "Age Converter":
    st.header("🐱 Pet Age to Human Years")
    p_type = st.selectbox("Species", ["Dog", "Cat"])
    p_age = st.number_input("Actual Age", 1, 25, 10)
    h_age = p_age * 7 if p_type == "Dog" else p_age * 6
    st.metric("Human Equivalent", f"~{h_age} Years Old")
    st.markdown('<div class="ad-slot">Mid-Page Ad Space</div>', unsafe_allow_html=True)

# 3. LA Resources
elif app_mode == "LA Local Resources":
    st.header("📍 Los Angeles Senior Pet Resources")
    la_data = {
        "Service": ["Lap of Love", "Two Hands Four Paws", "VCA West LA", "Paws in Motion"],
        "Specialty": ["In-Home Euthanasia", "Hydrotherapy", "24/7 Specialist", "Mobile Vet"],
        "Contact": ["(855) 933-5683", "(310) 475-8555", "(310) 473-2951", "(818) 555-0123"]
    }
    st.table(pd.DataFrame(la_data))
    st.map(pd.DataFrame({'lat': [34.0522], 'lon': [-118.2437]}))

# 4. Care Guides (Detailed Content)
elif app_mode == "Care Guides":
    st.header("📚 Senior Pet Knowledge Base")
    t1, t2, t3 = st.tabs(["Joint & Mobility", "Cognitive Health", "LA Weather Safety"])
    with t1:
        st.subheader("Managing Arthritis")
        st.write("Focus on weight management and orthopedic support to help your pet move comfortably.")
    with t2:
        st.subheader("Cognitive Health")
        st.write("Keep a consistent environment and routine to reduce anxiety for pets showing signs of dementia.")
    with t3:
        st.subheader("LA Heat Safety")
        st.write("Never walk your senior pet on hot asphalt during SoCal heatwaves. Use the 5-second rule.")

# 5. Legal & Contact
elif app_mode == "Legal & Contact":
    st.header("Legal & Policy Center")
    tab1, tab2, tab3 = st.tabs(["Privacy Policy", "Terms of Service", "Contact Us"])
    with tab1:
        st.write("**Privacy Policy:** We comply with standard 2026 data protection protocols. Your privacy is our priority.")
    with tab2:
        st.warning("**Medical Disclaimer:** This tool is for educational purposes only. Always consult a veterinarian for medical advice.")
    with tab3:
        st.write("📩 **Email Support:** w63812643@gmail.com")
        st.write("📍 **Location:** Los Angeles, California")

# --- Footer (Required for Compliance) ---
st.divider()
st.markdown("""
<div style="text-align: center; font-size: 0.8rem; color: #888;">
    <p>Senior Pet Hub LA | <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a></p>
</div>
""", unsafe_allow_html=True)