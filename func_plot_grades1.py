# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:19:28 2023

@author: Ida D. Stoltenberg
"""

import matplotlib.pyplot as plt
import numpy as np


grades = np.array([[2, 12, 4, 5, 0, 0, 0], 
                          [0, 0, 5, 10, 10, 5, 0], 
                          [0, 0, 0, 5, 10, 10, 5]])

def plot_grade_distribution(grades_matrix):
   # liste over mulige karakter bruges til x-aksen
    possible_grades = [-3, 0, 2, 4, 7, 10, 12]

    # Tæller antal studerne der får hver karakter og laver det til en list, som bruges som y-akse
    y= [np.count_nonzero(grades == -3),np.count_nonzero(grades == 0), np.count_nonzero(grades == 2), np.count_nonzero(grades == 4), np.count_nonzero(grades == 7), np.count_nonzero(grades == 10), np.count_nonzero(grades == 12)]
    # Lav søjle diagram med mulige karakter på x aksen og antal studerne på y aksen
    fig, ax = plt.subplots()
    ax.bar(possible_grades, y)

    # Sætter titel, scalering på x-aksen
    ax.set_xlabel('Karakter')
    ax.set_xticks(possible_grades)
    ax.set_ylabel('Antal studerne')
    ax.set_title('Karakter fordeling')

    # show the plot
    plt.show()
    
   




plot_grade_distribution(grades)
