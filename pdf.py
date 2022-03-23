#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:52:58 2021

@author: roberto
"""
import datetime
from datetime import date
from pathlib import Path
import requests

url_base="https://juntatexcoco.edomex.gob.mx/sites/juntatexcoco.edomex.gob.mx/files/files/"

def pdf_name(url_base):
    inicio = datetime.date(2021, 11, 25)
    hoy=date.today()
    dia=hoy.day
    mes=hoy.month
    year=hoy.year
    final=datetime.date(year, mes, dia)
    delta = datetime.timedelta(days=1)
    filename_list=[]

    
    while inicio <= final:
        formato=inicio.strftime("%d-%m-%Y")
        url=url_base+formato+".pdf"
        filename = Path(formato+'.pdf')
        response = requests.get(url)
        if response.status_code==404:
            pass
        else:
            filename.write_bytes(response.content)
            filename_list.append(filename)
        inicio += delta
    return filename_list
      
pdf_name(url_base)
    