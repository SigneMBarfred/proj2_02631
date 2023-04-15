# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 13:43:18 2023

@author: signe
"""
import numpy as np
#Generate grade file 
# user chooses number of students and number of grades

with (open('generatedGrades.txt','w')) as file: 

#syslist = dir(sys) #??
    for x in np.array([0,0,0]):
        file.write('{f}\t'.format(f=x))
        

