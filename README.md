# 🇮🇳 India Pollution Pulse

**A Real-Time Air Quality Monitoring Dashboard for India**

A beautiful, interactive, and professionally designed web dashboard that visualizes live air pollution data across India. It shows real-time AQI, pollutant levels on a 3D map, and provides powerful analytical insights — all built with Streamlit and deployed on Azure.

![Dashboard Preview](https://pollutionui-hvckfzekfvfyhqcw.canadacentral-01.azurewebsites.net/)



---

## ✨ Features

- **Live 3D Pollution Map** – 3D columns showing pollution intensity across India
- **AQI Map** – Color-coded Air Quality Index (Green → Dark Red) using official CPCB standards
- **Interactive Filters** – Filter by pollutant, region, state, and top N stations
- **Real-time AQI Calculation** – Uses official CPCB breakpoints and "Worst Pollutant" method
- **Multiple Analytical Views** – Time trends, regional comparison, hourly patterns, and KPIs
- **Dark Professional Theme** – Modern cyberpunk-style UI
- **Auto Refresh** – Data refreshes automatically every 5 minutes
- **Modular & Scalable Code** – Clean component-based architecture

---

## 📁 Project Folder Structure

```bash
india-pollution-pulse/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── components/                     # Modular components (recommended structure)
    ├── __init__.py
    ├── data_loader.py              # Database connection & data fetching
    ├── aqi_utils.py                # AQI calculation & color logic
    ├── regions.py                  # Region mapping (North, South, etc.)
    ├── tab1_map.py                 # All Pollutants Map
    ├── tab2_aqi_map.py             # AQI Map
    ├── tab3_analytics.py           # Analytics & Raw Data
    ├── tab4_time_trends.py         # Time Series Trends
    ├── tab5_regional_comparison.py # Regional & State Comparison
    ├── tab6_hourly_patterns.py     # Hourly & Daily Patterns
    └── tab7_kpi_overview.py        # AQI Overview & Gauge

🛠️ Technologies Used

Technology,Purpose
Streamlit,Dashboard framework
Pydeck,3D interactive maps
Plotly,Professional charts & gauge
Pandas,Data processing
pyodbc,Azure SQL Database connectivity
Azure SQL Database,Data storage
Azure Functions,Hourly ETL pipeline
Azure Web App,Production hosting


🚀 How to Run Locally
Prerequisites

Python 3.9 or higher
Azure SQL Database connection string

Steps

Clone the repositoryBashgit clone <your-repo-url>
cd india-pollution-pulse
Create virtual environmentBashpython -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
Install dependenciesBashpip install -r requirements.txt
Set environment variableBashexport CONNECTION_STRING="DRIVER={ODBC Driver 18 for SQL Server};SERVER=...;..."
Run the dashboardBashstreamlit run app.py


🌐 Deployment on Azure Web App
The project is designed to run seamlessly on Azure App Service (Linux).
Required Azure Settings:
General Settings → Startup Command
Bashpython -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0
Application Settings (Environment Variables)

SCM_DO_BUILD_DURING_DEPLOYMENT = true
CONNECTION_STRING = Your full Azure SQL connection string

After setting these, Restart the Web App.

📊 Dashboard Tabs Overview

Tab 1: All Pollutants Map (3D columns)
Tab 2: AQI Map (color-coded)
Tab 3: Analytics & Top Polluted Stations
Tab 4: Time Series Trends
Tab 5: Regional Comparison
Tab 6: Hourly & Daily Patterns
Tab 7: AQI Overview & KPIs (Gauge Chart)


🔮 Future Enhancements (Phase 2)

Historical date range selector
Export to CSV/Excel
Push notifications for high AQI
Weather integration
Mobile-responsive UI improvements


📄 License
This project is developed as a personal / academic / portfolio project. Feel free to use it for learning purposes.

Made with ❤️ for a cleaner India
By Shramita
