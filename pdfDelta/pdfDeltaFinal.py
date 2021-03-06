#This code converts the given pdf file
#into a text file for us to look for
#specific drawing numbers
#it takes in a pdf file and outputs a new text file titled "new.txt"

import sys
import PyPDF2
import os

quit = 0;
new_file = open('new_file123', "a+");			#creates text file to convert PDF to

while True:
	try:
		pdfName = input("Enter PDF Name: ")			#asks name of the pdf file
		if pdfName == 'quit':
			quit = 1;
			break;
		pdfObject = open(pdfName, 'rb')				#opens pdf
		break;
	except FileNotFoundError:
		print("Invalid pdf, enter new pdf name or quit to exit program: ")

if(not quit):
	pdfReader = PyPDF2.PdfFileReader(pdfObject) 	#reads the pdf

	numPages = pdfReader.numPages					#number of pages the PDF has 

	for i in range(numPages):
		pageObj = pdfReader.getPage(i)				#gets each individual page 
		new_file.write(pageObj.extractText())		#extracts the text from each page and writes it into the new_file
	
	new_file.close()								#closes text file
	pdfObject.close()								#closes pdf file

######### CODE MOVED FROM pdfDeltaTester.py

	list = [];

	with open('new_file123') as f:
		mylist = [line.rstrip('\n') for line in f]
	new_List = mylist[0].split()

	for i in new_List:									#i is a string
		if len(i) > 1 and i[0] == "I" and i[1] == "W":
			list.append(i)
		if len(i) != 2 and i[0] == "I" and i[1] == "S" :
			if i[2].isdigit():
				list.append(i)
	print(list)
	if(len(list) == 0):
		print("No drawings found")
	else:
		print(str(len(list)) + " Drawings Found")

new_file.close()
os.remove('new_file123')							#deletes the unneccesary text file
