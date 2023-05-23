import sys
from datetime import datetime
from multiprocessing import Manager, Pool

import openpyxl
from geopy.distance import geodesic


def calculate_distance(coords1, coords2):
    return geodesic(coords1, coords2).km


def find_nearest_distance(row, coords, manager):
    min_distance = float("inf")
    nearest_lc = None

    for lc, lat, lon in coords:
        if lc != row[0]:
            distance = calculate_distance((row[1], row[2]), (lat, lon))
            if distance > 0 and distance < min_distance:
                min_distance = distance
                nearest_lc = lc

    # If all distances are 0, find the nearest non-zero distance
    if min_distance == 0:
        for lc, lat, lon in coords:
            if lc != row[0]:
                distance = calculate_distance((row[1], row[2]), (lat, lon))
                if distance > 0:
                    min_distance = distance
                    nearest_lc = lc
                    break

    row[3] = min_distance
    row.append(nearest_lc)
    manager.append(row)


def process_rows(data, coords):
    with Manager() as manager:
        result = manager.list()

        pool = Pool()
        for row in data:
            pool.apply_async(find_nearest_distance, args=(row, coords, result))
        pool.close()
        pool.join()

        return list(result)
