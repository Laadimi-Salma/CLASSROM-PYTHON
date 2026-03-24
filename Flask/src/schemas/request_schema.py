REQUIRED_FIELDS = [
    "age",
    "monthly_income",
    "requested_amount",
    "family_status",
]


def validate_credit_request(payload):
    if payload is None:
        return False, ["Invalid JSON payload"]

    errors = []

    for field in REQUIRED_FIELDS:
        if field not in payload:
            errors.append(f"Missing field: {field}")

    if "age" in payload and (not isinstance(payload["age"], int) or payload["age"] <= 0):
        errors.append("Field 'age' must be a positive integer")

    if "monthly_income" in payload and (
        not isinstance(payload["monthly_income"], (int, float)) or payload["monthly_income"] <= 0
    ):
        errors.append("Field 'monthly_income' must be a positive number")

    if "requested_amount" in payload and (
        not isinstance(payload["requested_amount"], (int, float)) or payload["requested_amount"] <= 0
    ):
        errors.append("Field 'requested_amount' must be a positive number")

    if "family_status" in payload and not isinstance(payload["family_status"], str):
        errors.append("Field 'family_status' must be a string")

    return len(errors) == 0, errors
