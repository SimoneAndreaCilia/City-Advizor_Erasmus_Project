import requests

WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"

def get_city_info(city):
    """Retrieve city information from Wikipedia."""
    # Wikipedia richiede un User-Agent per non bloccare la richiesta
    headers = {
        "User-Agent": "CityAdvisor/1.0 (MyPersonalProject)"
    }
    
    params = {
        "action": "query",
        "format": "json",
        "titles": city,
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
    }
    
    # Aggiungiamo headers=headers alla richiesta
    response = requests.get(WIKIPEDIA_API_URL, params=params, headers=headers)
    
    # Controllo di sicurezza: se la risposta non è 200 (OK), non proviamo a leggere il JSON
    if response.status_code != 200:
        return "Errore nella connessione a Wikipedia."

    try:
        data = response.json()
        pages = data.get("query", {}).get("pages", {})
        # Prende il primo risultato (qualsiasi sia l'ID della pagina)
        page = next(iter(pages.values()), {})
        return page.get("extract", "No information available.")
    except Exception:
        return "Errore nella lettura dei dati."