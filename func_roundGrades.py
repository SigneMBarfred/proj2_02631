# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:28:21 2023

@author: signe & ida
for: project 2 - grades in 02631 F23
"""
##
#ROUNDING
#tager datafilens karakterkolonner som input og beregner en afrundet karakter fra 7-trins skalaen for hver talværdi
##

import numpy as np
#TESTRELEVANT GENERERING AF MATRIX - slettes når programmet er klar
M = int(input("Please input number of columns in the matrix you want to generate:    "))
N = int(input("Please input number of rows:    "))
grades = np.random.uniform(-3,12,(N,M))
#SLUT PÅ KODE TIL RANDOM KARAKTER

#grades = np.array([[11,2,3,6,7],[2,3,4,6,1]]) ## test af midt-intervalværdier

def roundGrade(grades):
    gradeScale = np.array([-3,0,2,4,7,10,12]) #definerer 7-trinsskalaen
    gradeRounded = []
    
    for student in grades:
        
        # ordne midtinterval oprundinger manuelt ved at gå ind og erstatte med værdien højere
        for i in range(len(student)):
          
            # replace mid interval with upper
            if student[i] == 1:
                student[i] = 2
          
            # replace 3 w 4
            if student[i] == 3:
                student[i] = 4
            
            # replace 11 w 12
            if student[i] == 11:
                student[i] =12
        
        # lav dictionary og sammenhold m karakterskala øverst i funktion  
        grade = [min(gradeScale,key=lambda x:abs(x-grade)) for grade in student]
        gradeRounded.append(grade) #saml i afrundet liste

    return gradeRounded

print(roundGrade(grades))

#roundGrade(grades)