import streamlit as st
import google.generativeai as genai
#AIzaSyDi_0VJSC8ICsjtHHzKAzrj9cJDQsDmhdo"
#api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key="AIzaSyDi_0VJSC8ICsjtHHzKAzrj9cJDQsDmhdo")

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Haidar Abandi")

with col2:
    st.image("images/haidar.jpg")


st.title("")

persona = """"""
st.title("Haidar's AI Bot")
user_value = st.text_input("Ask anything about me: ")
if st.button("ASK", use_container_width=400):
    prompt = persona + user_value
    response = model.generate_content(prompt)
    st.write(response.text)


st.subheader("")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Youtube Channel")
    st.write("- The Best Channel in the world")
    st.write("- 400k+ Subscribers")
    st.write("- Over 150 Free Tutorials")
    st.write("- 15 Million+ Views")

with col2:
    st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRgqVIKOZ")

st.subheader("")

st.title("My Setup")
st.image("images/setup.jpg", width=600)

st.title("My Skills")

st.slider("Programming", 0, 100, 50)
st.slider("Robotics", 0, 100, 50)
st.slider("Video Games Knowledge", 0, 100, 50)


st.subheader("")
st.title("Gallery")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/g1.jpg")

with col2:
    st.image("images/g2.jpg")

with col3:
    st.image("images/g3.jpg")

st.title("")

st.title("Contacts")

st.write("EMAIL: abandi.haidar@gmail.com")
st.write("PHONE: +966582245639")