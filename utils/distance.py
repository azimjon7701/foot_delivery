import googlemaps
from decouple import config

gmaps = googlemaps.Client(key=config('GOOGLE_API_KEY'))

def distance_matrix(origin, destination):
    try:
        response = gmaps.distance_matrix(
                    origins=origin,
                    destinations=destination
                )
        ditsance = response['rows'][0]['elements'][0]['distance']['value']
        return ditsance
    except Exception as e:
        return None


def find_distance(longitude1, latitude1, longitude2, latitude2):

    origin = (latitude1, longitude1)
    destination = (latitude2, longitude2)

    try:
        response = gmaps.distance_matrix(origins=origin, destinations=destination)
        distance = response['rows'][0]['elements'][0]['distance']['value']
        return distance
    except Exception as e:
        return None
