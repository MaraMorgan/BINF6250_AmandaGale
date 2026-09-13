#!/usr/bin/env python
from pprint import pprint

def parse_line(line):
    pass

def update_dictionary(disease_list, tally):
    pass

def read_file(filename):
    pass

if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))



#Pseudocode

#Whole Program (What Happens When You Run It)
#Start the program.
#Call the function that reads the file, giving it the name of the VCF file to open.
#Take whatever that function hands back (the tally of diseases).
#Print that tally out in a readable way.

#Function: read_file (walks through the whole file)
#Take in the name of a file to open.
#Open that file.
#Create an empty dictionary to keep track of disease counts.
#Go through the file one line at a time (never load the whole file at once):
    #If the line starts with a "#" (it's a header or meta-info line), skip it and move to the next line.
    #Otherwise, send this line to the function that examines a single line.
    #Take back the list of diseases that function returns (it might be empty).
    #If that list is not empty, send it (along with the running tally dictionary) to the function that updates the dictionary.
    #Take back the updated dictionary.
#Once every line has been read, close the file.
#Return the dictionary of disease counts.

#Function: parse_line (examines one single line)
#Take in one line of text from the file.
#Look inside that line for the AF_EXAC value.
#If AF_EXAC is not present in the line, return an empty list (nothing to report).
#If AF_EXAC is present, turn its value into a number.
#If that number is not less than 0.0001, the variant is not rare and return an empty list.
#If that number is less than 0.0001, the variant is rare:
    #Look inside the line for the CLNDN value (the disease names).
    #If there are multiple diseases separated by a pipe (|), split them into separate names.
    #Remove any disease name that is "not_specified" or "not_provided."
    #Return the remaining list of disease names.

#Function: update_dictionary (takes a list of diseases and the running tally, returns the updated tally)
#Take in a list of disease names and the current tally dictionary.
#For each disease name in that list:
    #If the disease is already a key in the dictionary, add one to its value.
    #If it is not yet a key in the dictionary, add it with a value of one.
#Return the updated dictionary.