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
    def parse_line(line):
        columns = line.strip().split("\t") #split the line into its 8 tab separated columns
        info_field = columns[7] #INFO is the 8th column (index 7, counting starts at 0)
        info_items = info_field.split(";") #split the INFO field into individual key=value pieces

        #Look inside that line for the AF_EXAC value.
        af_exac_value = None #start by assuming it's not there
        for item in info_items:
            if item.starswith("AF_EXAC="):
                af_exac_value = item.split("=")[1] #grab just the value after the "="
            if af_exac_value is None: #if AF_EXAC was never found, skip this line entirely
                return [] 

            af_exac_number = float(af_exac_value) #convert AF_EXAC string to a number to compare to 0.0001

            if af_exac_number >= 0.0001: #if it's not rare, nothing to report
                return []

            #the variant is rare, find the CLND item
            clndn_value = None
            for item in info_items:
                if item.starswith("CLNDN="):
                    clndn_value = item.split("=")[1]

                if clndn_value is None: #if no CLND value, nothing to report
                    return []

                #multiple dz pipe separated:  split into list
                disease_list = clndn_value("|")

                #remove dz names that aren't real diagnosis
                cleaned_diseases = []
                for disease in disease_list:
                    if disease != "not_specified" and disease != "not_provided":
                        cleaned_diseases.append(disease)

                return cleaned_diseases
            

#Function: update_dictionary (takes a list of diseases and the running tally, returns the updated tally)
#Take in a list of disease names and the current tally dictionary.
#For each disease name in that list:
    #If the disease is already a key in the dictionary, add one to its value.
    #If it is not yet a key in the dictionary, add it with a value of one.
#Return the updated dictionary.