import streamlit as st

slider = st.slider("Select a value")
st.write(slider, "squared is", slider * slider)
