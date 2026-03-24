import os

import requests

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:5000")

# Cas 1 : profil susceptible d'etre accorde
demande_1 = {
    "age": 38,
    "revenu_mensuel": 18000,
    "montant_credit_demande": 40000,
    "duree_remboursement_mois": 24,
    "nb_credits_anterieurs": 0,
    "situation_familiale": "marie",
    "type_emploi": "fonctionnaire",
}

reponse = requests.post(f"{BASE_URL}/predire", json=demande_1)
data_1 = reponse.json()
print(
    f"Demande 1 -> Decision: {data_1.get('decision', 'N/A')} | "
    f"Confiance: {data_1.get('confiance', 'N/A')}"
)

# Cas 2 : profil susceptible d'etre refuse
demande_2 = {
    "age": 24,
    "revenu_mensuel": 4000,
    "montant_credit_demande": 150000,
    "duree_remboursement_mois": 60,
    "nb_credits_anterieurs": 3,
    "situation_familiale": "celibataire",
    "type_emploi": "sans_emploi",
}

reponse2 = requests.post(f"{BASE_URL}/predire", json=demande_2)
data_2 = reponse2.json()
print(
    f"Demande 2 -> Decision: {data_2.get('decision', 'N/A')} | "
    f"Confiance: {data_2.get('confiance', 'N/A')}"
)
