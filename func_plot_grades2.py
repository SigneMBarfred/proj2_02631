# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 12:01:51 2023

@author: Ida D. Stoltenberg
"""

import matplotlib.pyplot as plt
import numpy as np
import random

#Plotgrade får data ind som np.array
# Skal lave 2 plots 
#"Final grades" søjle diagram med karakter på x-aksen og antal studerne på y-aksen
#"Grades per assignment" scatter plot med antal aflevering på x-aksen og karakter på y-aksen


def plot_grade_distribution(grades):
    # Karakter for studerne bruges til y-aksen
    y = grades 
    
    # generere  random number i mellem -0.1 og 0.1 med samme antal elementer som y
    random = np.random.uniform(low=-0.1, high=0.1, size=y.shape)
    # Om definer y, så der pludses et random nr. mellem -0.1 og 0.1 til alle elmenterne
    y = y+random
    #Laver x-værdier til en liste med samme længde som antal aflevering
    x = []
    for i in range(0,len(grades[0]),1):
        x.append( i+1)
    # laver en ny defination ("result") som skal bruges som x-akse på plotter. Result laver x om til en matrise hvor den hvor hver række går frem 1 til antal afleveringer
    result = ([x]*len(grades)+ random)
    
    # Regner gennemsnittet for hver aflevering
    #Virker kun for indtastet nr, skal laves så det gælder til M - afleveringer     
    gennemsnit = [np.mean(grades[:,0]), np.mean(grades[:,1]), np.mean(grades[:,2]), np.mean(grades[:,3]), np.mean(grades[:,4]), np.mean(grades[:,5]), np.mean(grades[:,6])]
    
    # laver en liste af mulige karakter
    possible_grades = [-3, 0, 2, 4, 7, 10, 12]
    
    fig, ax = plt.subplots()
    # Laver scatter plot med antal aflevering og karakter
    ax.scatter(result, y, s=50, alpha=0.8, facecolors='none', edgecolors='r' )
    # Laver kurve med den gennemsnitlige karakter som funktion af afleveringerne
    plt.plot(x, gennemsnit)

    # Sætter titel, scalering på x-aksen
    ax.set_xlabel('Numbers of assignments')
    ax.set_yticks(possible_grades)
    ax.set_ylabel('Grades')
    ax.set_title('Grades per assignment')
    
    #ax.set_title('Karakter fordeling')
    

    # Visser plot
    plt.show()
    
grades = np.array([[2, 12, 4, 10, 7, 0, 0], 
                          [0, 0, 12, 10, 10, 7, 0], 
                          [0, 0, 0, 2, 10, 10, 4]])
print(plot_grade_distribution(grades))