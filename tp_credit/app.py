import pickle
from pathlib import Path
import os

import pandas as pd
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


# Load model once at startup for better performance.
MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"
with open(MODEL_PATH, "rb") as f:
    modele = pickle.load(f)


@app.route("/", methods=["GET"])
def accueil():
    return render_template("index.html")


@app.route("/api-info", methods=["GET"])
def api_info():
    return jsonify(
        {
            "message": "API credit - operationnelle",
            "routes": {
                "POST /predire": "Soumettre une demande",
                "GET /demo": "Voir un exemple",
                "GET /": "Interface web",
            },
        }
    )


@app.route("/predire", methods=["POST"])
def predire():
    donnees = request.get_json(silent=True)

    if not donnees:
        return jsonify({"erreur": "Aucune donnee recue"}), 400

    df_demande = pd.DataFrame([donnees])

    prediction = modele.predict(df_demande)[0]
    probabilites = modele.predict_proba(df_demande)[0]
    confiance = round(float(max(probabilites)) * 100, 1)

    decision = "ACCORDE" if prediction == 1 else "REFUSE"
    return jsonify({"decision": decision, "confiance": f"{confiance}%"}), 200


@app.route("/demo", methods=["GET"])
def demo():
    exemple = {
        "age": 35,
        "revenu_mensuel": 12000,
        "montant_credit_demande": 50000,
        "duree_remboursement_mois": 36,
        "nb_credits_anterieurs": 1,
        "situation_familiale": "marie",
        "type_emploi": "fonctionnaire",
    }
    return jsonify(exemple), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
