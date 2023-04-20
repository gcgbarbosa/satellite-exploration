#!/usr/bin/env python3

from math import atan2, cos, sin, sqrt, radians

def calculate_angle(lat1, lon1, lat2, lon2):
    earth_radius_km = 6371
    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)

    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return c * earth_radius_km

# testing points
point1 = (0, 1) # geographic coordinates of point 1
point2 = (1, 1) # geographic coordinates of point 2

angle = calculate_angle(point1[0], point1[1], point2[0], point2[1])

# print angle
print(angle)
