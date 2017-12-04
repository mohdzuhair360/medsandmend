from googlemaps import geocoding

gmaps = geocoding.Client(key = " ")
geo_code = gmaps.geocode('KLCC, Kuala Lumpur')

