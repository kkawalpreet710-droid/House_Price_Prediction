import streamlit as st
import joblib
import numpy as np

model = joblib.load('house_price_model.pkl')

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

st.markdown("""
    <style>
        body { font-family: 'Segoe UI', sans-serif; }
        .main { background-color: #ffffff; }
        
        .hero {
            text-align: center;
            padding: 2rem 1rem 1rem;
        }
        .hero h1 {
            font-size: 2.2rem;
            font-weight: 700;
            color: inherit;
            margin-bottom: 0.3rem;
        }
        .hero p {
            color: #6b7280;
            font-size: 1rem;
        }

        .section-title {
            font-size: 0.75rem;
            font-weight: 600;
            color: #9ca3af;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin: 1.5rem 0 0.75rem;
        }

        .card {
            background: #f9fafb;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1rem;
        }

        .result-box {
            background: #f0fdf4;
            border: 1px solid #bbf7d0;
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            margin-top: 1.5rem;
        }
        .result-box .label {
            font-size: 0.85rem;
            color: #16a34a;
            font-weight: 500;
            margin-bottom: 0.25rem;
        }
        .result-box .price {
            font-size: 2rem;
            font-weight: 700;
            color: #15803d;
        }

        .impact-row {
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid #f3f4f6;
            font-size: 0.9rem;
            color: #374151;
        }
        .impact-row:last-child { border-bottom: none; }
        .impact-tag {
            font-size: 0.75rem;
            padding: 2px 8px;
            border-radius: 999px;
            font-weight: 500;
        }
        .high { background: #dcfce7; color: #15803d; }
        .medium { background: #fef9c3; color: #854d0e; }
        .negative { background: #fee2e2; color: #991b1b; }

        div[data-testid="stButton"] button {
            width: 100%;
            background-color: #1a1a1a;
            color: white;
            border: none;
            padding: 0.75rem;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            margin-top: 1rem;
        }
        div[data-testid="stButton"] button:hover {
            background-color: #333333;
        }

        footer { text-align: center; color: #9ca3af; font-size: 0.8rem; margin-top: 2rem; }
    </style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
    <div class="hero">
        <h1>🏠 House Price Predictor</h1>
        <p>Fill in the property details below to get an instant price estimate</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# Section 1 - Basic Details
st.markdown('<p class="section-title">Basic Details</p>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    area = st.number_input("Area (sq ft)", min_value=500, max_value=15000, value=3000, step=100)
with col2:
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
with col3:
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

col4, col5 = st.columns(2)
with col4:
    stories = st.number_input("Stories", min_value=1, max_value=10, value=2)
with col5:
    parking = st.number_input("Parking spots", min_value=0, max_value=5, value=1)

# Section 2 - Amenities
st.markdown('<p class="section-title">Amenities</p>', unsafe_allow_html=True)
col6, col7, col8 = st.columns(3)
with col6:
    airconditioning = st.selectbox("Air conditioning", ["Yes", "No"])
with col7:
    hotwaterheating = st.selectbox("Hot water heating", ["Yes", "No"])
with col8:
    guestroom = st.selectbox("Guest room", ["Yes", "No"])

col9, col10 = st.columns(2)
with col9:
    basement = st.selectbox("Basement", ["Yes", "No"])
with col10:
    furnishingstatus = st.selectbox("Furnishing status", ["Furnished", "Semi-furnished", "Unfurnished"])

# Section 3 - Location
st.markdown('<p class="section-title">Location</p>', unsafe_allow_html=True)
col11, col12 = st.columns(2)
with col11:
    mainroad = st.selectbox("Main road access", ["Yes", "No"])
with col12:
    prefarea = st.selectbox("Preferred area", ["Yes", "No"])

st.divider()

def yes_no(val):
    return 1 if val == "Yes" else 0

furnishing_semifurnished = 1 if furnishingstatus == "Semi-furnished" else 0
furnishing_unfurnished = 1 if furnishingstatus == "Unfurnished" else 0

if st.button("Predict Price →"):
    features = np.array([[
        area, bedrooms, bathrooms, stories, parking,
        yes_no(mainroad), yes_no(guestroom), yes_no(basement),
        yes_no(hotwaterheating), yes_no(airconditioning),
        yes_no(prefarea), furnishing_semifurnished, furnishing_unfurnished
    ]])

    prediction = model.predict(features)[0]

    st.markdown(f"""
        <div class="result-box">
            <div class="label">Estimated Price</div>
            <div class="price">₹ {prediction:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<p class="section-title" style="margin-top:1.5rem">What influenced this prediction</p>', unsafe_allow_html=True)
    st.markdown("""
        <div class="impact-row"><span>Area (sq ft)</span><span class="impact-tag high">Highest impact ↑</span></div>
        <div class="impact-row"><span>Bathrooms</span><span class="impact-tag high">High impact ↑</span></div>
        <div class="impact-row"><span>Air conditioning</span><span class="impact-tag medium">Medium impact ↑</span></div>
        <div class="impact-row"><span>Unfurnished status</span><span class="impact-tag negative">Negative impact ↓</span></div>
    """, unsafe_allow_html=True)

st.markdown('<footer>Built by Kawalpreet Kaur · House Price Prediction Project</footer>', unsafe_allow_html=True)
