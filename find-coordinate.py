#!/usr/bin/env python3


import math

def calculate_destination_coordinate(lat, lon, angle, distance):
    """
    Calculates the lat, lon of a point that is a distance d (in km) away from the given
    latitude and longitude at an angle of t (in degrees).
    """

    # Convert latitude and longitude to radians
    lat = math.radians(lat)
    lon = math.radians(lon)

    # Convert angle to radians
    angle = math.radians(angle)

    # Earth's radius in km
    radius = 6371.01

    # Calculate the new latitude and longitude coordinates
    new_lat = math.asin(math.sin(lat) * math.cos(distance / radius) +
                        math.cos(lat) * math.sin(distance / radius) * math.cos(angle))

    new_lon = lon + math.atan2(math.sin(angle) * math.sin(distance / radius) * math.cos(lat),
                              math.cos(distance / radius) - math.sin(lat) * math.sin(new_lat))

    # Convert back to degrees
    new_lat = math.degrees(new_lat)
    new_lon = math.degrees(new_lon)

    return (new_lat, new_lon)


calculate_destination_coordinate(37.7749, -122.4194, 45, 10)
