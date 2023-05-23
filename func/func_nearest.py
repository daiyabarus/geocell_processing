import math


def calculate_nearest_distance(source, coords):
    min_distance = float("inf")

    for coord in coords:
        distance = calculate_distance(source, coord)
        if distance > 0 and distance < min_distance:
            min_distance = distance

    return min_distance


def calculate_distance(source, destination):
    lat1, lon1 = source
    lat2, lon2 = destination

    # Mengubah derajat ke radian
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Menghitung selisih latitude dan longitude
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Rumus haversine
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c  # Mengubah ke kilometer

    return distance
