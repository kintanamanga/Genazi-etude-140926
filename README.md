# Genazi-etude-140926
Etude trajectoire et vents Genazi 
# 🌀 Satellite-Based Cyclone Dynamics & Track Forecasting System

## 📌 Project Overview
This expert system provides an advanced analysis of tropical cyclone dynamics, focusing on **inner-core convective asymmetry** and **rapid intensification (RI)** patterns. Developed as a showcase portfolio item for international consultancies, this project applies computer vision algorithms to open-source geostationary satellite data to bypass traditional physics-based numerical weather prediction (NWP) limitations.

The case study focuses on **Cyclone Gezani (February 2026)**, which underwent a severe rapid intensification phase prior to making a catastrophic landfall near **Toamasina (Tamatave), Madagascar**, with sustained gusts reaching **250 km/h**.

---

## 🛠️ Scientific Methodology & Technical Stack

Unlike archaic static vector tools, this project transitions fully into the modern cloud-geospatial ecosystem using **100% Open-Source Python architectures**:

1. **Data Acquisition:** Automatic extraction of the official "Ground Truth" track data using the international **IBTrACS (NOAA)** database.
2. **Kinematic Flow Analysis (The Alternative to DPIVsoft):** Instead of relying on legacy academic software (like MATLAB-based PIV), the core engine utilizes **OpenCV's Dense Optical Flow (Farnebäck algorithm)**. By evaluating pixel-intensity shifts in successive thermal infrared satellite bands, the algorithm computes precise local velocity matrices ($U$ and $V$ components) within the cloud structures surrounding the cyclone eye.
3. **Geospatial Projection:** Vector data is dynamically converted from pixel matrices into geographic space (Latitude/Longitude coordinates) using `pandas` and integrated into interactive maps.

---

## 🚀 Interactive Deployment
The model is decoupled from heavy local computation environments and fully deployed on the cloud. 

👉 **Access the Live Interactive Web Application:** `https://streamlit.app` *(Replace with your actual Streamlit link once deployed)*

### Key Features of the App:
* **Interactive Time-Slider:** Allows international disaster management teams to visualize wind vector evolutions hour by hour.
* **Real-Time KPI Metrics:** Continuous tracking of central pressure (hPa), core coordinates, and maximum wind speed.
* **Commercial SIG Deliverable:** Includes a direct data pipeline enabling users to download the computed vectors as a standardized `.csv` file for immediate integration into professional GIS software (ArcGIS, QGIS).

---

## 📂 Repository Structure
* `app.py`: Core Streamlit web application script including the visualization engine.
* `README.md`: Technical documentation and methodology overview.

---
**Contact & Consultancy Inquiries**
* **Lead Aerospace & Remote Sensing Consultant**
* Antananarivo, Madagascar | Available for international remote contracts
