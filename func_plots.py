# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:19:28 2023

@author: Ida D. Stoltenberg og Signe Barfred
"""
#Plotgrade får data ind som np.array
# Skal lave 2 plots  der outputtes i plotfanen
#"Final grades" søjle diagram med karakter på x-aksen og antal studerne på y-aksen
#"Grades per assignment" scatter plot med antal aflevering på x-aksen og karakter på y-aksen

import matplotlib.pyplot as plt
import numpy as np



def gradesPlot(grades):
   # liste over mulige karakter bruges til x-aksen
    possible_grades = [-3, 0, 2, 4, 7, 10, 12]

    # Tæller antal studerne der får hver karakter og laver det til en list, som bruges som y-akse
    y= [np.count_nonzero(grades == -3),np.count_nonzero(grades == 0), np.count_nonzero(grades == 2), np.count_nonzero(grades == 4), np.count_nonzero(grades == 7), np.count_nonzero(grades == 10), np.count_nonzero(grades == 12)]
    # Lav søjle diagram med mulige karakter på x aksen og antal studerne på y aksen
    fig, ax = plt.subplots()
    colors = list('rgbkymc') #udvalg af 7 farver - svarende til hver karakter på 7-trinsskalen for klarere visualisering
    ax.bar(possible_grades, y, color=colors)

    # Sætter titel, scalering på x-aksen
    ax.set_xlabel('Grades')
    ax.set_xticks(possible_grades)
    ax.set_ylabel('Numbers of students')
    ax.set_title('Final grades')

    # show the plot
    plt.show()
#plot_grade_distribution(grades)

##PLOT 2
#Plotgrade får data ind som np.array
# Skal lave 2 plots 
#"Final grades" søjle diagram med karakter på x-aksen og antal studerne på y-aksen
#"Grades per assignment" scatter plot med antal aflevering på x-aksen og karakter på y-aksen

    # Karakter for studerne bruges til y-aksen
    y2 = grades 
    
    # generere  random number i mellem -0.1 og 0.1 med samme antal elementer som y
    randomNumber = np.random.uniform(low=-0.1, high=0.1, size=y2.shape)
    # Om definer y, så der pludses et random nr. mellem -0.1 og 0.1 til alle elmenterne
    y2 = y2+randomNumber
    #Laver x-værdier til en liste med samme længde som antal aflevering
    x = []
    for i in range(0,len(grades[0]),1):
        x.append( i+1)
    # laver en ny defination ("result") som skal bruges som x-akse på plotter. Result laver x om til en matrise hvor den hvor hver række går frem 1 til antal afleveringer
    result = ([x]*len(grades)+ randomNumber)
    
    #Regner gennemsnittet for hver aflevering
    #Virker kun for indtastet nr, skal laves så det gælder til M - afleveringer     
    gennemsnit = []
    for i in range(len(grades[0])):
        gennemsnit.append(np.mean(grades[:,i]))
    
    # laver en liste af mulige karakter
    possible_grades = [-3, 0, 2, 4, 7, 10, 12]
    
    fig, ax = plt.subplots()
    # Laver scatter plot med antal aflevering og karakter
    ax.scatter(result, y2, s=50, alpha=0.8, marker='.', color='r' )
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
    
# grades = np.array([[2, 12, 4, 10, 7, 0, 0], 
#                           [0, 0, 12, 10, 10, 7, 0], 
#                           [0, 0, 0, 2, 10, 10, 4]])
# print(plot_grade_distribution(grades))
