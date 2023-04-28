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

#testtadata - skal kommenteres ud når det hele bliver samlet. 
data = np.array([['s12202', 'frank', 3, -4, 5], ['s12202', 'hans', 8, 9, 10], ['s12222', 'kirsten', 1, -2, 10],['s12220', 'jens', 13, 14, 15],['s12220', 'magdalene', 4, 4, 7],['s12230', 'henry', 4, 4, 7]]) #eksempeldata

def errorCheck(data):
    rowDelete = [] #list of rownumbers to be deleted
    rowDelete2 = [] #liste til sletning af duplikat studienumre
    #tjekker først om karakterer ligger i gyldigt interval
    for i in range(2,data.shape[1]): #ændr alle karakterer fra strings til floats så vi kan sammenligne dem
        #data[:,i] = data[:,i].astype(float)
        
        for ele in data[:,i].astype(float):
            if ele < -3.:
                row = np.where(data[:,i].astype(float) == ele) 
                errors = print("Value", ele," out of bounds." "   Occurs as grade for assignment", i-1, " - assigned to student number",data[row,0],"\n")
                rowDelete.append(row)
                
            elif ele > 12.:
                row = np.where(data[:,i].astype(float) == ele) 
                errors = print("Value", ele," out of bounds." "   Occurs as grade for assignment", i-1, " - assigned to student number",data[row,0],"\n")
                rowDelete.append(row)
    
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
            errors = print("Found {} instances of student nr. {} in column containing student numbers. Only first instance will be kept.".format(n, number),"\n")
            numberDuplicateList = np.where(data[:,0].astype(str) == 's'+str(number))[0] #liste over hvilke rækker der indeholder duplikat af studienr
            surplusNumbers = (numberDuplicateList[1:],)
            rowDelete2.append((surplusNumbers))
 

    if indicator == 0:
        errors = print("No other student numbers appear multiple times")
    
    listDelete = rowDelete + rowDelete2 #vi samler at det der skal slettes i en liste
    newData = np.delete(data,listDelete,0) #sletter data


    #print(newData)
    oldData = data #hvis man skulle få brug for den data der ikke er slettet i
    data = newData #skal gemme det nye, gyldige dataark efter at have slettet ugyldig data 
    return errors,data,oldData

data = errorCheck(data)[1] # data variablen skal kaldes på sådan her inde i main menuen når vi når dertil for at sikre at vi arbejder videre med korrigeret data
oldData = errorCheck(data)[2]

print(data) #test
