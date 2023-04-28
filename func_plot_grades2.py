# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 12:01:51 2023

@author: Ida D. Stoltenberg
"""

import matplotlib.pyplot as plt
import numpy as np
import random



def plot_grade_distribution(grades):
    # Tæller antal studerne der får hver karakter og laver det til en list, som bruges som y-akse
    #y = [np.count_nonzero(grades == -3), np.count_nonzero(grades == 0), np.count_nonzero(grades == 2), np.count_nonzero(grades == 4), np.count_nonzero(grades == 7), np.count_nonzero(grades == 10), np.count_nonzero(grades == 12)]
    y= grades
    
    #b= []
    #for b in range(0,len(grades),1):
        #b.append( b+1)
    x = []
    for i in range(0,len(grades[0]),1):
        x.append( i+1)
    
    result = [x]*len(grades)
    
    
    #Virker kun for indtastet nr, skal laves så det gælder til M - afleveringer     
    gennemsnit = [np.mean(grades[:,0]), np.mean(grades[:,1]), np.mean(grades[:,2]), np.mean(grades[:,3]), np.mean(grades[:,4]), np.mean(grades[:,5]), np.mean(grades[:,6])]
    
    possible_grades = [-3, 0, 2, 4, 7, 10, 12]
    #plt.scatter(x, y)
    fig, ax = plt.subplots()
    ax.scatter(result, y )
    plt.plot(x, gennemsnit)

    # Sætter titel, scalering på x-aksen
    ax.set_xlabel('Antal Afleveringer')
    ax.set_yticks(possible_grades)
    ax.set_ylabel('Karakter')
    #ax.set_title('Karakter fordeling')
    
    return b
    # show the plot
    plt.show()
    
grades = np.array([[2, 12, 4, 10, 7, 0, 0], 
                          [0, 0, 12, 10, 10, 7, 0], 
                          [0, 0, 0, 2, 10, 10, 4]])
print(plot_grade_distribution(grades))