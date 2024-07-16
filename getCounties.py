import requests
import time

def get_county(city, state):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"{city}, {state}, USA",
        "format": "json",
        "addressdetails": 1,
        "limit": 1
    }
    headers = {
        "User-Agent": "CityCountyLookup/1.0"
    }

    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()

        if data:
            address = data[0].get("address", {})
            county = address.get("county", "County not found")
            return county.replace(" County", "").replace(" Parish", "")
        else:
            return "No results found"

    except requests.RequestException as e:
        return f"An error occurred: {str(e)}"

    finally:
        time.sleep(1)