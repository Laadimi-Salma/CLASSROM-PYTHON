# Atelier de Deploiement - TP Credit

## Objectif
Deployer:
- API Flask + modele ML sur Railway
- Interface Streamlit sur Streamlit Community Cloud

## 1) Architecture de deploiement
En local, tout tourne sur votre machine. En production, les deux composantes sont separees et deployeees sur des plateformes differentes.

| Composante | En local | En production |
| --- | --- | --- |
| API Flask + modele ML | http://127.0.0.1:5000 | Railway -> URL publique HTTPS |
| Interface Streamlit | http://localhost:8501 | Streamlit Community Cloud |
| Communication | requests.post("http://127.0.0.1:5000/...") | requests.post("https://votre-app.railway.app/...") |

Note locale dans ce projet: si le port 5000 est bloque par Windows, utilisez http://127.0.0.1:5001.

Principe cle: l'interface Streamlit et l'API Flask ne sont pas deployeees au meme endroit. Streamlit gere l'affichage, Railway heberge la logique IA. Les deux communiquent via HTTP, comme en local, mais avec des URLs publiques.

## Fichiers requis (deja prets)
- app.py
- train_model.py
- interface.py
- model.pkl
- requirements.txt
- Procfile

## 2) Test local avant deploiement
Dans tp_credit:

1. Entrainement modele (si besoin):
   c:/Users/lenovo/Desktop/classrom-python/.venv/Scripts/python.exe train_model.py

2. Lancer API:
   c:/Users/lenovo/Desktop/classrom-python/.venv/Scripts/python.exe app.py

3. Lancer interface Streamlit (autre terminal):
   c:/Users/lenovo/Desktop/classrom-python/.venv/Scripts/streamlit.exe run interface.py

## 3) Publier sur GitHub
Dans tp_credit:

1. git init
2. git add .
3. git commit -m "TP credit deploy ready"
4. git branch -M main
5. git remote add origin https://github.com/<votre-user>/<votre-repo>.git
6. git push -u origin main

## 4) Deployer API sur Railway
1. Creer un compte Railway et cliquer New Project.
2. Choisir Deploy from GitHub Repo.
3. Selectionner votre repo.
4. Railway detecte Python et installe requirements.txt.
5. Verifier que Start command vient du Procfile:
   web: gunicorn app:app --bind 0.0.0.0:$PORT
6. Une URL publique sera creee, par exemple:
   https://tp-credit-production.up.railway.app
7. Tester:
   - GET /health
   - GET /api-info
   - POST /predire

## 5) Deployer Streamlit sur Community Cloud
1. Aller sur https://share.streamlit.io
2. Connecter GitHub et choisir le meme repo.
3. Main file path: interface.py
4. Ajouter une variable d'environnement (ou secrets) pour API_URL:
   API_URL = https://votre-app.up.railway.app
5. Deploy.

## 6) Connecter Streamlit a Railway
Dans interface.py, le endpoint est construit automatiquement:
- {API_URL}/predire

Si API_URL est vide, fallback local:
- http://127.0.0.1:5001

## Erreurs frequentes
1. Erreur de port Railway:
   - Toujours utiliser $PORT via Gunicorn/Procfile.

2. model.pkl introuvable:
   - Verifier que model.pkl est bien versionne dans le repo.

3. 404 sur /predire:
   - Verifier que URL API pointe vers Railway et finit sans slash final.

4. CORS:
   - Non bloquant ici car Streamlit appelle l'API cote serveur via requests.

5. Build failed:
   - Verifier versions dans requirements.txt et repusher.
