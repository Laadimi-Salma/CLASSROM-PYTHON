# 😊 Text Sentiment Analyzer

Une application web interactive pour analyser le sentiment des textes en utilisant Streamlit et TextBlob.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)

## 🌟 Fonctionnalités

- ✨ **Analyse de sentiment** en temps réel
- 📊 **Score de polarité** (-1 à +1)
- 🎯 **Score de subjectivité** (0 à 1)
- 📈 **Visualisations** interactives
- 🎨 Interface utilisateur **moderne et intuitive**

## 🚀 Démo

L'application analyse n'importe quel texte et détermine:

- Si le sentiment est positif, négatif ou neutre
- Le degré de subjectivité (opinion vs fait)
- Des visualisations graphiques des scores

## 💻 Installation Locale

### Prérequis

- Python 3.10 ou supérieur

### Installation

```bash
# Cloner le dépôt
git clone https://github.com/VOTRE-USERNAME/sentiment-analyzer.git
cd sentiment-analyzer

# Créer un environnement virtuel
python -m venv .venv

# Activer l'environnement virtuel
# Sur Windows:
.venv\Scripts\activate
# Sur Linux/Mac:
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run sentiment_analyzer.py
```

L'application sera accessible sur http://localhost:8501

## 🌐 Déploiement

Cette application peut être déployée sur plusieurs plateformes. Consultez [README_DEPLOYMENT.md](README_DEPLOYMENT.md) pour des instructions détaillées sur:

- ☁️ **Streamlit Cloud** (Gratuit, déploiement en 2 minutes)
- 🎨 **Render** (Gratuit avec limitations)
- 🐳 **Docker** (Local ou serveur)

## 📦 Technologies Utilisées

- **[Streamlit](https://streamlit.io/)** - Framework pour applications web en Python
- **[TextBlob](https://textblob.readthedocs.io/)** - Bibliothèque de traitement du langage naturel
- **Python 3.10** - Langage de programmation

## 📖 Utilisation

1. Entrez votre texte dans la zone de texte
2. Cliquez sur "Analyze Sentiment"
3. Consultez les résultats:
   - Catégorie de sentiment (Positif/Négatif/Neutre)
   - Score de polarité
   - Score de subjectivité
   - Visualisations graphiques

## 🤝 Contribution

Les contributions sont les bienvenues! N'hésitez pas à:

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est libre d'utilisation pour des fins éducatives et personnelles.

## 👤 Auteur

Votre Nom - [@votre-username](https://github.com/votre-username)

## 🙏 Remerciements

- Streamlit pour le framework incroyable
- TextBlob pour l'analyse de sentiment
- La communauté open source

---

**Profitez de l'analyse de sentiment! 🎉**
