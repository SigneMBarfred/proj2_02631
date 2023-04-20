# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:01:19 2023

@author: Ida D. Stoltenberg
"""

import csv
from pathlib import Path
import numpy 

# Functions formål er at indlæse data i form a en csv fil der er komma separaret
# Der prints filnavn, antalet af studernde, og antal af aflevering, hvilket vil gøre det nemt for brugeren at se om filen er loadet rigtigt.
# Hvis der indtastes et ikke eksisterende filnavn vil funktion oplyse dette.

def dataLoad(filename):
    global data
# Hvis funktion bruges til at undersøg om der er en fil med det ønskede navn, hvis ikke printes en fejl kode
    if not Path(filename).is_file():  

        print("ERROR: Not valid file name or location please try again")
        return []
    
   

    # Åbner og læser fil
    file = open(filename)
    csvFile = csv.reader(file)

    data = []

    # Indlæser data fra den angivet fil
    for row in csvFile: data.append(row)

    file.close()
    
    
    
    # Outputet af funktionen angives ved komandoen print og oplyser filnavn, antalet af studernde og antal af aflevering
    print("File: \"" + filename + "\" Loaded\nNumber of Students: " + str(len(data)-1) +
          "\nNumber of Assignments: " + str(len(data[0])-2)) 

    return data

dataLoad("testfil.csv")

def errorCheck(data):
    data = numpy.delete(data,[0], axis=0)
    for row in data:
        for element in row[2:len(row)]:
            if element < -3 or element > 12:
                errors = print("Error: Grade", element, "is out of the 7-point grading scale")
    return errors

print(errorCheck(data))