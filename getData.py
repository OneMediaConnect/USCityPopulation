from getCounties import get_county
import json
import requests

us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}
    
# invert the dictionary
abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))


def findFIPS(city, state):
    
    county = get_county(city, state)

    with open('fips.json', 'r') as f:
        fips_data = json.load(f)

    if state in abbrev_to_us_state:
        stateConv = abbrev_to_us_state[state]
    

    for entry in fips_data:
        if entry["countyName"].lower() == county.lower() and entry["stateName"] == stateConv:
            return entry["countyFIPS"]
    

def totalHouseHoldCount(fips):
    base_url = "https://api.census.gov/data/2022/acs/acs1/profile?get=group(DP02)&ucgid=0500000US"
    call_url = base_url + fips

    response = requests.get(call_url)
    response.raise_for_status()  # Raise an exception for bad responses
    data = response.json()

    # The first row contains headers, so we'll use it to find the index of DP02_0001E
    headers = data[0]
    try:
        household_count_index = headers.index('DP02_0001E')
    except ValueError:
        return "Error: DP02_0001E not found in the response"

    # The second row contains the actual data
    if len(data) > 1:
        household_count = data[1][household_count_index]
        return int(household_count)
    else:
        return "Error: No data found in the response"