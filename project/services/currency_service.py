
import requests
from flask import current_app
import os

# Simplified mapping for demonstration. Expanded based on common travel destinations.
COUNTRY_CURRENCY_MAP = {
    # Europe
    "IT": "EUR", "FR": "EUR", "DE": "EUR", "ES": "EUR", "NL": "EUR", "BE": "EUR", 
    "PT": "EUR", "IE": "EUR", "GR": "EUR", "AT": "EUR", "FI": "EUR", "EE": "EUR", 
    "LV": "EUR", "LT": "EUR", "SK": "EUR", "SI": "EUR", "CY": "EUR", "MT": "EUR",
    "LU": "EUR",
    "GB": "GBP", "CH": "CHF", "NO": "NOK", "SE": "SEK", "DK": "DKK", "PL": "PLN", 
    "CZ": "CZK", "HU": "HUF", "RO": "RON", "BG": "BGN", "HR": "EUR", "IS": "ISK",
    "TR": "TRY",
    
    # Americas
    "US": "USD", "CA": "CAD", "MX": "MXN", "BR": "BRL", "AR": "ARS", "CL": "CLP", 
    "CO": "COP", "PE": "PEN",
    
    # Asia/Pacific
    "JP": "JPY", "CN": "CNY", "IN": "INR", "AU": "AUD", "NZ": "NZD", "KR": "KRW", 
    "SG": "SGD", "HK": "HKD", "TH": "THB", "ID": "IDR", "MY": "MYR", "VN": "VND", 
    "PH": "PHP",
    
    # Middle East / Africa
    "AE": "AED", "SA": "SAR", "IL": "ILS", "ZA": "ZAR", "EG": "EGP", "MA": "MAD"
}

def get_currency_code(country_code):
    """Returns the currency code for a given ISO 2-letter country code."""
    return COUNTRY_CURRENCY_MAP.get(country_code.upper(), "USD") # Default to USD if unknown

def get_exchange_rate(target_currency):
    """
    Fetches the exchange rate from 1 EUR to target_currency.
    Uses https://v6.exchangerate-api.com
    """
    if target_currency == "EUR":
        return 1.0

    api_key = os.environ.get("EXCHANGE_RATE_API_KEY") 
    if not api_key:
        print("Warning: EXCHANGE_RATE_API_KEY not found in environment variables.")
        return None

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        if data["result"] == "success":
            rates = data["conversion_rates"]
            return rates.get(target_currency)
    except Exception as e:
        print(f"Error fetching exchange rate: {e}")
        return None
    
    return None
