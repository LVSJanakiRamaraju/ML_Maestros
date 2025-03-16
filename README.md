# Twitter Trending Topics Predictor

## Overview
The **Twitter Trending Topics Predictor** is a machine learning-powered web application that predicts trending topics on Twitter based on country and context selection. Built using **Streamlit**, it leverages machine learning techniques to analyze and forecast popular discussions across different regions.

## Features
- **Predict trending topics** based on country and context.
- **User-friendly UI** developed with Streamlit.
- **Machine learning model** using Random Forest for predictions.
- **KMeans clustering** for filtering relevant contexts per country.
- **Team members and instructor profile pages** for better engagement.

## Technologies Used
- **Frontend**: Streamlit (Python-based UI framework)
- **Backend**: Python (pandas, scikit-learn)
- **Machine Learning**: Random Forest Classifier, KMeans Clustering
- **Dataset**: Twitter data (CSV format)

## Installation
### Prerequisites
Ensure you have Python installed (version 3.8 or later).

### Steps to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/LVSJanakiRamaraju/ML_Maestros.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## How It Works
1. **Data Preprocessing**: Categorical features (country, context, name) are encoded.
2. **Clustering**: KMeans algorithm groups similar contexts for filtering.
3. **Model Training**: Random Forest Classifier predicts trending topics based on historical data.
4. **User Input & Prediction**: User selects a country & context, and the model predicts the trending topic.

## Team Members
- **Rama Raju** - Problem Solver | UI/UX Designer
- **Satish** - ML Expert | Model Developer
- **Abhi Ram** - Data Scientist | Model Analyzer
- **Manoj** - Developer | Model Optimizer
- **Pavan** - ML Researcher | AI Engineer

## Contact
For queries or collaboration, contact us via email:
📧 **rajakanumuri2005@gmail.com**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
