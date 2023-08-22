import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/profilepic.png", width=400)

with col2:
    st.title("Jerry Ronnau")
    content = """
    I'm Jerry Ronnau, a Cloud Engineer and skilled freelance developer specializing 
    in MERN stack websites and Python applications. With a passion for transforming 
    ideas into powerful digital solutions, I've crafted intricate ecommerce sites 
    featuring real-time stock updates and dynamic pricing. My expertise lies in 
    orchestrating reliable, scalable solutions using AWS and Kubernetes. I excel 
    in creating seamless user experiences by merging innovative design with robust 
    technical architecture. Let's collaborate to bring your digital vision to 
    life and empower your business.
    """
    st.write(content)

signup = """
I am committed to turning visions into digital realities that empower businesses to 
thrive without the burdens of technical intricacies. Below you can find some of 
websites and applications I've developed. Sign up below to get started!
"""
st.write(signup)

col3, col4 = st.columns(2)

df = pandas.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[:10].iterrows():
        col3.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        col4.header(row["title"])