import requests
import math

API_KEY = 'f98d2fc661fd4e06a931df27db2d1155'  # Replace with your own OpenCage Geocoder API key

def get_coordinates(postcode):
    url = f'https://api.opencagedata.com/geocode/v1/json?q={postcode}&key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['total_results'] > 0:
            result = data['results'][0]
            latitude = result['geometry']['lat']
            longitude = result['geometry']['lng']
            return latitude, longitude
    return None

def calculate_distance(postcode1, postcode2):
    coordinates1 = get_coordinates(postcode1)
    coordinates2 = get_coordinates(postcode2)

    if not coordinates1 or not coordinates2:
        return None

    # Haversine formula to calculate distance
    lat1, lon1 = coordinates1
    lat2, lon2 = coordinates2
    radius = 6371

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c

    return distance

# User input
postcode1 = input("Enter the first postcode: ")
postcode2 = input("Enter the second postcode: ")

distance = calculate_distance(postcode1, postcode2)
if distance is not None:
    print(f"The distance between {postcode1} and {postcode2} is {distance:.2f} kilometers.")
else:
    print("Error: Invalid postalcode(s). Please try again")

