import os
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()

st.title("PDF QA Agent")
st.write("Ask questions based on the provided PDFs.")
st.write("  - introduction to cells.")
st.write("  - introduction to metabolism - enzymes and energy.")
st.write("  - the cell cycle and mitosis.")


question = st.text_input("Enter your question:")

if st.button("Ask"):
    response = None
    try:
        if question:
            base_url = os.getenv("SERVER_URL")
            response = requests.get(f"{base_url}/answer?question={question}")
            if response.status_code == 200:
                print("response.json()", response.json())
                answer = response.json().get("answer", "")
                print('answer', answer)
                st.markdown(f'<p style="color:green;">{answer}</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="color:red;">Error occurred while processing the question.</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p style="color:red;">Please enter a question to proceed.</p>', unsafe_allow_html=True)

    except requests.exceptions.ConnectionError as ce:
        st.markdown(
            '<p style="color:red;">Connection Error: Failed to establish a connection. Please check your server configuration or try again later.</p>',
            unsafe_allow_html=True)

    except requests.exceptions.RequestException as e:
        st.markdown('<p style="color:red;">Error: Request error occurred. Please try again later.</p>',
                    unsafe_allow_html=True)

    except Exception as e:
        if response and response.status_code == 500:
            st.markdown(f'<p style="color:red;">Error occurred: {response.json().get("detail", "")}</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="color:red;">Error occurred</p>', unsafe_allow_html=True)
