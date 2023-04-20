# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:28:21 2023

@author: signe & ida
for: project 2 - grades in 02631 F23
"""

#ROUNDING
#tager datafilens karakterkolonner som input og beregner en afrundet karakter fra 7-trins skalaen for hver talværdi
# import bisect
# from decimal import localcontext, Decimal, ROUND_HALF_UP

#TESTRELEVANT GENERERING AF MATRIX
import numpy as np
M = int(input("Please input number of columns in the matrix you want to generate:    "))
N = int(input("Please input number of rows:    "))
grades = np.random.uniform(-3,12,(N,M))
#SLUT PÅ KODE TIL RANDOM KARAKTER

def roundGrade(grades):
    
    gradeScale = np.array([-3,0,2,4,7,10,12]) #definerer 7-trinsskalaen
    gradeRounded = []

    for student in grades:

            #grade = bisect.bisect_left(gradeScale,grade)
            grade = [min(gradeScale,key=lambda x:abs(x-grade)) for grade in student]
            gradeRounded.append(grade)


    return gradeRounded

print(roundGrade(grades))

#have styr på grænsetilfælde ift afrunde eks 1 og 11
#print(min(gradeScale,key=lambda x:abs(x-11)))