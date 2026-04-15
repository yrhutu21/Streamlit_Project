import streamlit as st
import requests

st.title("Simple Calculator (HTTP)")

num1 = st.number_input("Enter first number", value=10)
num2 = st.number_input("Enter second number", value=20)

if st.button("Calculate"):
    try:
        payload = {
            "jsonrpc": "2.0",
            "method": "add",
            "params": [num1, num2],   # IMPORTANT: list
            "id": 1
        }

        response = requests.post(
            "http://127.0.0.1:4000",   # IMPORTANT: port 4000
            json=payload
        )

        data = response.json()

        if "result" in data:
            st.success(f"Result: {data['result']}")
        else:
            st.error(f"Error: {data}")

    except Exception as e:
        st.error(f"Error: {e}")