# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 12:01:51 2023

@author: Ida D. Stoltenberg
"""

import matplotlib.pyplot as plt
import numpy as np


grades = np.array([[2, 12, 4, 5, 0, 0, 0], 
                          [0, 0, 5, 10, 10, 5, 0], 
                          [0, 0, 0, 5, 10, 10, 5]])

def plot_grade_distribution(grades_matrix):
    # Tæller antal studerne der får hver karakter og laver det til en list, som bruges som y-akse
    y= [np.count_nonzero(grades == -3), np.count_nonzero(grades == 0), np.count_nonzero(grades == 2), np.count_nonzero(grades == 4), np.count_nonzero(grades == 7), np.count_nonzero(grades == 10), np.count_nonzero(grades == 12)]
    #x= grades[1:]
    
    #fig, ax = plt.subplots()
    #ax.bar(x, y)

    # Sætter titel, scalering på x-aksen
    #ax.set_xlabel('Karakter')
    #ax.set_ylabel('Antal studerne')
    #ax.set_title('Karakter fordeling')
    
    return y
    # show the plot
    #plt.show()
    
    print(plot_grade_distribution(grades))