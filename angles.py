#!/usr/bin/env python3

import math

def calculate_bearing(lat1, lon1, lat2, lon2):
    """
    Calculate the bearing between two geographic coordinates.
    Returns the angle in degrees, where 0 degrees is due north.
    """
    # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Calculate the difference between the two longitudes
    dlon = lon2 - lon1

    # Calculate the three-dimensional distance between the two points
    y = math.sin(dlon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    distance = math.atan2(y, x)

    # Convert the distance to bearing and normalize to 0-360 degrees
    bearing = (math.degrees(distance) + 360) % 360

    return bearing


def calculate_azimuth(lat1, long1, lat2, long2):
    # convert decimal degrees to radians
    lat1, long1, lat2, long2 = map(math.radians, [lat1, long1, lat2, long2])

    d_long = long2 - long1

    y = math.sin(d_long) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - \
        math.sin(lat1) * math.cos(lat2) * math.cos(d_long)

    azimuth = (math.atan2(y, x) + 2*math.pi) % (2*math.pi)

    # convert radians to degrees
    azimuth = math.degrees(azimuth)

    return azimuth


def orbital_inclination(lat1, lon1, lat2, lon2):
    # convert latitudes and longitudes to radians
    lat1, lon1 = math.radians(lat1), math.radians(lon1)
    lat2, lon2 = math.radians(lat2), math.radians(lon2)

    # calculate dot product of two points in Cartesian coordinates
    x1 = math.cos(lat1) * math.cos(lon1)
    y1 = math.cos(lat1) * math.sin(lon1)
    z1 = math.sin(lat1)

    x2 = math.cos(lat2) * math.cos(lon2)
    y2 = math.cos(lat2) * math.sin(lon2)
    z2 = math.sin(lat2)

    dot = x1 * x2 + y1 * y2 + z1 * z2

    # calculate magnitude of two points
    mag1 = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    mag2 = math.sqrt(x2 ** 2 + y2 ** 2 + z2 ** 2)

    # calculate angle between two points
    angle = math.acos(dot / (mag1 * mag2))

    # convert angle from radians to degrees
    inclination = math.degrees(angle)

    return inclination

#2,San-Jose,9.934261,-84.079025
#3,P2,-1.514283,14.613158
point1 = (9.934261,-84.079025)
point2 = (-1.514283,14.613158)


point1 = (45.501886,-73.567392)
point2 = (-53.788989,-73.571008)


print("azimuth: ", calculate_azimuth(point1[0], point1[1], point2[0], point2[1]))
print("bearing: ", calculate_bearing(point1[0], point1[1], point2[0], point2[1]))
print("orbital: ", orbital_inclination(point1[0], point1[1], point2[0], point2[1]))
