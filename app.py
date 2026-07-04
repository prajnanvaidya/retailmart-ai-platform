import streamlit as st

from components.sidebar import show_sidebar

st.set_page_config(

    page_title="RetailMart AI",

    page_icon="🛒",

    layout="wide"

)

show_sidebar()

st.title("RetailMart AI Platform")

st.write("Welcome to RetailMart AI")