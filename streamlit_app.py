import streamlit as st
import requests

st.title("Instagram Caption Downloader")

instagram_url = st.text_input("Enter Instagram Post URL:")

if st.button("Extract Caption"):
    if instagram_url:

        response = requests.post("https://your-flask-app-url.com/extract", data={"instagram_url": instagram_url})
        if response.status_code == 200:
            st.success("Caption extracted successfully! You can download it below.")
            st.markdown("[Download Caption](http://localhost:5000/show_caption)")
        else:
            st.error("Failed to extract caption. Please check the URL.")
    else:
        st.warning("Please enter an Instagram URL.")

st.text("")

st.subheader("Extracted Caption:")
iframe_code = """
<iframe src='http://localhost:5000/show_caption' width='100%' height='300px' frameborder='0'></iframe>
"""
st.markdown(iframe_code, unsafe_allow_html=True)
