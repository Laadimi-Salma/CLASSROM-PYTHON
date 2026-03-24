from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression

_MODEL = None


def _build_fallback_model():
    # Prototype fallback model until a trained model file is added in models/.
    x = np.array(
        [
            [22, 4000, 12000, 0],
            [45, 15000, 30000, 1],
            [31, 6000, 50000, 0],
            [52, 18000, 20000, 1],
            [27, 5000, 35000, 0],
            [40, 12000, 25000, 1],
        ],
        dtype=float,
    )
    y = np.array([1, 0, 1, 0, 1, 0])

    model = LogisticRegression()
    model.fit(x, y)
    return model


def get_model():
    global _MODEL

    if _MODEL is None:
        model_path = Path(__file__).resolve().parents[2] / "models" / "credit_risk_model.joblib"
        if model_path.exists():
            import joblib

            _MODEL = joblib.load(model_path)
        else:
            _MODEL = _build_fallback_model()

    return _MODEL
