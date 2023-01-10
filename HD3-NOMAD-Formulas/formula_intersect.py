# -*- coding: utf-8 -*-


import os 
import sys

from pathlib import Path

from rdflib import Graph
from rdflib.compare import to_isomorphic, graph_diff, similar


import re



####### Nomad data here


t =[]
with open('query_nomad_test.txt') as f:
    for line in f:
        line = line.strip('\n')
        t.append(line)

t1 = []
for i in t:
    i1 = (i.split('matvoc-core/')[-1])  
    t1.append(i1)
    

# print((t1[0]))



######  Hybrid data here

t2 =[]
with open('query_hybrid.txt') as f:

    for line in f:
        string = (line.split('matvoc-core/')[-1])  
        # print(string)
            
        if "%" in string:
            # print('true')
            
            
            index = string.index("%")
            # print(index)
            while index+2 < len(string):
                string = string[:index] + string[index+3:]
                try:
                    index = string.index("%")
                except ValueError:
                    break
            
            
    
            t2.append(string)
        else:
            t2.append(string)
            
       
# print(t2)


t3 = []
for i2 in t2:
    
    i3 = i2.split(',')[0]
    i3 = re.sub("[^A-Za-z0-9]", '', i3)



    i3= re.sub( r"([A-Z])", r" \1", i3).split()

    # print(i3)

    i3 = sorted(i3)

    i3 = ''.join(i3)


    # print(i3)
    # break
    
    t3.append(i3)

# print(t3)
# print(type(t3[0]))


def common_formula(a,b):   
    a_set = set(a)
    b_set = set(b)
     
    # print(a_set)
    # print(b_set)
    # check length
    if len(a_set.intersection(b_set)) > 0:
        return(a_set.intersection(b_set)) 
    else:
        return("no common formula's")




print("finding common formula's")


print(common_formula(t1,t3))



















