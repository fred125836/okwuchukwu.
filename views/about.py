import streamlit as st
from forms.contact import contact_form
from PIL import Image
import io




@st.dialog("contact me💌")
def show_contact_form():
    contact_form()


col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.page_link("views/about_the_developer.py", label=":red[**Go to About the Developer**]")
    with col2:
        st.page_link("views/chatbot.py", label="Ask our Chatbot anything")
file = Image.open("images/trader.jpg")
if file is not None:
    st.image(file)
else:
    st.write("nothing to show here")
        
import streamlit as st

# Custom CSS
st.markdown("""
    <style>
    .custom-link {
        color: #0066cc;
        font-size: 18px;
        font-weight: bold;
        text-decoration: none;
    }
    .custom-link:hover {
        color: #ff6600;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# Styled link
st.markdown('<a href="/page_2" class="custom-link">Go to Page 2</a>', unsafe_allow_html=True)

st.link_button("_go to_ our payment :blue[website]", "https://www.jmhpsoftware.com")

with st.container():
    st.badge("enejo")
    st.title("this is under st container")

# Inject custom CSS to style st.button
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #CEBA27;     /* Dodger Blue */
        color: white;                  /* Button text color */
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        font-size: 16px;
        font-weight: bold;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #1D5471;     /* Darker blue on hover */
        color: ##CEBA27;
    }
    </style>
""", unsafe_allow_html=True)

# Create the button
if st.button("Click Me"):
    show_contact_form()

st.title(":red[_colored text_]:smile:")
st.write("this code will be printed")
st.badge("highlight",color="green")

# Load image from file (you can also use BytesIO or PIL)
with open("images/krm.jpg", "rb") as img_file:
    img_bytes = img_file.read()

# Create download button
st.download_button(
    label="Download JPEG Image",
    data=img_bytes,
    file_name="okwuchukwu.jpg",
    mime="image/jpeg"
)
pen = st.color_picker("pick a color")
st.write(f"you picked {pen}")
birthday = st.date_input("enter your birthday")

if st.button("submit"):
    st.write(f" your birthday is {birthday}")


st.page_link("forms/hello.py", label="go to our hello page")
# Custom centered and colored text
st.markdown(
    """
    <h2 style='text-align: center; color: red;'>
        FREQUENTLY ASKED QUESTION AND ANSWER
    </h2>
    <p style='text-align: center; color: red; font-size:20px;'>
        What you need to know about the JMHP Software
    </p>
    """,
    unsafe_allow_html=True
)



# White box with shadow on top of blue background
bir1, bir2, bir3 = st.columns(3, gap="medium")
with bir1: 
    st.markdown(
     """
        <div style="
            width: 300px;
            height: 420px;
            padding: 20px;
            background-color: white;
            border-radius: 15px;
            box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.3);
            margin: 50px auto;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: black;
        ">
            <h3 style="margin: 0;">Hello Streamlit</h3>
            <p>This box is on a blue background with a shadow.</p>
            <p>This box is on a blue background with a shadow.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    with bir2:
        st.markdown("""
            <div style="
                width: 300px;
                height: 420px;
                padding: 20px;
                background-color: white;
                border-radius: 15px;
                box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.3);
                margin: 50px auto;
                text-align: center;
                display: flex;
                flex-direction: column;
                justify-content: center;
                color: black;
            ">
                <h3 style="margin: 0;">Hello Streamlit</h3>
                <p>This box is on a blue background with a shadow.</p>
                <p>This box is on a blue background with a shadow.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("##")
        cap = bir3.camera_input("take a photo")
        if cap is not None:
            brd = Image.open (cap)
            st.image(brd, caption="this is how you look like now", use_container_width=True)
            bir3.success("you have uploaded your emage")


with st.expander("Is JMHP Software a robot or EA that trades for me automatically?"):
    st.write(
        """
        No, JMHP Software is not a robot or Expert Advisor (EA). It does not execute trades automatically on your behalf. Instead, it is a premium trading indicator system built for TradingView, designed to help you identify high-probability trade setups, get precise entry, stop loss, and take-profit levels, and understand market sentiment and trend structure. It empowers manual traders with advanced data and signals so you can make better trading decisions. You remain in full control of placing your trades

        """
    )
with st.expander("Does JMHP Software work for Deriv Synthetic Indices?"):
    st.write(
        """
        No, JMHP Software currently works only on TradingView-supported markets, such as Forex pairs (e.g., EURUSD, GBPJPY), Cryptocurrencies (e.g., BTCUSD, ETHUSD), Commodities (e.g., XAUUSD, Crude Oil), and Indices (e.g., NASDAQ, S&P 500). Deriv Synthetic Indices are not available on TradingView, so JMHP Software cannot be applied to them. If Deriv becomes integrated with TradingView in the future, support may be considered.

        """
    )
    with bir2:
        st.empty()

st.page_link("forms/hello.py", label="Ask our Chatbot anything")

with st.expander("Enter your info"):
        name = st.text_input("What's your name?")
        age = st.number_input("Your age", min_value=0)
        if st.button("sumit"):
            st.write(f"Hello {name}, you are {age} years old.")
st.link_button("gigi", "hello.py")
    
img = st.camera_input("please upload an image")
if img is not None:
    caps = Image.open(img)
    st.success("you have uploaded")
    st.image(caps, caption="this is you right now")
    caps_bytes = io.BytesIO()
    caps.save(caps_bytes, format='PNG')
    caps_bytes.seek(0)

    # Add a download button
    st.download_button(
        label="📥 Download Image",
        data=caps_bytes,
        file_name="captured_image.png",
        mime="image/png"
    )
    st.success("you have successfully downloaded and uploaded your image")
