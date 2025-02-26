import streamlit as st
import pint
from currency_converter import CurrencyConverter

# Unit registry
ureg = pint.UnitRegistry()
ureg.define("celsius = kelvin; offset: 273.15")  # Ensuring offset unit is handled properly

# Currency Converter
currency_converter = CurrencyConverter()

# Streamlit App UI
st.set_page_config(page_title="UniFlex Converter", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .header {
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            padding: 10px;
            color: #4C7769;
            border-radius: 8px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">🔄  Smart Unit Converter</div>', unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🌐 **UniFlex Converter**")
st.sidebar.markdown("### Select a category:")

# Category selection
categories = {
    "📏 Length": ["meter", "kilometer", "mile", "yard", "foot", "inch", "centimeter", "millimeter"],
    "⚖️ Weight": ["kilogram", "gram", "pound", "ounce", "ton", "stone"],
    "🌡️ Temperature": ["celsius", "fahrenheit", "kelvin"],
    "🚀 Speed": ["meter/second", "kilometer/hour", "mile/hour", "knot"],
    "⏳ Time": ["second", "minute", "hour", "day", "week", "month", "year"],
    "📐 Area": ["meter ** 2", "kilometer ** 2", "mile ** 2", "yard ** 2", "foot ** 2", "inch ** 2", "hectare", "acre"],
    "🛢️ Volume": ["liter", "milliliter", "gallon", "meter ** 3", "centimeter ** 3"],
    "⚡ Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt_hour", "kilowatt_hour"],
    "💾 Digital Storage": ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte"],
    "💰 Currency": None  # Currency handled separately
}

selected_category = st.sidebar.radio("", list(categories.keys()), index=0)

# Display category heading with an icon
st.markdown(f'<h3 style="color: #4C7769;">{selected_category} Converter</h3>', unsafe_allow_html=True)

# Function to handle unit conversion
def convert_units(unit_list):
    input_value = st.number_input("Enter value:", value=1.0)
    from_unit = st.selectbox("From:", unit_list, key="from_unit")
    to_unit = st.selectbox("To:", unit_list, key="to_unit")
    
    try:
        if selected_category == "🌡️ Temperature":
            # Special handling for temperature units
            result = ureg.Quantity(input_value, ureg(from_unit)).to(ureg(to_unit))
        else:
            # Regular unit conversion
            result = (input_value * ureg(from_unit)).to(to_unit)
        
        st.success(f"{input_value} {from_unit} = {result:.4f} {to_unit}")
    except Exception as e:
        st.error(f"Conversion error: {e}")

# Handling Categories
if selected_category in categories and selected_category != "💰 Currency":
    convert_units(categories[selected_category])
elif selected_category == "💰 Currency":
    currency_list = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "INR", "CNY"]
    input_value = st.number_input("Enter amount:", value=1.0)
    from_currency = st.selectbox("From:", currency_list, key="from_currency")
    to_currency = st.selectbox("To:", currency_list, key="to_currency")
    
    try:
        result = currency_converter.convert(input_value, from_currency, to_currency)
        st.success(f"{input_value} {from_currency} = {result:.2f} {to_currency}")
    except Exception as e:
        st.error(f"Currency conversion failed: {e}")

st.markdown("---")
st.markdown("Created by ❤️ Zoya Afzal using **Streamlit UV** and **Python**")









