import streamlit as st
import requests
import os
from dotenv import load_dotenv

# 🔁 Chargement des variables d'environnement
load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# 🎨 Configuration de l'app
st.set_page_config(page_title="Fynance AI", layout="centered")
st.title("💼 Fynance AI – Interface MVP")
st.markdown("Test de connexion au backend FastAPI déployé sur Render.")

# 🔍 Affichage de l'URL utilisée
st.markdown("**URL appelée :**")
st.code(f"{BACKEND_URL}/")

# 🔄 Bouton de test
if st.button("🔄 Tester la connexion backend"):
    with st.spinner("Connexion au backend en cours..."):
        try:
            response = requests.get(f"{BACKEND_URL}/", timeout=20)
            if response.status_code == 200:
                st.success("✅ Backend en ligne !")
                st.markdown("**🧾 Réponse JSON :**")
                st.json(response.json())
            else:
                st.warning(f"⚠️ Statut inattendu : {response.status_code}")
        except Exception as e:
            st.error(f"❌ Erreur de connexion au backend : {e}")
