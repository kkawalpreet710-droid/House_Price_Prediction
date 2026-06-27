import streamlit as st
import joblib
import numpy as np

model = joblib.load('house_price_model.pkl')

st.set_page_config(page_title="House Price Predictor", page_icon="🏠")

st.title("🏠 House Price Predictor")
st.markdown("Enter the property details below to get an estimated price.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (sq ft)", min_value=500, max_value=15000, value=3000, step=100)
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
    stories = st.number_input("Stories", min_value=1, max_value=10, value=2)
    parking = st.number_input("Parking spots", min_value=0, max_value=5, value=1)
    furnishingstatus = st.selectbox("Furnishing status", options=["Furnished", "Semi-furnished", "Unfurnished"])

with col2:
    mainroad = st.selectbox("Main road access", options=["Yes", "No"])
    guestroom = st.selectbox("Guest room", options=["Yes", "No"])
    basement = st.selectbox("Basement", options=["Yes", "No"])
    hotwaterheating = st.selectbox("Hot water heating", options=["Yes", "No"])
    airconditioning = st.selectbox("Air conditioning", options=["Yes", "No"])
    prefarea = st.selectbox("Preferred area", options=["Yes", "No"])

st.divider()

def yes_no(val):
    return 1 if val == "Yes" else 0

# drop_first=True dropped: mainroad_no, guestroom_no, basement_no,
# hotwaterheating_no, airconditioning_no, prefarea_no, furnishingstatus_furnished
furnishing_semifurnished = 1 if furnishingstatus == "Semi-furnished" else 0
furnishing_unfurnished = 1 if furnishingstatus == "Unfurnished" else 0

if st.button("Predict Price", use_container_width=True, type="primary"):
    features = np.array([[
        area,
        bedrooms,
        bathrooms,
        stories,
        parking,
        yes_no(mainroad),
        yes_no(guestroom),
        yes_no(basement),
        yes_no(hotwaterheating),
        yes_no(airconditioning),
        yes_no(prefarea),
        furnishing_semifurnished,
        furnishing_unfurnished
    ]])

    prediction = model.predict(features)[0]

    st.success(f"### Estimated Price: ₹ {prediction:,.0f}")

    st.markdown("#### What influenced this prediction")
    st.markdown("""
    - **Area** — highest positive impact
    - **Bathrooms** — high positive impact
    - **Air conditioning** — medium positive impact
    - **Unfurnished status** — negative impact
    """)

st.markdown("---")
st.caption("Built by Kawalpreet Kaur | House Price Prediction Project")
