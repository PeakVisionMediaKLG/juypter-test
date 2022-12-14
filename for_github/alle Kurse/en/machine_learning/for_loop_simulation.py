# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 09:07:03 2017

@author: bernd
"""

cities = ["Hamburg", "Berlin", "München", "Stuttgart", "Zürich"]
#cities = 42


iterator = iter(cities)
while True:
    try:
        city = next(iterator)
    except StopIteration:
        break
    print(city)