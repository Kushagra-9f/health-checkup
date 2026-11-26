import streamlit as st
name = st.text_input("enter your name")
age = st.number_input("enter your age")
hours of sleep = st.number_input("hours of sleep", min_value=0, max_value=24)
