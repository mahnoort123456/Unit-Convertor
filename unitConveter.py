import streamlit as st

st.title("🔄 Unit Converter")
st.markdown("🧮 Converts Length, Weight and Time Instantly")
st.write("Welcome! Select a category, Enter a value and get the converted result in real-time.")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

# Correct place to take 'unit' input
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to miles", "Miles to kilometers"]) 
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])               
elif category == "Time":
    unit = st.selectbox("⏱️ Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

value = st.number_input("Enter the value to convert", format="%.4f")

if st.button("Convert"):
    try:
        result = convert_units(category, value, unit)
        if isinstance(result, (int, float)):
            st.success(f"✅ The result is: {result:.2f}")
        else:
            st.error("❌ Conversion failed. Please check your inputs.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
