import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import numpy as np

# 1. Configuration de la page Web (Look Professionnel)
st.set_page_config(page_title="Gezani Cyclone Tracker | Expert System", layout="wide")

st.title("🌀 Système Expert d'Analyse Cyclonique — Cyclone Gezani")
st.write("*Développé par le Cabinet de Conseil en Ingénierie Spatiale (Antananarivo, Madagascar)*")
st.markdown("---")

# 2. Données fiables enregistrées (Vérité Terrain)
donnees_trajectoire = [
    {"heure": "04:00", "lat": -17.20, "lon": 53.50, "vent": 180, "pression": 955, "statut": "En mer - Intensification"},
    {"heure": "08:00", "lat": -17.50, "lon": 52.10, "vent": 200, "pression": 948, "statut": "Approche Océan Indien"},
    {"heure": "12:00", "lat": -17.80, "lon": 50.90, "vent": 220, "pression": 940, "statut": "Alerte Rouge Déclenchée"},
    {"heure": "16:00", "lat": -18.00, "lon": 49.90, "vent": 250, "pression": 925, "statut": "Intensification Maximale (Cat. 4)"},
    {"heure": "20:00", "lat": -18.1492, "lon": 49.4023, "vent": 210, "pression": 938, "statut": "Impact à Toamasina (Tamatave)"}
]
df = pd.DataFrame(donnees_trajectoire)

# 3. Barre latérale de contrôle pour le client international
st.sidebar.header("🎛️ Paramètres d'Analyse")
heure_selectionnee = st.sidebar.select_slider(
    "Sélectionner l'heure du relevé satellite (10 Février 2026) :",
    options=df["heure"].tolist()
)

# Extraction du point sélectionné
point_actuel = df[df["heure"] == heure_selectionnee].iloc[0]

# 4. Affichage des Indicateurs Clés (KPI Météo Professionnels)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Position de l'Œil", f"{point_actuel['lat']}°S , {point_actuel['lon']}°E")
col2.metric("Vitesse des Vents (Rafales)", f"{point_actuel['vent']} km/h")
col3.metric("Pression Centrale", f"{point_actuel['pression']} hPa")
col4.metric("Statut du Système", str(point_actuel['statut']))

# 5. Moteur Cartographique Avancé (Sans blocage de serveur externe)
st.subheader("🗺️ Cartographie Dynamique des Risques & Flux Optique")

carte = folium.Map(
    location=[point_actuel['lat'], point_actuel['lon']], 
    zoom_start=7, 
    tiles='https://{s}://{z}/{x}/{y}{r}.png',
    attr='&copy; OpenStreetMap & CARTO'
)

# Tracé de la trajectoire globale
folium.PolyLine([[p['lat'], p['lon']] for p in donnees_trajectoire], color='#ff0055', weight=3, opacity=0.6).add_to(carte)

# Affichage du Cyclone à l'instant T
folium.Marker(
    location=[point_actuel['lat'], point_actuel['lon']],
    popup=f"Position à {heure_selectionnee}",
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(carte)

# Rendu de la carte dans l'application web
st_folium(carte, width=1100, height=500)

# 6. Section de téléchargement commercial du fichier de données
st.subheader("💾 Téléchargement des Données Vectorielles (Livrable SIG)")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Télécharger le fichier CSV Commercial (Vecteurs de vent)",
    data=csv,
    file_name=f"donnees_expert_cyclone_gezani_{heure_selectionnee}.csv",
    mime="text/csv"
)
