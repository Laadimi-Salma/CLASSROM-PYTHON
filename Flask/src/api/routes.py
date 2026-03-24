from flask import Blueprint, jsonify, request

from src.schemas.request_schema import validate_credit_request
from src.services.decision_service import evaluate_credit_request

api_bp = Blueprint("api", __name__)


@api_bp.get("/health")
def health_check():
    return jsonify({"status": "ok"}), 200


@api_bp.post("/api/v1/credit-decision")
def credit_decision():
    payload = request.get_json(silent=True)

    is_valid, errors = validate_credit_request(payload)
    if not is_valid:
        return jsonify({"errors": errors}), 400

    result = evaluate_credit_request(payload)
    return jsonify(result), 200
