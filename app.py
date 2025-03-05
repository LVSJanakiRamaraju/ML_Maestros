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
        "Rama Raju": "Problem Solver | UI/UX Designer",
        "Satish": "ML Expert | Model Developer",
        "Abhi Ram": "Data Scientist | Model Analyzer",
        "Manoj": "Developer | Model Optimizer",
        "Pavan": "ML Researcher | AI Engineer"
    }
    for name, role in team_members.items():
        st.subheader(name)
        st.write(role)

# Instructor Profile Section
elif page == "Instructor":
    st.title("Instructor Profile")
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

