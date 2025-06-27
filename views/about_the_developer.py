import streamlit as st

col1, col2 = st.columns(2, gap="medium", vertical_alignment = "top")
with col1:
    st.image("images/krm.jpg",  caption="THIS IS MY REAL FACE", width=400)
    with col2:
        st.header("JUDE OKWUCHUKWU", anchor=False)


with st.expander("Enter your info"):
    name = st.text_input("What's your name?")
    age = st.number_input("Your age", min_value=0, max_value=200)
    if st.button("submit"):
        st.write(f"Hello {name}, you are {age} years old.")
    