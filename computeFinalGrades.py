# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:50:04 2023

@author: Ida D. Stoltenberg
"""
import numpy as np

Grades = [["s18", "John", 8, 5], ["s13", "g", 4, 5], ["s24", "k", 13, 5], ["s17", "a", 4, 3]]

def computeFinalGrades(Grades):
    #Hvis der kun er en aflevering
    M= len(Grades[0])    
    if M == 3:
        gradesFinal= np.array(Grades)[:,2]
     
    #Hvis der er flere afleveringer   
    # Find den lavest karateker og slet den
    #min_value= min(Grades[0])
    elif len(Grades) > 3:
        gradesFinal = M-3
    
    #Hvis studernde får -3 i en aflevering
    for row in Grades:
        for element in row[2:len(row)]:
            if element == -3: 
                gradesFinal= -3  
    
    return gradesFinal

print(computeFinalGrades(Grades))


# Hvor vil det se ud hvis nogle aflever 1 aflevering og andre flere? 


