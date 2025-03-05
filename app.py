
import streamlit as st
import model

# Streamlit UI
st.title("Twitter Trending Topics Predictor")

country = st.selectbox("Select Country", model.df['country'].unique())
context_options = model.get_contexts_for_country(country)
context = st.selectbox("Select Context", context_options)

if st.button("Predict Trending Topic"):
    trending_topic = model.predict_trending_topic(country, context)
    st.success(f"Predicted Trending Topic: {trending_topic}")