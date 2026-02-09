import streamlit as st
import pandas as pd

st.title("Domain Intelligence Tool")
st.write("Welcome! Upload your dotDB file to start.")

uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    st.dataframe(df)
