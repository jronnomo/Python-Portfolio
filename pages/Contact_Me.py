import streamlit as st
from send_email import send_email


st.header("Contact Me")


with st.form(key="contact_info"):
    user_email = st.text_input(label="Input email address", key="email")
    user_message = st.text_area("Your message", key="message")
    button = st.form_submit_button(label="Submit")
    if button:
        send_email(user_email, user_message)
        st.info("Your info was sent!")

