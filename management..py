import streamlit as st
import requests
import time
import os
from st_pages import add_indentation

st.html("""
<style>
[data-testid=stSidebar] {
        background-color: #212750;
    }
[data-testid="stSidebarContent"] {
    color: white;
    span {
        color: white;
    }
    p {
        color: white;
    }
}
</style>
""")


add_indentation()

with st.sidebar:
    defai_api_key = st.text_input("Definitive API Key", key="defai_api_key", type="password")

st.markdown("<h1 style='text-align: center; color: #212750;'>Agent Generator</h1>", unsafe_allow_html=True)
st.header("Saved Agents")
st.subheader('Enter a SessionId to delete generated Agents')

url = st.secrets["DEFAI_URL"]

session_id = st.text_input("Enter Session ID")

if session_id:
    if not defai_api_key:
        st.warning("Please enter your Definitive API Key in the sidebar.")
    else:
        #headers = {"Authorization": f"Bearer {defai_api_key}"}
        headers = {"Authorization": f"{defai_api_key}"}
        try:
            download_url = f"/api/delete/{session_id}"
            download_response = requests.get(url + download_url, headers=headers)
            download_response.raise_for_status()
            response = download_response.json()["response"]
            if response == "Complete":
                st.info("Agents Deleted")
        except requests.exceptions.RequestException as e:
            st.error(f"Error retrieving file: {str(e)}")
        except KeyError:
            st.error("Invalid response format. 'file_id' not found in the response.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
else:
    st.info("Please enter a Session ID to retrieve the file.")