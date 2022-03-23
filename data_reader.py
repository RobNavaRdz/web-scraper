#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:08:38 2021

@author: roberto
"""

import PyPDF2
import re

def datos(documento):
    info={}
    casos={}
    page={}
    all_data={}
    object = PyPDF2.PdfFileReader(documento)
    NumPages = object.getNumPages()
    
    fecha= "BAZ"
    juzgado1="ESPECIAL"
    expediente = "EXPEDIENTE"
    nombre="VS"
    nombre2="V.S"
    demandado="Y/"
    
    
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        #print("this is page ",i+1,"------------------------------------------------------------------")
        Text = str(PageObj.extractText())
        Text2=Text.strip().upper().replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U")
        Text3=Text2.split()
        k=0
        for j in Text3:
            fecha_match=re.search(fecha, j)
            if fecha_match:
                dat_fecha=Text3[k+2]+" "+Text3[k+3]+" "+Text3[k+4]+" "+Text3[k+5]+" "+Text3[k+6]
            juzgado_match=re.search(juzgado1, j)
            if juzgado_match:
                dat_juzgado=Text3[k-1]+" "+Text3[k]+" "+Text3[k+1]+" "+Text3[k+2]
            nombre_match=re.search(nombre, j)
            if nombre_match:
                demand=Text3[k+1]
                demandado_match=re.search(demandado,Text3[k+2])
                if demandado_match:
                    dat_demandado=demand
                else:
                    demand=demand+" "+Text3[k+2]
                    dat_demandado=demand
                    demandado_match=re.search(demandado,Text3[k+3])
                    if demandado_match:
                        dat_demandado=demand
                    else:
                        demand=demand+" "+Text3[k+3]
                        demandado_match=re.search(demandado,Text3[k+4])
                        if demandado_match:
                            dat_demandado=demand
                        else:
                            demand=demand+" "+Text3[k+4]
                            demandado_match=re.search(demandado,Text3[k+5])
                            if demandado_match:
                                dat_demandado=demand
                            else:
                                demand=demand+" "+Text3[k+5]
                                dat_demandado=demand
                info["demandado"]=dat_demandado
            expediente_match=re.search(expediente, j)
            if expediente_match:
                sig_pal=Text3[k+1]
                sig_pal_2=Text3[k+2]
                sig_pal_3=Text3[k+3]
                
                if re.search("^J." or "^H." or "^E." or "^T.",sig_pal):
                    dat_expediente=sig_pal
                else:
                    if re.search("^J." or "^H." or "^E." or "^T.", sig_pal_2):
                        dat_expediente=sig_pal_2
                    else:
                        if re.search("^J." or "^H." or "^E." or "^T.", sig_pal_3):
                            dat_expediente=sig_pal_3
                        else:
                            dat_expediente=None
                            
                if dat_expediente==sig_pal:
                    nom=sig_pal_2+" "+sig_pal_3
                    nombre_match=re.search(nombre or nombre2,Text3[k+4])
                    if nombre_match:
                        dat_nombre=nom
                    else:
                        nom=nom+" "+Text3[k+4]
                        nombre_match=re.search(nombre or nombre2,Text3[k+5])
                        if nombre_match:
                            dat_nombre=nom
                        else:
                            nom=nom+" "+Text3[k+5]
                            dat_nombre=nom
                elif dat_expediente==sig_pal_2:
                     nom=sig_pal_3+" "+Text3[k+4]
                     nombre_match=re.search(nombre or nombre2,Text3[k+5])
                     if nombre_match:
                         dat_nombre=nom
                     else:
                         nom=nom+" "+Text3[k+5]
                         nombre_match=re.search(nombre or nombre2,Text3[k+6])
                         if nombre_match:
                             dat_nombre=nom
                         else:
                             nom=nom+" "+Text3[k+6]
                             dat_nombre=nom
                elif dat_expediente==sig_pal_3:
                     nom=Text3[k+4]+" "+Text3[k+5]
                     nombre_match=re.search(nombre or nombre2,Text3[k+6])
                     if nombre_match:
                         dat_nombre=nom
                     else:
                         nom=nom+" "+Text3[k+6]
                         nombre_match=re.search(nombre or nombre2,Text3[k+7])
                         if nombre_match:
                             dat_nombre=nom
                         else:
                             nom=nom+" "+Text3[k+7]
                             dat_nombre=nom
                else:
                    nom=sig_pal_2+" "+sig_pal_3
                    nombre_match=re.search(nombre or nombre2,Text3[k+4])
                    if nombre_match:
                        dat_nombre=nom
                    else:
                        nom=nom+" "+Text3[k+4]
                        nombre_match=re.search(nombre or nombre2,Text3[k+5])
                        if nombre_match:
                            dat_nombre=nom
                        else:
                            nom=nom+" "+Text3[k+5]
                            dat_nombre=nom
            
                            
                #print("********************************************************")
                info["fecha"]=dat_fecha
                info["expediente"]=dat_expediente
                info["juzgado"]=dat_juzgado
                info["nombre"]=dat_nombre
                #print(info)
            casos["caso"+str(i)]=info
            k+=1
        page["pagina"+str(i+1)]=casos
    all_data[str(documento)]=page
    print(all_data)
    return(all_data)
            
            
                        
            
            
            
            
            
            
            
            
            