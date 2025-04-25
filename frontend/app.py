import streamlit as st
import requests
import os
from dotenv import load_dotenv

# 🔁 Chargement de la configuration .env
load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# 🎨 UI de l'app
st.set_page_config(page_title="Fynance AI", layout="centered")
st.title("💼 Fynance AI – Interface MVP")

st.markdown("Test de connexion au backend FastAPI déployé sur Render.")

# 📡 Test API backend
if st.button("🔄 Tester la connexion backend"):
    try:
        response = requests.get(f"{BACKEND_URL}/")
        if response.status_code == 200:
            st.success("✅ Backend en ligne !")
            st.json(response.json())
        else:
            st.warning(f"⚠️ Backend répondu avec le statut {response.status_code}")
    except Exception as e:
        st.error(f"❌ Erreur de connexion au backend : {e}")
