import streamlit as st
import requests

"""
# Azure Container App Demo with Streamlit

This is a demo application to show:
- How to host a Streamlit-App with a Azure Function Backend in Azure Container App
- Python/Streamlit development mit GitHub Codespaces

See GitHub repo for details: https://github.com/rbrands/streamlit-azure-container-app
"""

url = "http://localhost:7071/api/GetVersion"
r = requests.get(url)
st.info("FunctionApi Version: " + r.text)