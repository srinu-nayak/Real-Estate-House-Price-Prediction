import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠", layout='wide')  # Must be first Streamlit command


st.title("🏠 House or Flat Price Prediction & Recommendations")

# Introduction
st.markdown("""
Welcome to the **Real Estate House & Flat Price Predictor**. This tool uses machine learning models trained on real-world data to help you:
""")

# Key Features
st.markdown("""
### 🔍 What We Offer
- **🏡 Predict House & Flat Prices Accurately**  
  Estimate property values based on features like location, size, furnishing, and amenities.
- **📊 Data-Driven Decision Making**  
  Make informed decisions using insights from real listings in Gurgaon.
- **🏙️ Location-Specific Trends**  
  View sector-wise pricing differences to choose your ideal neighborhood.
- **🔧 Customize Your Search**  
  Select property features and get instant price predictions.
- **💡 Property Recommendations**  
  Receive suggestions for similar properties matching your preferences.
- **💬 Simple & Transparent Interface**  
  Whether you're a buyer, renter, or investor — we make it easy to explore prices.
""")


# Call to action or instructions
st.info("👈 Use the sidebar to explore pages like 🗺️ Interactive map of listings and Live Predictions.")
