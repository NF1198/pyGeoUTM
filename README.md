Universal Transverse Mercator (UTM) to Lat-Lon converter

Adapted from : http://www.rcn.montana.edu/resources/converter.aspx
Ref: http://www.uwgb.edu/dutchs/UsefulData/UTMFormulas.HTM
 
A UTM -> Lat/Long (or vice versa) converter adapted from the script used at
    http://www.uwgb.edu/dutchs/UsefulData/ConvertUTMNoOZ.HTM
 
## Usage

```python
## Point-Line Localizer (Identifies the fractional distance of a point along a line)
from pyGeoUTM import Coordinate, localize_line
line = [Coordinate(0, 0), Coordinate(5, 5), Coordinate(10, 10)]
test_point = Coordinate(6, 6)
along_line = localize_line(test_point, line)

LocalizerResult(t=1.2, d=0.0, intersection=Coordinate(x=6.0, y=6.0))

## Lat-Lon --> UTM
from pyGeoUTM import LatLonCoord
from pyGeoUTM.projections.utm import getInstance as getUTMInstance, findUTMZone
loc = LatLonCoord(35, -106)
zone = findUTMZone(loc)
utm_projection = getUTMInstance(zone)
coord = utm_projection(loc)

Coordinate(x=408746.7471660567, y=3873499.8509180606)

## UTM --> Lat-Lon
from pyGeoUTM import Coordinate
from pyGeoUTM.projections.utm import getInverseInstance as getUTMInverseInstance
coord = Coordinate(408746.75, 3873499.85)
zone = 13
utm_inv = getUTMInverseInstance(zone, False)
loc = utm_inv(coord)

LatLonCoord(lat=34.999999, lon=-105.99999996884759)
```

## Testing

```
python3 -m unittest
```

## Building

```
python3 setup.py sdist bdist_wheel
```