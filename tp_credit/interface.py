import os

import requests
import streamlit as st

st.set_page_config(page_title="Interface Credit", page_icon="💳", layout="centered")

st.title("Interface Streamlit - Decision Credit")
st.caption("Cette interface appelle l'API Flask de scoring credit deployee sur Railway.")

api_url = st.text_input(
    "URL API Flask (Railway ou local)",
    value=os.getenv("API_URL", "http://127.0.0.1:5001"),
)

with st.form("credit_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=35, step=1)
        revenu_mensuel = st.number_input(
            "Revenu mensuel (MAD)", min_value=1000, value=12000, step=500
        )
        montant_credit_demande = st.number_input(
            "Montant demande (MAD)", min_value=1000, value=50000, step=1000
        )
        duree_remboursement_mois = st.number_input(
            "Duree (mois)", min_value=12, max_value=60, value=36, step=1
        )

    with col2:
        nb_credits_anterieurs = st.number_input(
            "Credits anterieurs", min_value=0, max_value=20, value=1, step=1
        )
        situation_familiale = st.selectbox(
            "Situation familiale", ["celibataire", "marie", "divorce"]
        )
        type_emploi = st.selectbox(
            "Type emploi",
            ["salarie_prive", "fonctionnaire", "independant", "sans_emploi"],
        )

    submit = st.form_submit_button("Predire")

if submit:
    payload = {
        "age": int(age),
        "revenu_mensuel": float(revenu_mensuel),
        "montant_credit_demande": float(montant_credit_demande),
        "duree_remboursement_mois": int(duree_remboursement_mois),
        "nb_credits_anterieurs": int(nb_credits_anterieurs),
        "situation_familiale": situation_familiale,
        "type_emploi": type_emploi,
    }

    endpoint = f"{api_url.rstrip('/')}/predire"

    try:
        response = requests.post(endpoint, json=payload, timeout=20)
        response.raise_for_status()
        data = response.json()

        decision = data.get("decision", "N/A")
        confiance = data.get("confiance", "N/A")

        if decision == "ACCORDE":
            st.success(f"Decision: {decision} | Confiance: {confiance}")
        else:
            st.error(f"Decision: {decision} | Confiance: {confiance}")

    except requests.exceptions.RequestException as exc:
        st.error(f"Erreur de connexion a l'API: {exc}")
