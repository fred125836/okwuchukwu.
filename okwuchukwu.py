import streamlit as st
from datetime import datetime

st.set_page_config(page_title="hello", layout="wide" )


            
# ---- PAGE SETUP ----
page_1 = st.Page(
    page="views/about.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True, 
)
page_2 = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
page_3 = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:", 
)
page_4 = st.Page(
    page="views/about_the_developer.py",
    title="About The Developer",
    icon=":material/keyboard:", 
)
page_5 = st.Page(
    page="forms/hello.py",
    title="hello",
    icon=":material/keyboard:", 
)

# --- NAVIGATION SETUP [WITHOUT SECTION] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page,])
     
# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(
    {
        "Info": [page_1],
        "Projects": [page_2, page_3],
        "more": [page_4, page_5]
    }
)
now = datetime.now().hour

# --- SHARED ON ALL PAGES ---
st.logo("images/web_de.jpg")
st.sidebar.text(
            """
            Made with 🧡 by Hoodricch
            You are highly welcome💥
            """
        )

with st.sidebar:
    st.write("current hour:", now)
    st.page_link("views/chatbot.py", label="Ask our Chatbot anything")


# --- RUN NAVIGATION ---
pg.run()

