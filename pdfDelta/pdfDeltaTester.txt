#This code takes the "new.txt" file that pdfDelta creates
#and creates a list of all the drawings that start with
#IW and IS
#

import sys
import os


list = [0]*40;
index = 0;

with open('new.txt') as f:
    mylist = [line.rstrip('\n') for line in f]
new_List = mylist[0].split()

for i in new_List:									#i is a string
	if len(i) > 1 and i[0] == "I" and i[1] == "W":
		list[index] = i
		index += 1
	if len(i) != 2 and i[0] == "I" and i[1] == "S" :
		if i[2].isdigit():
			list[index] = i
			index += 1

print(len(list))
print(list)

			
		
		

	
	


	
