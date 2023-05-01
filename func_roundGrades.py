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

def roundGrade(grades):
    gradeScale = np.array([-3,0,2,4,7,10,12]) #definerer 7-trinsskalaen
    gradeRounded = []
    grades = grades.astype(float)
    for student in grades:
        
        # ordne midtinterval oprundinger manuelt ved at gå ind og erstatte med værdien højere
        for i in range(len(student)):
          
            # udskifte midtinterval med øvre grænse
            if student[i] == 1:
                student[i] = 2
          
            # udskifte midt m øvre
            if student[i] == 3:
                student[i] = 4
            
            # udskifte mid med øvre
            if student[i] == 11:
                student[i] =12
        
        # lav dictionary og sammenhold m karakterskala øverst i funktion  
        grade = [min(gradeScale,key=lambda x:abs(x-grade)) for grade in student]
        gradeRounded.append(grade) #saml i afrundet liste

    return gradeRounded
