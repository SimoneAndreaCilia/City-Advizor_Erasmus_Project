
def get_emergency_number(country_code):
    """
    Returns the primary emergency number for a given country code.
    Defaults to 112 (Standard for most of the world/GSM) or 911.
    """
    code = country_code.upper()
    
    # Specific Mappings
    numbers = {
        # Europe (General 112, but specific overrides if preferred)
        "GB": "999", "FR": "112", "DE": "112", "IT": "112", "ES": "112", 
        
        # North America
        "US": "911", "CA": "911", "MX": "911",
        
        # Asia
        "JP": "119", # Ambulance/Fire (110 Police) - User requested 119
        "CN": "120", # Ambulance (110 Police)
        "IN": "112",
        "KR": "119",
        "TH": "1669",
        "VN": "115",
        "ID": "118",
        
        # Oceania
        "AU": "000", "NZ": "111",
        
        # South America
        "BR": "192", "AR": "107",
        
        # Others
        "ZA": "10177", "RU": "103" 
    }
    
    return numbers.get(code, "112") # Default to 112 as it works in most countries for mobiles
