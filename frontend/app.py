import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")  # fallback si non défini

st.title("Fynance UI")

# Ex. appel backend
if st.button("Tester API"):
    try:
        response = requests.get(f"{BACKEND_URL}/")
        st.success(f"Réponse: {response.status_code}")
        st.write(response.json())
    except Exception as e:
        st.error(f"Erreur de connexion au backend : {e}")
