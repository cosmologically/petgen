#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Description: Generates random fictional pets and prints the results.
#Author: Per Wolf
#Date: 10/12/2018
#Contact: per.c.wolf@gmail.com

import random 

i = 1
statuscat = "YOUR EGG HATCHED INTO A(N)...  \n \n "

color = []
with open("color.txt", "r") as f:
	for line in f.readlines():
		color = color + line.strip("\n").split("\n")	
f.close()	
size = []
with open("size.txt", "r") as f:
	for line in f.readlines():
		size = size + line.strip("\n").split("\n")	
f.close()	
species = []
with open("species.txt", "r") as f:
	for line in f.readlines():
		species = species + line.strip().split("\n")	
f.close()		
special = []
with open("special.txt", "r") as f:
	for line in f.readlines():
		special = special + line.strip("\n").split("\n")
f.close()		

while i > 0:
  rand_desc = random.choice(size)
  rand_color = random.choice(color)
  rand_species = random.choice(species)
  rand_special = random.choice(special)
  statuscat = statuscat + rand_desc + rand_color + rand_species + " \n\nCONGRATULATIONS! \n\n(You notice that this one " + rand_special + "...)" 
  print(statuscat) 
  i = -1
