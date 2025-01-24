import streamlit as st
import datetime

st.set_page_config(layout="wide")
st.title('Test Streamlit')

result1 = st.button("click me1!")
if result1:
    st.write('you click on 1')

result2 = st.button("click me2!", type="tertiary")
if result1 & result2:
    st.write('you click both')

st.button("Reset", type="primary")