import pickle
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def main():
    base_dir = Path(__file__).resolve().parent
    candidates = [
        base_dir / "Classweur1.xlsx",
        base_dir / "Classeur1.xlsx",
        base_dir.parent / "Flask" / "Classweur1.xlsx",
        base_dir.parent / "Flask" / "Classeur1.xlsx",
    ]

    excel_path = next((p for p in candidates if p.exists()), None)
    if excel_path is not None:
        df = pd.read_excel(excel_path)
        print(f"Dataset charge depuis: {excel_path}")
    else:
        csv_path = base_dir / "credit_dataset.csv"
        if not csv_path.exists():
            raise FileNotFoundError(
                "Aucun dataset trouve. Placez Classweur1.xlsx/Classeur1.xlsx ou credit_dataset.csv."
            )
        df = pd.read_csv(csv_path)
        print(f"Dataset charge depuis: {csv_path}")

    # X = features d'entree, y = cible a predire.
    x = df.drop(columns=["decision"])
    y = df["decision"]

    # 80% entrainement, 20% test.
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    colonnes_num = [
        "age",
        "revenu_mensuel",
        "montant_credit_demande",
        "duree_remboursement_mois",
        "nb_credits_anterieurs",
    ]
    colonnes_cat = ["situation_familiale", "type_emploi"]

    preprocesseur = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), colonnes_num),
            ("cat", OneHotEncoder(handle_unknown="ignore"), colonnes_cat),
        ]
    )

    pipeline = Pipeline(
        steps=[
            ("preprocesseur", preprocesseur),
            ("modele", RandomForestClassifier(n_estimators=100, random_state=42)),
        ]
    )

    pipeline.fit(x_train, y_train)
    y_pred = pipeline.predict(x_test)

    print(f"Accuracy : {accuracy_score(y_test, y_pred):.2%}")
    print(classification_report(y_test, y_pred, target_names=["Refuse", "Accorde"]))

    with open("model.pkl", "wb") as f:
        pickle.dump(pipeline, f)

    print("Modele sauvegarde dans model.pkl")


if __name__ == "__main__":
    main()
