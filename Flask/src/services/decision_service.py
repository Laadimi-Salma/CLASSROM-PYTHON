from src.ml.model_loader import get_model


def evaluate_credit_request(payload):
    model = get_model()

    feature_vector = [
        float(payload["age"]),
        float(payload["monthly_income"]),
        float(payload["requested_amount"]),
        1.0 if payload["family_status"].lower() == "marie" else 0.0,
    ]

    risk_score = model.predict_proba([feature_vector])[0][1]
    decision = "REFUSE" if risk_score >= 0.5 else "ACCORDE"

    confidence = risk_score if decision == "REFUSE" else 1 - risk_score

    return {
        "decision": decision,
        "risk_score": round(float(risk_score), 4),
        "confidence": round(float(confidence), 4),
    }
