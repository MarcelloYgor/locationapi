import geocoder
import json
import math

def getLocation(search):
    g = geocoder.here(search,
        app_id = '',
	    app_code = '')
    return g.lat, g.lng

#/*::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::*/
#/*::  This routine calculates the distance between two points (given the     :*/
#/*::  latitude/longitude of those points). It is being used to calculate     :*/
#/*::  the distance between two locations using GeoDataSource (TM) prodducts  :*/
#/*::                                                                         :*/
#/*::  Official Web site: http://www.geodatasource.com                        :*/
#/*::                                                                         :*/
#/*::           GeoDataSource.com (C) All Rights Reserved 2015                :*/
#/*::                                                                         :*/
#/*::  Versao original em Java                                                :*/
#/*::  Traduzida de Java para Python para fins academicos                     :*/
#/*::                                 por Marcello Ygor - 08/02/2019          :*/
def distance(coord1, coord2, unit):
    theta = coord1[1] - coord2[1]
    dist = (
        math.sin(deg2rad(coord1[0])) 
        * math.sin(deg2rad(coord2[0])) 
        + math.cos(deg2rad(coord1[0])) 
        * math.cos(deg2rad(coord2[0])) 
        * math.cos(deg2rad(theta))
        )
    dist = math.acos(dist)
    dist = rad2deg(dist)
    dist = dist * 60 * 1.1515
    if unit.startswith('K'):
        dist = dist * 1.609344
    elif unit.startswith('N'):
        dist = dist * 0.8684

    return dist
#/*::                                                                         :*/
def deg2rad(deg):
    return deg * math.pi / 180
#/*::                                                                         :*/
def rad2deg(rad):
    return rad * 180 / math.pi
#/*::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::*/

searchParam1 = raw_input('Digite o primeiro local:\n')
searchParam2 = raw_input('Digite o segundo local:\n')
coord1 = getLocation(searchParam1)
coord2 = getLocation(searchParam2)
distancia = distance(coord1, coord2, 'K')
print('A distancia entre esses lugares e de %g km' % distancia)