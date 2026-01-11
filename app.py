import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="FishPro AI",
    page_icon="🐠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. OCEAN THEME CSS & HTML (WITH TEXT VISIBILITY FIXES)
# ==========================================
st.markdown("""
    <style>
    /* --- OCEAN THEME BACKGROUND --- */
    .stApp {
        background: linear-gradient(to bottom, #E0F7FA, #E1F5FE);
    }

    /* --- GLOBAL TEXT VISIBILITY FIX --- */
    /* இது அப்ளிகேஷனில் உள்ள பொதுவான தலைப்புகள் மற்றும் லேபிள்களை கருப்பு நிறமாக்கும் */
    h1, h2, h3, p, label, .stMarkdown {
        color: #004D40 !important; /* ஒரு அடர்ந்த நிறம் */
    }
    
    /* --- SIDEBAR TEXT FIX --- */
    /* சைட்பாரில் உள்ள அனைத்து எழுத்துக்களையும் கட்டாயமாக கருப்பு நிறமாக்கும் */
    [data-testid="stSidebar"] * {
        color: #000000 !important;
    }
    /* சைட்பார் தலைப்பு மற்றும் ஐகானுக்கான ஸ்டைல் */
    [data-testid="stSidebar"] h1 {
        color: #006064 !important;
        text-align: center;
    }
    [data-testid="stSidebar"] img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    /* --- DEEP SEA NAVIGATION BAR --- */
    .navbar {
        background: linear-gradient(90deg, #0277BD, #006064);
        padding: 20px;
        margin-bottom: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0, 96, 100, 0.3);
        border-bottom: 5px solid #4DD0E1;
    }
    /* நேவிகேஷன் பார் தலைப்பு மட்டும் வெள்ளையாக இருக்கட்டும் */
    .navbar h1 {
        margin: 0;
        font-family: 'Helvetica', sans-serif;
        font-weight: 800;
        font-size: 2.8rem;
        color: #ffffff !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .navbar p {
        margin: 5px 0 0;
        font-size: 1.2rem;
        color: #E0F7FA !important;
        font-weight: 500;
    }
    
    /* --- NUCLEAR TEXT FIX FOR UPLOADER (Keep text Black) --- */
    [data-testid="stFileUploader"] {
        background-color: rgba(255, 255, 255, 0.9);
        border: 2px dashed #00BCD4;
        padding: 20px;
        border-radius: 15px;
    }
    [data-testid="stFileUploader"] div, 
    [data-testid="stFileUploader"] span, 
    [data-testid="stFileUploader"] small,
    [data-testid="stFileUploader"] label {
        color: #000000 !important;
        font-weight: 700 !important;
        -webkit-text-fill-color: #000000 !important;
    }
    
    /* --- RESULT CARD (Ocean Style) --- */
    .result-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border-left: 10px solid #00ACC1;
        box-shadow: 0 4px 15px rgba(0, 172, 193, 0.2);
        text-align: center;
        margin-bottom: 20px;
    }
    .result-label {
        color: #006064 !important;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .result-value {
        color: #0277BD !important;
        font-size: 36px;
        font-weight: 900;
        margin: 0;
    }
    
    /* --- SIDEBAR BACKGROUND --- */
    [data-testid="stSidebar"] {
        background-color: #E0F2F1;
        border-right: 1px solid #B2DFDB;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #00ACC1;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    /* Alert/Info Boxes */
    .stAlert {
        color: #000000 !important;
    }
    </style>
    
    <div class="navbar">
        <h1>🌊 FishPro AI</h1>
        <p>Smart Ocean Species Recognition System</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 3. SIDEBAR INFO
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3065/3065977.png", width=100)
    st.markdown("# Project Controls")
    st.markdown("---")
    # Using markdown for better control over text color
    st.markdown("### 📊 **Model Used:**")
    st.info("MobileNetV2")
    st.markdown("### ✅ **Accuracy:**")
    st.success("99.27%")
    st.markdown("---")
    st.markdown("### 🌊 **About:**")
    st.write("This tool uses advanced Deep Learning to identify 11 different species of fish found in the ocean and seafood markets.")

# ==========================================
# 4. LOAD MODEL
# ==========================================
MODEL_PATH = "mobilenet_fish_model.h5"

CLASS_NAMES = [
    'Animal Fish', 'Bass', 'Black Sea Sprat', 'Gilt Head Bream', 
    'Hourse Mackerel', 'Red Mullet', 'Red Sea Bream', 'Sea Bass', 
    'Shrimp', 'Striped Red Mullet', 'Trout'
]

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

# ==========================================
# 5. MAIN APP LOGIC
# ==========================================
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📤 Upload Specimen")
    
    # Instructions with clear dark text
    st.markdown("""
    <div style='background-color: #B2EBF2; padding: 15px; border-radius: 10px; border-left: 5px solid #0097A7; margin-bottom: 20px;'>
        <p style='color: #000000; font-weight:bold; font-size: 16px; margin:0;'>
            👉 Please upload a clear image of the fish (JPG or PNG format).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Browse File", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    with col1:
        st.image(image, caption='Uploaded Specimen', use_column_width=True)

    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = 100 * np.max(predictions[0])

    with col2:
        st.markdown("### 🧬 Identification Results")
        
        st.markdown(f"""
        <div class="result-card">
            <p class="result-label">Species Identified:</p>
            <p class="result-value">{predicted_class}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        st.markdown("### AI Confidence Level:")
        
        st.progress(int(confidence))
        
        if confidence > 90:
            st.success(f"**High Confidence Match: {confidence:.2f}%**")
        else:
            st.warning(f"**Moderate Confidence Match: {confidence:.2f}%**")

else:
    with col2:
        # Placeholder with clear dark text
        st.info("**👈 Please upload an image from the left panel to begin the analysis.**")
        st.image("https://cdn-icons-png.flaticon.com/512/3364/3364402.png", width=150, caption="Waiting for Input...")