import streamlit as st


st.header("Contact Me")


with st.form(key="contact_info", clear_on_submit=True):
    user_email = st.text_input(label="Input email address", key="email")
    user_message = st.text_area("Your message", key="message")
    button = st.form_submit_button(label="Submit")

