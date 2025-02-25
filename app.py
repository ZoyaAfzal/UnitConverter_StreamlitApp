import streamlit as st
import streamlit.components.v1 as components

# Apply custom styling
st.markdown(
    """
    <style>
        body { font-family: Arial, sans-serif; }
        .stButton>button { background-color: #4285F4; color: white; font-size: 16px; padding: 10px; border-radius: 5px; }
        .stSelectbox, .stNumberInput { font-size: 16px; }
        .stMarkdown { text-align: center; }
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

st.title("🔄 Unit Converter")
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
    st.success(f"✅ {value} {from_unit} = {result:.5f} {to_unit}")

# Footer
st.markdown("---")
st.markdown("💡 Built with ❤️ using Streamlit")
