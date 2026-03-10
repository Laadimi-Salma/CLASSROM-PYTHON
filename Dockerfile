# Utiliser l'image Python officielle
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Télécharger les corpus nécessaires pour TextBlob
RUN python -m textblob.download_corpora

# Copier l'application
COPY sentiment_analyzer.py .

# Exposer le port Streamlit
EXPOSE 8501

# Configurer Streamlit pour accepter les connexions externes
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_HEADLESS=true

# Commande pour démarrer l'application
CMD ["streamlit", "run", "sentiment_analyzer.py", "--server.address=0.0.0.0"]
