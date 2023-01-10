# -*- coding: utf-8 -*-




from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd
import os
import sys



















''' query2a '''







from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper("http://vm188067-l3s.hosting.uni-hannover.de:7200/repositories/Nomad")

# sparql = SPARQLWrapper("metadata_v1_0.ttl")


sparql.setQuery("""
 
PREFIX dc: <http://purl.org/dc/elements/1.1/> 
PREFIX nomad: <http://https://nomad-coe.eu/ontology#> 
PREFIX qudt: <http://qudt.org/2.1/schema/qudt#>  
PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX sosa: <http://www.w3.org/ns/sosa/> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX matvoc:	<http://stream-ontology.com/matvoc-core/>


select ?formula
WHERE
{ 
    
    ?material a sosa:Sample;
       nomad:has_formula ?formula ;
      sosa:isResultOf ?s.
        
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
with open('query_nomad.txt', 'w') as f:
    for s in query1:
        f.write(str(s)+'\n')   
        # f.write(str(s)+'\n')   




            
            
            


