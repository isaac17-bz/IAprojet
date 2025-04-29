Car Price Prediction App 🚗💰 Description du projet Ce projet permet de prédire le prix d'une voiture en fonction de ses caractéristiques, telles que la marque, le modèle, l'année de fabrication, la taille du moteur, le type de carburant, le nombre de portes, le compte de propriétaires précédents, et bien plus encore. L'application utilise un modèle de régression basé sur scikit-learn pour effectuer cette prédiction.

L'interface utilisateur a été développée avec Streamlit, une bibliothèque Python qui permet de créer facilement des applications web interactives.

Fonctionnalités principales L'utilisateur peut entrer les caractéristiques d'une voiture dans un formulaire (par exemple, marque, modèle, année, etc.).

L'application prédit automatiquement le prix de la voiture sur la base du modèle de régression.

Performance du modèle :

Le modèle utilise des données historiques pour effectuer des prédictions précises du prix des voitures.

Le modèle a été évalué avec un RMSE (Root Mean Squared Error) de 467.60 et un R² Score de 0.98.

Bibliothèques utilisées Le projet utilise plusieurs bibliothèques Python pour accomplir les tâches suivantes :

Streamlit : Création d'interfaces utilisateurs interactives pour déployer des applications web.

Pandas : Manipulation des données du dataset.

Scikit-learn : Utilisation du modèle de régression linéaire pour prédire les prix des voitures.

Joblib : Sérialisation du modèle pour le charger et l'utiliser efficacement.

Google Drive : Hébergement du modèle (.joblib) pour le télécharger dynamiquement dans l'application.

Installation et exécution Clonez ce repo sur votre machine locale.

Installez les dépendances nécessaires :

bash Copy Edit pip install -r requirements.txt Lancez l'application Streamlit :

bash Copy Edit streamlit run car_price_app.py Accédez à l'interface dans votre navigateur à l'adresse http://localhost:8501.

Remarques Le modèle de prédiction est téléchargé automatiquement depuis Google Drive à chaque démarrage de l'application, ce qui garantit qu'il est toujours à jour.

Le dataset des voitures utilisé pour entraîner le modèle est également inclus dans ce projet. Si nécessaire, il peut être hébergé sur Google Drive pour un accès facile.
