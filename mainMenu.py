# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 13:30:54 2023

@author: signe og ida
"""

##Main script! 


# kalder alle funktionerne
# kan vise de forskellige muligheder
# kan indlæse brugerens fil og give passende fejlmeldinger
# kan plotte
# kan vise endelige karakterer
# kan afslutte
#kodeastruktur baseret på hovedmenuen vi lavede til proj1 (grp 91)

from func_dataLoad import dataLoad
from func_errorCheck import errorCheck
from func_finalGrade import computeFinalGrades
from func_roundGrades import roundGrade
from func_plots import gradesPlot
import os 
import numpy as np

#Definer variable til at farve tekst grøn i interfacet
CSTART = '\x1b[6;30;42m'
CEND = '\x1b[0m'

#Definer variable til at farve tekst grøn i interfacet
ESTART = '\x1b[6;31;40m'
EEND = '\x1b[0m'

print("Hello! Welcome - this is a programme to read, compute and illustrate grades for a set of students")

#hovedmenu
def menu():
    
    print("MAIN MENU  - These are your options:")
    print("1 - Load data")
    print("2 - Error check loaded data")
    print("3 - Generate plots")
    print("4 - Display list of final grades")
    print("5 - Exit programme")
    
menu() #kør funktionen

#brugerinput
while True:
    
    try:
        option = int(input("Please choose an option:"))
        break #videre når rigtig type input
    
    except ValueError: #loop når forkert type input
        raise ValueError(ESTART + "Invalid option chosen. Please input a number from the menu (no.1-5)"+ EEND)
    
loadData = False #vi holder øje med om data er indlæst

while option != 5: #så længe man ikke har valgt at afslutte programmet skal nedenstående køres.
    
    if option == 1: #load data
        print(CSTART + "1 - LOAD DATA CHOSEN"+CEND)
        while True:
            filename = input("Please enter filename for your data or enter '5' to exit sub-menu:") #fil skal ligge i samme mappe som kode
            
            if filename == '5':
                break
            
            elif not os.path.exists(filename): #led efter fil i mappen via os
                print(ESTART + "Not a valid filename. Should look like a 'YourName.csv'. Remember to check that the file you want loaded is placed in the same folder as this programme."+EEND)
            
            else:
                loadData = True # data er indlæst
                data = np.array([dataLoad(filename)[0]])
                data = data[0,...] #der bliver loaded en 3rd dimension m udstrækning 0 - den fjerner vi lige
                print(CSTART+'\n >>Returning to main menu.'+CEND)
                break
        
    elif option == 2 and loadData: #error check data option
        print(CSTART + "2 - ERROR CHECK DATA CHOSEN" + CEND)
        print("Following errors have been detected and the data has been modified to account for it.")
        errorCheck(data)
        print(CSTART+'\n >>Returning to main menu.'+CEND)

    elif option == 3 and loadData: #Plots option

        print(CSTART + "3 - GENERATE PLOTS CHOSEN"+ CEND)
        #skal plotte de afrundede karakterer
        
        #først indlæses array af karakterer
        grades = data[:,2:] #piller std nr og navne fra
        grades = grades.astype(float)
        grades = np.array(roundGrade(grades)) #afrunder karakterer
        
        gradesPlot(grades) #bar plot og graf
        #plot_grade_graph(grades) #graf m gns
        print(CSTART + 'Plots generated and showns in the Plots - menu' + CEND)
    
    elif option == 4 and loadData: #plot
        print(CSTART+"4 - LIST OF GRADES CHOSEN"+CEND)
        #viser studerendes navn ( alfabetisk), karakterer for hver afl samt endelig karakter
        grades = data[:,2:] #piller std nr og navne fra
        grades = grades.astype(float)
        roundedGrades = np.array(roundGrade(grades))
        finalGrades = np.transpose(np.array([computeFinalGrades(roundedGrades)]))
        finalGrades = np.array(roundGrade(finalGrades))
        rG = roundedGrades.astype(str) #skal konverteres for at kunne stackes
        fG = finalGrades.astype(str) #ligeså her
        
        #vi henter lige kolonnenavnene ned fra csv filen
        Header = np.array([dataLoad(filename)[2]])[0]
        Header = Header[0,...]#fjerner unødv dimension
        Header = np.append(np.transpose(Header),'Final Grade') #tilføjer den ekstra kolonne
        
        combinedData = np.hstack([data[:,0:1],data[:,1:2],rG[:,0:],fG])
        combinedData = combinedData[np.argsort(combinedData[:, 1])] #sorter alfabetisk ved at returnerer index for sorteret matrice og konstruere ny matrice om det
        combinedData = np.vstack([Header,combinedData]) #tilføj overskrift
        print(combinedData)
        print(CSTART + "Above is list of grades and final grades. Now returning to main menu..." + CEND)




#test for om data er indlæst;   
    elif 2 <= option <=4 and not loadData:
        print(ESTART +'Option not available until data has been loaded. Choose option 1 from main menu.'+EEND)
        
#man kan godt undgå value error når man indtaster et tal - så v ugyldigt tal printes nedenstående
    else:
        print(ESTART + 'Invalid number entered. Accepted inputs are numbers 1-5.' + EEND)
    menu() #efter menupunkt er fuldført - vis main menu (slip for inf. whileloop)
    option = int(input("Please choose an option:  "))

print(CSTART + "Programme exited. Goodbye."+ CEND) #whileloop køker ikke når opt er 5 - afslut prog.
