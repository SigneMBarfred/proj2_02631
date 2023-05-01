# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:50:04 2023
@author: Ida D. Stoltenberg og Signe Barfred
"""
#FINAL GRADE
# Skal via input grades (array af karakterer) beregne endelig karakter 
# udfra givne kriterier. den endelige karakter skal ligge på 7-trinsskalaen
#Output: endelig karakter

import numpy as np
from func_roundGrades import roundGrade

def computeFinalGrades(grades):
    gradesFinal = []
    #Hvis der kun er en aflevering
    for i in range(0,len(grades),1):
        M = len(grades[i])    
        if M == 1:
            
            gradesFinal.append(grades[i][:,0])
     
        #Hvis der er flere afleveringer   
        elif M > 1 and -3 not in grades[i]:
            gradesExMin = sorted(grades[i])[1:]# Find den lavest karateker og slet den
            
            gradesFinal.append(np.mean(gradesExMin)) #lad den endelige karakter være gns af tilbageværende karakterer
        
        #Hvis studernde får -3 i en aflevering
        if -3 in grades[i] and M !=1:
            gradesFinal.append(-3) 
   
    #gradesFinal = np.array(roundGrade(gradesFinal)) #dette giver fejlmelding - relateret til lagring af dataen og dens type? rounding af final grade varetaget i main script istedet
        
    return gradesFinal

