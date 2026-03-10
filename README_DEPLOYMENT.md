# 🚀 Guide de Déploiement - Sentiment Analyzer

Ce guide vous explique comment déployer l'application Sentiment Analyzer sur **3 plateformes différentes** pour la rendre accessible depuis n'importe où dans le monde.

---

## 📋 Table des matières

1. [Streamlit Cloud (Gratuit & Rapide)](#1-streamlit-cloud)
2. [Render git push -u origin main(Gratuit avec limitations)](#2-render)
3. [Docker en Local (Accessible en réseau)](#3-docker-en-local)

---

## 1. ☁️ Streamlit Cloud

### Avantages

- ✅ **100% Gratuit**
- ✅ Déploiement en 2 minutes
- ✅ HTTPS automatique
- ✅ Accessible mondialement

### Instructions

#### Étape 1: Préparer votre dépôt GitHub

```bash
# Initialiser Git (si pas déjà fait)
git init

# Ajouter tous les fichiers
git add .

# Faire un commit
git commit -m "Initial commit - Sentiment Analyzer"

# Créer un dépôt sur GitHub et le lier
git remote add origin https://github.com/VOTRE-USERNAME/sentiment-analyzer.git
git branch -M main
git push -u origin main
```

#### Étape 2: Déployer sur Streamlit Cloud

1. Allez sur [share.streamlit.io](https://share.streamlit.io)
2. Connectez-vous avec GitHub
3. Cliquez sur **"New app"**
4. Sélectionnez:
   - **Repository**: votre dépôt GitHub
   - **Branch**: main
   - **Main file path**: sentiment_analyzer.py
5. Cliquez sur **"Deploy!"**

#### Étape 3: Accéder à votre application

Votre app sera accessible à une URL comme:

```
https://votre-app-sentiment-analyzer.streamlit.app
```

---

## 2. 🎨 Render

### Avantages

- ✅ Gratuit (avec 750h/mois)
- ✅ Déploiement automatique depuis GitHub
- ✅ HTTPS inclus

### Instructions

#### Étape 1: Préparer votre dépôt GitHub

(Même procédure que Streamlit Cloud ci-dessus)

#### Étape 2: Déployer sur Render

1. Allez sur [render.com](https://render.com)
2. Créez un compte et connectez GitHub
3. Cliquez sur **"New +"** → **"Web Service"**
4. Sélectionnez votre dépôt
5. Configurez:
   - **Name**: sentiment-analyzer
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run sentiment_analyzer.py --server.port=$PORT --server.address=0.0.0.0`
6. Cliquez sur **"Create Web Service"**

#### Étape 3: Accéder à votre application

URL fournie par Render:

```
https://sentiment-analyzer-xxxx.onrender.com
```

⚠️ **Note**: Sur le plan gratuit, l'app peut prendre 30-60 secondes à démarrer si inactive.

---

## 3. 🐳 Docker en Local (Accessible en réseau)

### Avantages

- ✅ Contrôle total
- ✅ Fonctionne offline
- ✅ Accessible sur votre réseau local
- ⚠️ Nécessite Docker installé

### Prérequis

Installer Docker Desktop: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

### Option A: Docker Compose (Recommandé)

```bash
# Construire et démarrer l'application
docker-compose up -d

# Vérifier que le conteneur fonctionne
docker-compose ps

# Voir les logs
docker-compose logs -f

# Arrêter l'application
docker-compose down
```

### Option B: Docker classique

```bash
# Construire l'image
docker build -t sentiment-analyzer .

# Lancer le conteneur
docker run -d -p 8501:8501 --name sentiment-app sentiment-analyzer

# Vérifier le statut
docker ps

# Voir les logs
docker logs -f sentiment-app

# Arrêter le conteneur
docker stop sentiment-app

# Supprimer le conteneur
docker rm sentiment-app
```

### Accéder à l'application

#### Sur votre machine locale:

```
http://localhost:8501
```

#### Depuis d'autres appareils sur votre réseau:

1. Trouvez votre adresse IP locale:

   ```powershell
   ipconfig
   ```

   Cherchez "IPv4 Address" (ex: 192.168.1.100)

2. Accédez depuis n'importe quel appareil sur le même réseau:
   ```
   http://192.168.1.100:8501
   ```

### Rendre accessible sur Internet (Avancé)

Pour rendre votre application Docker accessible depuis Internet, vous avez plusieurs options:

#### Option 1: Ngrok (Gratuit & Simple)

```bash
# Installer ngrok: https://ngrok.com/download

# Exposer le port 8501
ngrok http 8501
```

Vous obtiendrez une URL publique temporaire comme: `https://xxxx-xx-xx-xx-xx.ngrok.io`

#### Option 2: Configuration du routeur (Port Forwarding)

1. Accédez à l'interface de votre routeur (généralement 192.168.1.1)
2. Configurez le port forwarding:
   - Port externe: 8501
   - Port interne: 8501
   - IP locale: votre adresse IP locale
3. Trouvez votre IP publique sur [whatismyip.com](https://whatismyip.com)
4. Accédez via: `http://VOTRE-IP-PUBLIQUE:8501`

⚠️ **Attention**: Exposer directement votre application peut présenter des risques de sécurité. Utilisez un VPN ou un reverse proxy pour plus de sécurité.

---

## 📊 Comparaison des plateformes

| Critère                 | Streamlit Cloud | Render              | Docker Local        |
| ----------------------- | --------------- | ------------------- | ------------------- |
| **Coût**                | Gratuit         | Gratuit (limité)    | Gratuit             |
| **Facilité**            | ⭐⭐⭐⭐⭐      | ⭐⭐⭐⭐            | ⭐⭐⭐              |
| **Vitesse déploiement** | 2 min           | 5 min               | 5 min               |
| **Accessible Internet** | ✅ Oui          | ✅ Oui              | ⚠️ Nécessite config |
| **HTTPS**               | ✅ Oui          | ✅ Oui              | ❌ Non (par défaut) |
| **Temps démarrage**     | Instantané      | 30-60s (si inactif) | Instantané          |
| **Resources**           | Limitées        | 512 MB RAM          | Selon votre machine |

---

## 🎯 Recommandation

### Pour partager rapidement:

**→ Utilisez Streamlit Cloud** (le plus simple et rapide)

### Pour un projet professionnel:

**→ Utilisez Render** (avec plan payant pour performances)

### Pour développement/tests:

**→ Utilisez Docker en local**

---

## 🔧 Maintenance

### Mettre à jour l'application

#### Streamlit Cloud / Render:

```bash
git add .
git commit -m "Update app"
git push
```

Le déploiement se fait automatiquement!

#### Docker:

```bash
# Reconstruire l'image
docker-compose down
docker-compose up -d --build
```

---

## 🆘 Dépannage

### Streamlit Cloud

- **Erreur de déploiement**: Vérifiez que `requirements.txt` est bien présent
- **App crash**: Consultez les logs dans le dashboard Streamlit Cloud

### Render

- **App lente**: Normal sur le plan gratuit, upgrade pour de meilleures performances
- **Build failed**: Vérifiez les commandes de build et start

### Docker

- **Port déjà utilisé**: Changez le port dans `docker-compose.yml` (ex: "8502:8501")
- **Conteneur ne démarre pas**: Vérifiez les logs avec `docker logs sentiment-app`

---

## 📝 Fichiers créés

- ✅ `requirements.txt` - Dépendances Python
- ✅ `Dockerfile` - Configuration Docker
- ✅ `docker-compose.yml` - Orchestration Docker
- ✅ `.dockerignore` - Fichiers à exclure de Docker

---

## 🌟 Prochaines étapes

1. **Personnalisation**: Modifiez l'app selon vos besoins
2. **Analytics**: Ajoutez Google Analytics pour suivre les utilisateurs
3. **Base de données**: Stockez les analyses dans une DB
4. **API**: Créez une API REST pour l'intégration
5. **Tests**: Ajoutez des tests unitaires

---

**Bon déploiement! 🚀**
