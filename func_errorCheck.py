# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:27:41 2023

@author: signe & ida
"""
##
#ERRORCHECK
#får data ind som np.array
#skal kunne fortælle hvor der er ugyldige værdier for studienumre og karakterer i et dataark (liste)

#skal kunne fjerne ugyldig data fra dataarket og gemme det nye, gyldige, dataark
#returnerer fejlmeddelelser og ny data som 'data'
##

import numpy as np

def errorCheck(data):

    #tjekker først om karakterer ligger i gyldigt interval
    for i in range(2,data.shape[1]): #ændr alle karakterer fra strings til floats så vi kan sammenligne dem 
        for ele in data[:,i].astype(float):
            if ele < -3.:
                row = np.where(data[:,i].astype(float) == ele) 
                errors = print("Value", ele," out of bounds." "   Occurs as grade for assignment", i-1, " - assigned to student number",data[row,0],"\n")

                
            elif ele > 12.:
                row = np.where(data[:,i].astype(float) == ele) 
                errors = print("Value", ele," out of bounds." "   Occurs as grade for assignment", i-1, " - assigned to student number",data[row,0],"\n")

    
    #herefter tjekker vi for multiple tilfælde af studienumre
    #vi skal kunne sammenligne studienumrerne og se om de er ens når de står i en sorteret liste
    count = 0 #stud. nr. vi er ved nu
    previous = -1 # forrige stud. nr. i sorteret liste
    indicator = 0 #udpeger duplikattilfælde
    n = 2 #grænsen for hvor mange ens nr. der skal være førend vi udpeger duplikat
    studentList = data[:,0].astype(str) #piller stud. nr. ud af dataarket
    studentNumbers = np.char.strip(studentList,'s') #fjerner s-præfix så vi kan konvertere til int
    studentNumbers = studentNumbers.astype(int)
    studentNumbers.sort() #sorterer efter størrelse 

    for number in studentNumbers:
        if number == previous:
            count = count + 1
        else:
            count = 1
        previous = number
         
        if count >= n:
            indicator = 1
            errors = print("Found {} instances of student nr. {} in column containing student numbers.".format(n, number),"\n")

 

    if indicator == 0:
        errors = print("No other student numbers appear multiple times")

    return errors,data,

