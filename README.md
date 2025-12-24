# City Advizor 🌍

**City Advizor** is a modern web application built with **Flask** that allows users to discover detailed information about any city in the world. It provides real-time weather data, an interactive map, and a guide to top tourist attractions.

> 🇪🇺 Developed during the **Erasmus+ 2024/2025** program in **Sofia, Bulgaria 🇧🇬**, in collaboration with an international team of students.

## ✨ Key Features

*   **🔍 Universal City Search**: Find information on any global city.
*   **weather Real-Time Weather**:
    *   Clear display of temperature, weather conditions, humidity, wind, and pressure.
    *   Data provided by *OpenWeatherMap*.
*   **🏛️ Top Attractions**:
    *   Discover popular points of interest (museums, parks, monuments) within 5km of the city center.
    *   Synthesized descriptions and ratings.
    *   Powered by *Geoapify*.
*   **🗺️ Interactive Map**: Explore the city with a dynamic map based on *Leaflet* and *OpenStreetMap*.
*   **👤 User Area**:
    *   Secure Registration and Login.
    *   **Favorites**: Save your beloved cities for quick access.
    *   **History**: Keep track of your recent searches.

## 🛠️ Technology Stack

*   **Backend**: Python, Flask, Flask-SQLAlchemy, Flask-Login.
*   **Frontend**: HTML5, CSS3 (Modern, Responsive Design), JavaScript (Vanilla).
*   **Database**: SQLite.
*   **External APIs**:
    *   OpenWeatherMap (Weather)
    *   Geoapify (Attractions)
    *   OpenStreetMap (Maps)

## 🚀 Installation and Usage

Follow these steps to run the project locally:

1.  **Clone the repository**:
    ```bash
    git clone <your-repository-url>
    cd CITY-Advizor
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Keys**:
    Create a `.env` file in the main folder (where `run.py` is located) and insert your keys. You can use the `.env.example` file as a reference or copy this template:
    ```env
    SECRET_KEY=your_random_secret_key
    OPENWEATHER_API_KEY=your_openweather_key
    GOOGLE_PLACES_API_KEY=your_google_key  # (Optional/Legacy)
    Geoapify_API_KEY=your_geoapify_key
    DATABASE_URL=sqlite:///city_advisor.db
    ```

5.  **Run the application**:
    ```bash
    python run.py
    ```

6.  Open your browser at `http://127.0.0.1:5000`.

## 🛡️ Security

This project uses `python-dotenv` to manage sensitive credentials. Always ensure that the `.env` file is included in your `.gitignore` (as already configured) to avoid publishing your API Keys.

---
&copy; 2024 City Advizor. All rights reserved.
