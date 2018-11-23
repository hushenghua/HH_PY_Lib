# -*- coding: utf-8 -*-
"""
处理管理地理信息相关的工具函数
Created on Fri Nov 23 14:30:44 2018

@author: hushenghua
"""

#判断一个指定的经纬坐标是否落在一个多边形区域内？
#ref: https://blog.csdn.net/bluehawksky/article/details/51669994
def IsPtInPoly(aLon, aLat, pointList):
    '''
    :param aLon: double 经度
    :param aLat: double 纬度
    :param pointList: list [(lon, lat)...] 多边形点的顺序需根据顺时针或逆时针，不能乱
    '''
    
    iSum = 0
    iCount = len(pointList)
    
    if(iCount < 3):
        return False
    
    #可以优化一下，取得经度最大最小值，纬度最大最小值。如果对应点在这几个极端点外，直接判定不在，就不用按下面挨个点计算了
    #get mix max
    min_lon = 999
    min_lat = 999    
    max_lon = -999
    max_lat = -999    
    for p in pointList:
        if p[0] < min_lon:
            min_lon = p[0]
        if p[0] > max_lon:
            max_lon = p[0]
        if p[1] < min_lat:
            min_lat = p[1]
        if p[1] > max_lat:
            max_lat = p[1]
    if (aLon < min_lon) or (aLon > max_lon) or (aLat < min_lat) or (aLat > max_lat):
        return False
        
    #对每两个连续的点进行计算判定
    for i in range(iCount):
        
        pLon1 = pointList[i][0]
        pLat1 = pointList[i][1]
        
        if(i == iCount - 1):
            
            pLon2 = pointList[0][0]
            pLat2 = pointList[0][1]
        else:
            pLon2 = pointList[i + 1][0]
            pLat2 = pointList[i + 1][1]
        
        if ((aLat >= pLat1) and (aLat < pLat2)) or ((aLat>=pLat2) and (aLat < pLat1)):
            
            if (abs(pLat1 - pLat2) > 0):
                
                pLon = pLon1 - ((pLon1 - pLon2) * (pLat1 - aLat)) / (pLat1 - pLat2);
                
                if(pLon < aLon):
                    iSum += 1
 
    if(iSum % 2 != 0):
        return True
    else:
        return False
    
'''
#测试
pointlist = [[0,0],[3,3],[6,2],[9,4],[10,5],[12,4],[12,0]]
alon = 7
alat = 2
print(IsPtInPoly(alon, alat, pointlist))
'''    


#计算两个点间的距离，考虑地球弧度
#ref: https://blog.csdn.net/u013401853/article/details/73368850
from math import sin, asin, cos, radians, fabs, sqrt
 
EARTH_RADIUS=6371           # 地球平均半径，6371km
 
def hav(theta):
    s = sin(theta / 2)
    return s * s
 
def get_distance_hav(lat0, lng0, lat1, lng1):
    "用haversine公式计算球面两点间的距离。"
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)
 
    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))
 
    return distance
 
lon1,lat1 = (22.599578, 113.973129) #深圳野生动物园(起点）
lon2,lat2 = (22.6986848, 114.3311032) #深圳坪山站 (百度地图测距：38.3km)
d2 = get_distance_hav(lon1,lat1,lon2,lat2)
print(d2)
 
lon2,lat2 = (39.9087202, 116.3974799) #北京天安门(1938.4KM)
d2 = get_distance_hav(lon1,lat1,lon2,lat2)
print(d2)
 
lon2,lat2 =(34.0522342, -118.2436849) #洛杉矶(11625.7KM)
d2 = get_distance_hav(lon1,lat1,lon2,lat2)
print(d2)

    