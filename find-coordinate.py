#!/usr/bin/env python3

import math
import argparse

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



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # parser.add_argument('arg_name', help='helpful message about the argument')
    parser.add_argument('lat', type=float, help='Latitude')
    parser.add_argument('long', type=float, help='Longitude')
    parser.add_argument('d', type=float, help='distance')
    parser.add_argument('i', type=float, help='Angle')

    args = parser.parse_args()

    coordinate = calculate_destination_coordinate(args.lat, args.long, args.i, args.d)

    print(coordinate)
