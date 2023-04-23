#!/usr/bin/env python3


from math import radians, sin, cos, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    earth_radius_km = 6371

    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)

    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return c * earth_radius_km

#0,Sao-Paulo,-23.559350,-46.557583
# 1,P1,51.813583,27.431797
# testing points
point1 = (-23.559350,-46.557583)
point2 = (51.813583,27.431797)

#2,San-Jose,9.934261,-84.079025
#3,P2,-1.514283,14.613158
point1 = (9.934261,-84.079025)
point2 = (-1.514283,14.613158)

#4,Montreal,45.501886,-73.567392
#5,P3,-53.788989,-73.571008

point1 = (45.501886,-73.567392)
point2 = (-53.788989,-73.571008)

#6,Victoria,48.421769,-123.362389
#7,P4,-39.989778,-72.517383
point1 = (48.421769,-123.362389)
point2 = (-39.989778,-72.517383)

point1 = (36.99996960996491, 89.91487913126574)
point2 = (0.0, 0.0)

distance = calculate_distance(point1[0], point1[1], point2[0], point2[1])

# print distance
print(distance)
