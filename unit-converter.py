import streamlit as st

def convert_units(value, units_from, units_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000
    }
    
    key = f"{units_from}_{units_to}"
    
    if key in conversions:
        conversion_factor = conversions[key]
        return value * conversion_factor
    else:
        return "Conversion not supported"

st.title("Unit Converter")

# Get input values
value = st.number_input("Enter The Value:")
units_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])
units_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Perform conversion
if st.button("Convert"):
    result = convert_units(value, units_from, units_to)
    st.write(f"Converted value: {result}")
