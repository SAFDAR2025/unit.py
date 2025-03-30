# -unit_convertorapp.py
import streamlit as st
st.title("Unit Converter")

# Dictionary of conversion factors
conversion_factors = {
    "Length": {
        "Meters to Kilometers": 0.001,
        "Kilometers to Meters": 1000,
        "Miles to Kilometers": 1.60934,
        "Kilometers to Miles": 0.621371
    },
    "Weight": {
        "Grams to Kilograms": 0.001,
        "Kilograms to Grams": 1000,
        "Pounds to Kilograms": 0.453592,
        "Kilograms to Pounds": 2.20462
    },
    "Temperature": {
        "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
        "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9,
        "Celsius to Kelvin": lambda c: c + 273.15,
        "Kelvin to Celsius": lambda k: k - 273.15
    }
}

# Select conversion type
conversion_type = st.selectbox("Select conversion type", list(conversion_factors.keys()))

# Select conversion direction
conversion_option = st.selectbox("Select conversion", list(conversion_factors[conversion_type].keys()))

# Input value
value = st.number_input("Enter value:", format="%.4f")

# Perform conversion when button is clicked
if st.button("Convert"):
    conversion = conversion_factors[conversion_type][conversion_option]
    
    # For temperature conversions, conversion is a function; otherwise, it's a numeric factor.
    if callable(conversion):  
        result = conversion(value)
    else:  
        result = value * conversion
    
    st.success(f"Converted Value: {result:.4f}")
