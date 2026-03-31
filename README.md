# 🇮🇳 India Pollution Pulse

**A Real-Time Air Quality Monitoring Dashboard for India**


A beautiful, interactive, and professional web dashboard that visualizes **live air pollution data** across India using 3D maps, AQI calculations, and powerful analytics.

**Live Dashboard:** [https://pollutionui-hvckfzekfvfyhqcw.canadacentral-01.azurewebsites.net/](https://pollutionui-hvckfzekfvfyhqcw.canadacentral-01.azurewebsites.net/)

---

## ✨ Key Features

- 3D interactive pollution map of India
- Official CPCB AQI calculation with color coding
- 7 professional tabs with charts and insights
- Real-time filters (Pollutant, Region, State, Top N)
- Dark modern theme
- Auto-refresh every 5 minutes
- Fully modular & maintainable code

---

## 📁 Project Folder Structure

```bash
india-pollution-pulse/
├── app.py                          # Main Streamlit app
├── requirements.txt                # All dependencies
├── README.md                       # This file
└── components/                     # Clean modular architecture
    ├── __init__.py
    ├── data_loader.py              # Azure SQL connection
    ├── aqi_utils.py                # AQI logic & breakpoints
    ├── regions.py                  # North/South/East etc.
    ├── tab1_map.py                 # All Pollutants Map
    ├── tab2_aqi_map.py             # AQI Map
    ├── tab3_analytics.py           # Top stations + raw data
    ├── tab4_time_trends.py         # Time series
    ├── tab5_regional_comparison.py # Regional & state bars
    ├── tab6_hourly_patterns.py     # Hourly heatmap
    └── tab7_kpi_overview.py        # National AQI gauge

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
