import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title('Test Streamlit')

txt = st.text_area(
    "Text to analyze",
    "management of analytics and datatechnologies "*5,
)

st.write(f"You wrote {len(txt)} characters.")
