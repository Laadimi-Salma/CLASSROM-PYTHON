# Prototype API Credit Scoring (Banque Marocaine)

## Contexte du projet
Une banque marocaine souhaite automatiser le pre-traitement de ses demandes de credit.
Aujourd'hui, chaque dossier est analyse manuellement par un conseiller, ce qui prend du temps et manque de coherence.

## Mission
Developper un prototype d'API intelligente qui:
- Recoit les informations d'un demandeur (age, revenu, montant souhaite, situation familiale, ...)
- Applique un modele ML pour evaluer le risque
- Retourne une decision: ACCORDE ou REFUSE avec un score de confiance

## Architecture creee dans ce dossier

```text
Flask/
  app.py
  requirements.txt
  README.md
  models/
    .gitkeep
  src/
    __init__.py
    api/
      routes.py
    schemas/
      request_schema.py
    services/
      decision_service.py
    ml/
      model_loader.py
```

## Endpoints disponibles
- GET /health
- POST /api/v1/credit-decision

## Exemple de payload
```json
{
  "age": 32,
  "monthly_income": 8500,
  "requested_amount": 28000,
  "family_status": "marie"
}
```

## Reponse type
```json
{
  "decision": "ACCORDE",
  "risk_score": 0.2142,
  "confidence": 0.7858
}
```

## Prochaine etape
Completer le modele avec un vrai entrainement et brancher le fichier modele dans models/credit_risk_model.joblib.
