# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:57:56 2023

@author: Formation
"""


###LIBRAIRIES###

#Lecture d'url
import requests

#Lecture et parsing de XML
import xml.etree.ElementTree as ET

#xml en dictionnaire parce qu'on ne sait pas faire autrement...
#import xmltodict

#lecture de csv
import pandas as pd




if __name__ == "__main__":
    
    
    #Récupérer l'url
    
    url = "https://wxs.ign.fr/geoportail/wmts?SERVICE=WMTS&REQUEST=GetCapabilities"
    
    response = requests.get(url)
    
    #Créer un XML en local
    
    with open('temp.xml','wb') as file:
        file.write(response.content)
    
    #dict_data = xmltodict.parse(response.content) très mauvaise idée ça complique le unparse
                            
    xml_data = ET.parse('temp.xml')
    
    root = xml_data.getroot()
    
    contents_elem = root.find('{http://www.opengis.net/wmts/1.0}Contents')
    
    
    for layer in contents_elem.findall('{http://www.opengis.net/wmts/1.0}Layer'):
        
        layer_identifier = layer.find('{http://www.opengis.net/ows/1.1}Identifier').text
        
        print(layer.tag, layer_identifier)
    
    print('Hellooo Worldd!')
    
    print(root.tag)
    
    good_layers_csv = pd.read_csv('layers.csv') 
    print(good_layers_csv)
    
    
    
    
    
    
    
    
    
    
