import streamlit as st
import requests
import os

# Get backend URL from environment variables on Render
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.title("FastAPI + Streamlit CRUD")

# CREATE
with st.form("add_item"):
  name = st.text_input("Item Name")
  desc = st.text_area("Description")
  if st.form_submit_button("Add Item"):
    res = requests.post(f"{BACKEND_URL}/items", json = {"name": name, "description": desc})
    st.success("Added!") if res.status_code == 200 else st.error("Error!")

# READ
if st.button("Refresh List"):
  data = requests.get(f"{BACKEND_URL}/items").json()
  for item in data:
    st.write(f"**{item['name']}**: {item['description']}")
    # DELETE
    if st.button(f"Delete {item['name']}", key = item['name']):
      requests.delete(f"{BACKEND_URL}/items/{item['name']}")
      st.rerun()

# streamlit with fastapi example codes with crud operations, which will be deployed to render.com with postgresql database


# Setting 	      Backend (FastAPI)	                            Frontend (Streamlit)
# Service Type	  Web Service	                                  Web Service
# Root Directory	backend	                                      frontend
# Build Command	  pip install -r requirements.txt	              pip install -r requirements.txt
# Start Command	  uvicorn main:app --host 0.0.0.0 --port $PORT	streamlit run app.py --server.port $PORT
# Env Vars	       N/A	                                        BACKEND_URL: (The URL of your Backend service)
