import streamlit as st
import model

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Team", "Instructor", "Model Workflow"])

# Home Page - Prediction UI
if page == "Home":
    st.title("Twitter Trending Topics Predictor")

    country = st.selectbox("Select Country", model.df['country'].unique())
    context_options = model.get_contexts_for_country(country)
    context = st.selectbox("Select Context", context_options)

    if st.button("Predict Trending Topic"):
        trending_topic = model.predict_trending_topic(country, context)
        st.success(f"Predicted Trending Topic: {trending_topic}")

# Team Members Section
elif page == "Team":
    st.title("Meet Our Team : ML Maestros")

    team_members = {
        "Rama Raju": ("Problem Solver | UI/UX Designer","https://res.cloudinary.com/drlfc6gsb/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1741190082/Screenshot_2024-05-03_065557_lr3iim.png"),
        "Satish": ("ML Expert | Model Developer","https://res.cloudinary.com/drlfc6gsb/image/upload/w_1000,c_fill,ar_1:1,g_auto,r_max,bo_5px_solid_red,b_rgb:262c35/v1741190486/WhatsApp_Image_2025-03-05_at_9.15.35_PM_r36pyr.jpg"),
        "Abhi Ram": ("Data Scientist | Model Analyzer","https://res.cloudinary.com/drlfc6gsb/image/upload/w_1000,c_fill,ar_1:1,g_auto,r_max,bo_5px_solid_red,b_rgb:262c35/v1741190582/WhatsApp_Image_2025-03-05_at_9.15.33_PM_zvcc9n.jpg"),
        "Manoj": ("Developer | Model Optimizer","https://res.cloudinary.com/drlfc6gsb/image/upload/w_1000,c_fill,ar_1:1,g_auto,r_max,bo_5px_solid_red,b_rgb:262c35/v1741190696/WhatsApp_Image_2025-03-05_at_9.06.55_PM_qmjing.jpg"),
        "Pavan": ("ML Researcher | AI Engineer","https://res.cloudinary.com/drlfc6gsb/image/upload/w_1000,c_fill,ar_1:1,g_auto,r_max,bo_5px_solid_red,b_rgb:262c35/v1741190700/WhatsApp_Image_2025-03-05_at_9.30.22_PM_nvzbfn.jpg")
    }
    for name, (role, img_path) in team_members.items():
        col1, col2 = st.columns([1, 3])  # Create two columns for image & text
        with col1:
            st.image(img_path, width=120)  # Display image
        with col2:
            st.subheader(name)
            st.write(role)


# Instructor Profile Section
elif page == "Instructor":
    st.title("Instructor Profile")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://media.licdn.com/dms/image/v2/C4D03AQHvE3ZzPxUDCA/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1516846311487?e=1746662400&v=beta&t=5vRBpBuPVZ0DO0wgv3x-otf73FadC2h9UZBXtaXadng", width=120)
    with col2:
        st.subheader("S Ratan Kumar,")
        st.write("Programmer | Passionate Educator in Cyber Security, Data Science, AI, ML | Trainer in Wireshark, NMAP, Burp Suite, Ghidra,MS Excel, SQL,Tableau, Power BI, Orange, Rapid Miner, Weka, KNIME")

# Model Workflow Section
elif page == "Model Workflow":
    st.title("How Our Model Works")
    st.write("""
    1. **Data Collection**: Fetches real-time Twitter data from different countries.
    2. **Preprocessing**: Cleans the data, removes stop words, and applies Data Handling & Preprocessing.
    3. **Feature Engineering**: Extracts key features like hashtags, user engagement, etc.
    4. **Prediction Model**: Uses a trained ML model to predict trending topics.
    5. **Output Generation**: Displays the most likely trending topic for the selected country & context.
    """)

