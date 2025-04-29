import streamlit as st
import pandas as pd
import joblib
import requests
import io

st.set_page_config(page_title="Prédiction Prix Voiture", page_icon="🚗")

st.title("🚗 Prédiction du Prix d'une Voiture")

# URL directe du modèle depuis Google Drive
model_url = "https://drive.google.com/uc?id=1r99eYWZsVIHAn4hhSC1Qt6UxFYeWXvnf"

# Fonction pour charger le modèle depuis Drive
@st.cache_resource
def load_model_from_drive(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error("Erreur lors du chargement du modèle.")
        return None
    return joblib.load(io.BytesIO(response.content))

# Charger le modèle
model = load_model_from_drive(model_url)

if model:
    # Collecter les entrées de l'utilisateur
    brand = st.selectbox("Marque", ["Toyota", "Renault", "Peugeot", "BMW", "Audi", "Hyundai"])
    model_name = st.text_input("Modèle")
    engine_size = st.number_input("Cylindrée du moteur (en L)", min_value=0.0, step=0.1)
    fuel_type = st.selectbox("Type de carburant", ["Petrol", "Diesel", "Electric", "Hybrid"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic", "CVT"])
    mileage = st.number_input("Kilométrage", min_value=0)
    doors = st.selectbox("Nombre de portes", [2, 3, 4, 5])
    owner_count = st.selectbox("Nombre de propriétaires précédents", [0, 1, 2, 3])

    # Préparer les données utilisateur
    input_data = pd.DataFrame({
        "Brand": [brand],
        "Model": [model_name],
        "Engine_Size": [engine_size],
        "Fuel_Type": [fuel_type],
        "Transmission": [transmission],
        "Milleage": [mileage],
        "Doors": [doors],
        "Owner_count": [owner_count]
    })

    # Prédiction
    if st.button("Prédire le prix"):
        try:
            prediction = model.predict(input_data)
            st.success(f"💰 Prix estimé : {int(prediction[0]):,} DZD")
        except Exception as e:
            st.error(f"Erreur lors de la prédiction : {e}")
