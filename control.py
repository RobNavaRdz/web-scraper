#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 19:07:50 2021

@author: roberto
"""
import pdf
import data_reader
import json

url_base="https://juntatexcoco.edomex.gob.mx/sites/juntatexcoco.edomex.gob.mx/files/files/"

nom_list=pdf.pdf_name(url_base)

dicc={}

for i in nom_list:
    j=1
    file=str(i)
    print(file)
    dicc["documento"+str(j)]=data_reader.datos(file)
    j+=1
with open ("data.json", "w") as file:
    json.dump(dicc, file, indent=4)


    