import streamlit as st
import streamlit.components.v1 as components

# Apply dark theme custom styling with animated headings
st.markdown(
    """
    <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, black, black) !important;
            color: white !important;
        }

        /* General text styling */
        html, body, [data-testid="stAppViewContainer"] * {
            color: #E0E0E0 !important;
            font-family: 'Arial', sans-serif !important;
        }
        /* Animated heading with blue gradient */
        @keyframes colorChange {
            0% { color: #008080; }  /* Teal */
            50% { color: white; }
            100% { color: #00FFFF; }  /* Cyan */
        }
        /* Sidebar (navbar) black */
        [data-testid="stSidebar"] {
        background-color: black !important;
        color: white !important;
        border-right: 2px solid #FFD700 !important;
        }


        h1 { 
        color: #FFD700 !important; /* Gold */
        text-align: center !important;
        font-weight: bold !important;
        font-size: 40px !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        }

        h2, h3 {
            color: #56CCF2; /* Light Blue */
            text-align: center;
        }
        [data-testid="stSidebar"] {
        background-color: black !important;
        color: white !important;
        border-right: 2px solid #FFD700 !important; /* Gold border */
        }
        select {
        background-color: black !important;
        color: white !important;
        }

        .stSelectbox:hover, .stNumberInput:hover, .stTextInput:hover, .stTextArea:hover {
            border-color: #4A90E2 !important;
        }
            /* Input fields black */
        .stSelectbox, .stNumberInput, .stTextInput, .stTextArea {
            background-color: black !important;
            color: #E0E0E0 !important;
            border-radius: 8px !important;
            padding: 8px !important;
            border: 1px solid #444 !important;
            transition: all 0.3s ease-in-out !important;
        }

        /* Improve label visibility */
        .stSelectbox label, .stNumberInput label, .stTextInput label, .stTextArea label {
            color: white !important;
            font-weight: bold !important;
            font-size: 16px !important;
        }

        /* Modern button with purple gradient */
        .stButton>button { 
            background: linear-gradient(90deg, #7B1FA2, #D500F9) !important;  Deep Purple → Neon Pink 
            color: white !important; 
            font-size: 16px !important; 
            padding: 12px !important; 
            border-radius: 8px !important; 
            font-weight: bold !important;
            transition: transform 0.2s ease-in-out, background 0.3s ease-in-out !important;
            border: none !important;
        }
        .gradient-heading {
            background: linear-gradient(90deg, #7B1FA2, #D500F9);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 32px;
            font-weight: bold;
            text-align: center;
        }

        .stButton>button:hover { 
            transform: scale(1.05);
            background: linear-gradient(90deg, #D500F9, #7B1FA2) !important; /* Neon Pink → Deep Purple */
        }

        /* Center markdown content */
        .stMarkdown { 
            text-align: center !important;
        }

        /* Divider styling */
        hr {
            border: 1px solid #444 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Conversion factors for different unit types
conversion_factors = {
    "Length": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1e6,
        "Pound": 2.20462,
        "Ounce": 35.274
    },
    "Temperature": "Special",
    "Speed": {
        "Meter per second": 1,
        "Kilometer per hour": 3.6,
        "Mile per hour": 2.23694,
        "Foot per second": 3.28084
    },
    "Volume": {
        "Liter": 1,
        "Milliliter": 1000,
        "Cubic meter": 0.001,
        "Cubic centimeter": 1000,
        "Gallon": 0.264172,
        "Quart": 1.05669
    },
    "Area": {
        "Square meter": 1,
        "Square kilometer": 0.000001,
        "Square centimeter": 10000,
        "Square millimeter": 1000000,
        "Square mile": 3.861e-7,
        "Acre": 0.000247105
    }
}

def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return value  # Same unit
    else:
        return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])
st.markdown(
    """
<style>
    .gradient-title {
        background: linear-gradient(90deg, #7B1FA2, #D500F9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2rem;
        font-weight: bold;
        display: inline-block;
    }
    .blue-icon {
        color: #007bff; /* Blue color */
        font-size: 2rem;
    }
</style>

<h1><span class="blue-icon">🔄</span> <span class="gradient-title">Quick Unit Converter</span></h1>
""",
unsafe_allow_html=True
)

st.markdown("### 📏⚖️🌡️ Convert units easily with an intuitive interface")

# Dropdown for category selection
category = st.selectbox("🔹 Select Unit Category", list(conversion_factors.keys()))

# Special case for temperature
if category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
else:
    units = list(conversion_factors[category].keys())

# Input fields
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("🔻 From", units)
with col2:
    to_unit = st.selectbox("🔺 To", units)

value = st.number_input("✏️ Enter value", min_value=0.0, format="%.5f")

# Conversion
if st.button("🔄 Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    #st.success(f"✅ {value} {from_unit} = {result:.5f} {to_unit}")
    st.markdown(
    f"""
    <div style="
        background-color: #3b82f6;  /* Change to any color */
        padding: 12px;
        border-radius: 6px;
        color: white;
        font-weight: bold;
        text-align: center;
        font-size: 16px;">
        ✅ {value} {from_unit} = {result: .5f} {to_unit}
    </div>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown("---")
st.markdown("💡 Built with ❤️ using Streamlit")
