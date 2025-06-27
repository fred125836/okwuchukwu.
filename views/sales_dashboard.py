import streamlit as st

tab_month, tab_category, tab_man = st.tabs(["DAILY ANALYSIS", "WEEKLY ANALYSIS", "GENERAL ANALYSIS"])

with tab_month: 
    st.title("you are welcome")
    with tab_category:
        st.title("you are not welcome")
        with tab_man:
            st.title("FOREX TRAINING")

st.markdown(
    """
    <div style="
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
        width: fit-content;
        margin: 20px auto;
        text-align: center;
    ">
        <h3 style="margin: 0;">Box with Shadow</h3>
        <p>This box has a shadow effect!</p>
    </div>
    """,
    unsafe_allow_html=True
)