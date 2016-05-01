# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 13:47:50 2016

@author: Moon

模擬一個城市的客運流量 simulate a sim_city, there are lots of people want to take a bus
the bus always crowded during traffic hour.

"""
import random

"""
平日 72班 對開,台北 > 桃園 72班,同時 桃園 > 台北 72班

假日 61班 對開, 同上

桃園到台北,總共有十站

台北到桃園,總共有五站或六站，老師里不知道算不算
"""

bus_TyToTp = []

bus_TpToTy = []



