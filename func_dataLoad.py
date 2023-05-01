# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:54:31 2023

@author: signe og Ida
"""
import numpy as np
from pathlib import Path


# Functions formål er at indlæse data i form a en csv fil der er komma separaret
# Der prints filnavn, antalet af studernde, og antal af aflevering, hvilket vil gøre det nemt for brugeren at se om filen er loadet rigtigt.
# Hvis der indtastes et ikke eksisterende filnavn vil funktion oplyse dette.

#Definer variable til at farve tekst grøn i interfacet
CSTART = '\x1b[6;30;42m'
CEND = '\x1b[0m'

#Definer variable til at farve tekst grøn i interfacet
ESTART = '\x1b[6;31;40m'
EEND = '\x1b[0m'

#filename = input('Enter a filename for your students grades:  ' )

def dataLoad(filename):
# Hvis funktion bruges til at undersøg om der er en fil med det ønskede navn, hvis ikke printes en fejl kode
    if not Path(filename).is_file():  
        data = []
        message = print(ESTART + "ERROR: Not valid file name or location please try again" + EEND)
    
    else: 
       dataWithHeader = np.genfromtxt(open(filename, "rb"), delimiter=",", dtype=str)
       data = dataWithHeader[1:]
    # Outputet af funktionen angives ved komandoen print og oplyser filnavn, antalet af studernde og antal af aflevering
       message = print("File: " + filename +  "  loaded. \nNumber of Students: " + str(len(data[:,0])) +"\nNumber of Assignments: " + str(len(data[0])-2)) 

    return data,message,dataWithHeader
