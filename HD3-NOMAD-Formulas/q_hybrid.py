# -*- coding: utf-8 -*-




from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd
import os
import sys










''' query2a '''







from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper("http://vm188067-l3s.hosting.uni-hannover.de:7200/repositories/Hybrid3")

sparql.setQuery("""
 
PREFIX hybrid3: <https://materials.hybrid3.duke.edu/materials/> 
 PREFIX matonto: <http://matonto.org/ontology/matonto#> 
 PREFIX owl: <http://www.w3.org/2002/07/owl#> 
 PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
 PREFIX sosa: <http://www.w3.org/ns/sosa/> 
 PREFIX ssn: <http://www.w3.org/ns/ssn/> 
 PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
 PREFIX rml: <http://semweb.mmlab.be/ns/rml#>
 PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
 PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX matvoc:	<http://stream-ontology.com/matvoc-core/>


select ?formula
 where{
    
   ?id a sosa:FeatureOfInterest;
         sosa:hasSample ?system.
    
         ?system a sosa:Sample;
               hybrid3:has_formula ?formula.
    
            
    

}
""")

results = sparql.query()
# print(results)
sparql.setReturnFormat(JSON)
results_query1 = sparql.query().convert()



''' storing results locally '''
query1=[]
for result in results_query1["results"]["bindings"]:
    query1.append((result["formula"]["value"]))
    # print(query1)
with open('query_hybrid.txt', 'w',encoding="utf-8") as f:
    for s in query1:
        # f.write(str(s)[1:-1]+'\n')   
        f.write(str(s)+'\n')   




            
            


