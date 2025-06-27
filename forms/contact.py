import re

import streamlit as st
import requests

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_patttern = r"^[a-zA-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+$"
    return re.match(email_patttern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        name_2 = st.text_input("Second Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email Service is not set up please try again later.", icon="😎")
                st.stop()

            if not name:
                st.error("Please enter your firstname")
                st.stop()

            if not name_2:
                st.error("Please enter your secondname")
                st.stop()

            if not email:
                st.error("please enter a valid email")
                st.stop()

            if not is_valid_email(email):
                st.error("please provide a valid email address")
                st.stop()

            if not message:
                st.error("please provide a message")
                st.stop()

        # Prepare the Data Payload and send it to the specified webhook URL
        data = {"email": email,"name": name, "name_2": name_2, "message": message}
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
             st.success("Your Message has been sent successfully")
        else: 
             st.error("There was an error sending your message")
        
        
        
        


