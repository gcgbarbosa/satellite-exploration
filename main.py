#!/usr/bin/env python3

from sgp4.api import Satrec

s = '1 25544U 98067A   19343.69339541  .00001764  00000-0  38792-4 0  9991'
t = '2 25544  51.6439 211.2001 0007417  17.6667  85.6398 15.50103472202482'

satellite = Satrec.twoline2rv(s, t)

jd, fr = 2458827, 0.362605

e, r, v = satellite.sgp4(jd, fr)

print(r)  # True Equator Mean Equinox position (km)
# (-6102.44..., -986.33..., -2820.31...)

print(v)  # True Equator Mean Equinox velocity (km/s)
# (-1.45..., -5.52..., 5.10...)
