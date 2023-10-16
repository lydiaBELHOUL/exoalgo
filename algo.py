#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:27:49 2023

@author: lydia
"""
####### exo2
list=[13,79,1,30,456,16]
maximum= list[0]
for i in list :
     if i> maximum:
         maximum= i
print("le plus grand element est", maximum)
#### exo3#####

list3= [13, 79, 1, 30, 456, 16]

list2= []

list4=[]

for i in list3 :
    if i%4==0:
        list4.append(i)
    else :
        list2.append(i)
print ("Liste des nombres divisibles par 4:", list4)
print ("Liste des nombres divisibles par 4:", list2)