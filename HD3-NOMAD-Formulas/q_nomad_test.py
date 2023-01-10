# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:33:00 2022

@author: GuptaR
"""

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:17:05 2022

@author: GuptaR
"""



from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd
import os
import sys



# __file__ = 'rdf.py'


''' query2 '''







# from SPARQLWrapper import SPARQLWrapper

# sparql = SPARQLWrapper("http://vm188067-l3s.hosting.uni-hannover.de:7200/repositories/Nomad")

# sparql.setQuery("""
 
# PREFIX dc: <http://purl.org/dc/elements/1.1/> 
# PREFIX nomad: <http://https://nomad-coe.eu/ontology#> 
# PREFIX qudt: <http://qudt.org/2.1/schema/qudt#>  
# PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
# PREFIX sosa: <http://www.w3.org/ns/sosa/> 
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
# PREFIX matvoc: <http://stream-ontology.com/matvoc#> 


# CONSTRUCT {         
    
#     ?material nomad:has_material_name ?material_name;
#                nomad:has_formula ?formula.
#               }
# WHERE
# { 
    
#     ?material a sosa:Sample;
#        nomad:has_atoms ?atom ;
#        nomad:has_formula ?formula;
#       sosa:isResultOf ?s.
    
#     # OPTIONAL {  ?material nomad:has_material_name ?material_name.}
    
    
     
#             # ?s a sosa:Sampling;
      
#             # sosa:hasResult ?material;
            
#             # nomad:has_crystal_system "trigonal".
    
# }
# """)


# results = sparql.queryAndConvert()
# print(results.serialize('./actual_results/query2.ttl'))







''' query2a '''





from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper("http://localhost:7200/repositories/nomad_test")

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
       nomad:has_formula ?formula .        
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
with open('query_nomad_test.txt', 'w') as f:
    for s in query1:
        f.write(str(s)+'\n')   
        # f.write(str(s)+'\n')   



# print((query1[0][0]))







# start = time.time()


# sparql = SPARQLWrapper("http://localhost:7200/repositories/metadata")


# # sparql.setMethod(POST)

 
# sparql.setQuery("""
# PREFIX nomad: <http://https://nomad-coe.eu/ontology#> 
# PREFIX qudt: <http://qudt.org/2.1/schema/qudt#> 
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
# PREFIX sosa: <http://www.w3.org/ns/sosa/> 
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
# PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 
# PREFIX matvoc: <http://stream-ontology.com/matvoc#> 

# select   distinct ?material ?formula ?atom ?material_name ?basis_set ?code_name ?version ?compound ?crystal

# where

# { 
    
#     ?material a sosa:Sample;
#        nomad:has_atoms ?atom ;
#        nomad:has_formula ?formula;
#       sosa:isResultOf ?s.
    
#     OPTIONAL {  ?material nomad:has_material_name ?material_name.}
    
#      SERVICE <http://localhost:7200/repositories/method>
#     {
#             ?s a sosa:Sampling;
      
#             sosa:hasResult ?material;

#        nomad:has_basis_set ?basis_set;
    
#           nomad:has_code_name ?code_name;
#        nomad:has_code_version ?version;
#        nomad:has_compound_type ?compound;
#        nomad:has_crystal_system ?crystal
       
       
#     }
    
# }

# """)

# results = sparql.query()
# # print(results)
# sparql.setReturnFormat(JSON)
# results_query2 = sparql.query().convert()

# print(results_query2)

# end = time.time()

# print('time taken to execute the query',end -   start)



# ''' storing results locally '''
# query2=[]

# for result in results_query2["results"]["bindings"]:
    
#     try:
        
    
#         query2.append((result["material"]["value"],result["formula"]["value"],result['atom']['value'],result['material_name']['value'],result['basis_set']['value'],result['code_name']['value'],result['version']['value'],result['compound']['value'],result['crystal']['value']))
#         with open('.//query_results//query2.txt', 'w') as f:
#             for s in query2:
#                 f.write(str(s)[1:-1]+'\n')
#     except:
        
        
#         query2.append((result["material"]["value"],result["formula"]["value"],result['atom']['value'],result['basis_set']['value'],result['code_name']['value'],result['version']['value'],result['compound']['value'],result['crystal']['value']))
#         with open('.//query_results//query2.txt', 'w') as f:
#             for s in query2:
#                 f.write(str(s)[1:-1]+'\n')
            
            
# ''' query4 '''

# start = time.time()


# sparql = SPARQLWrapper("http://localhost:7200/repositories/metadata")


# # sparql.setMethod(POST)

 
# sparql.setQuery("""
# PREFIX dc: <http://purl.org/dc/elements/1.1/> 
# PREFIX nomad: <http://https://nomad-coe.eu/ontology#> 
# PREFIX qudt: <http://qudt.org/2.1/schema/qudt#>  
# PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
# PREFIX sosa: <http://www.w3.org/ns/sosa/> 
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
# PREFIX matvoc: <http://stream-ontology.com/matvoc#> 

# select ?material ?formula ?material_name ?energy_total_T0
# where
# {
 

#    ?material a sosa:Sample;
#        nomad:has_formula ?formula.
    
#     OPTIONAL { ?material nomad:has_material_name ?material_name. }
       
           
    
# SERVICE <http://localhost:7200/repositories/obser>{
        
#         ?ob a sosa:Observation;
#                                    sosa:hasfeatureOfInterest ?material;
#                                    sosa:hasResult ?r.
#         ?r dc:title "energy_total_T0"@en;
#            ?p ?energy_total_T0.
    
#       FILTER (?p = nomad:array || ?p = qudt:numericValue )
        
        
#     }
# }
   
# ORDER BY DESC((?value)) 
# LIMIT 1

# """)

# results = sparql.query()
# # print(results)
# sparql.setReturnFormat(JSON)
# results_query4 = sparql.query().convert()


# end = time.time()

# print('time taken to execute the query',end -   start)


# ''' storing results locally '''
# query4=[]

# for result in results_query4["results"]["bindings"]:
    
#     try:
        
        
        
    
#         query4.append((result["material"]["value"],result["formula"]["value"],result['material_name']['value'],result['energy_total_T0']['value']))
#         with open('.//query_results//query4.txt', 'w') as f:
            
#             for s in query4:
#                 f.write(str(s)[1:-1]+'\n')
#     except:
#         query4.append((result["material"]["value"],result["formula"]["value"],result['energy_total_T0']['value']))
#         with open('.//query_results//query4.txt', 'w') as f:
#             for s in query4:
#                 f.write(str(s)[1:-1]+'\n')
                        
            
            
            


