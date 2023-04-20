# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:21:17 2023

@author: Ida D. Stoltenberg
"""

data = [[-4, 2, 3, -4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

def errorCheck(data):
    for row in data:
        for element in row[2:len(row)]:
            if element < -3 or element > 12:
                errors = print("Error: Grade", element, "is out of the 7-point grading scale")
    return errors

print(errorCheck(data))