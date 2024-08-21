import streamlit as st
import requests

st.title("Instagram Caption Downloader")

instagram_url = st.text_input("Enter Instagram Post URL:")

if st.button("Extract Caption"):
    if instagram_url:
        try:
            # Send request to Flask endpoint
            response = requests.post("http://127.0.0.1:5000/extract", data={"instagram_url": instagram_url})
            st.write("Response Status Code:", response.status_code)  # Debugging line
            response_data = response.json()
            
            if response.status_code == 200:
                caption = response_data.get('caption', 'No caption found')
                st.success("Caption extracted successfully! You can view it below.")
                st.write(caption)
            else:
                st.error(f"Failed to extract caption: {response_data.get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter an Instagram URL.")

st.text("")
st.subheader("Extracted Caption:")
