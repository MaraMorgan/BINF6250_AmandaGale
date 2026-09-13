"""
Expectations

You are expected to:
    Copy the template code below into your program
    Download and move the clinvar_20190923_short.vcf to the same folder as your program
    Within the program:
        Write a function called parse_line that:
            Takes a string as an argument
            Extract the AF_EXAC data to determine the rarity of the variant
                If AF_EXAC is not present, skip the line
                If the variant is rare (value for the AF_EXAC key < 0.0001)
                    return a list of associated diseases in CLNDN
                        Do not count the diseases that are:
                            not_specified
                            not_provided
                If the variant is not rare:
                    return an empty list
        Write another function called read_file that:
            Takes a string as an argument representing the file to be opened
            Open the file
            Read the file line by line.
                Note: You are expected to do this one line at a time.
                      The reasoning is that if the file is sufficiently large, you may not have the memory available to hold it.
                      So, do not use readlines()!
            Passes the line to parse_line
            Use a dictionary to count the results given by parse_line to keep a running tally (or count) of the number of times a specific disease is observed
            return that dictionary
        print the results from read_file when it is complete

"""


"""
Project specific information

The given data (clinvar_20190923_short.vcf) is a specialized form of the VCF file. 
As such, there are some additional details to consider when parsing for this assignment. 
You will be expected to consider two (2) special types of keys:

    The AF_EXAC key that describes the allele frequencies from the ExAC database
        ##INFO=<ID=AF_EXAC,Number=1,Type=Float,Description="allele frequencies from ExAC">;
        The data included are floating point numbers
    
    The CLNDN key that gives all the names of diseases the given variant is associated with
        ##INFO=<ID=CLNDN,Number=.,Type=String,Description="ClinVar's preferred disease name for the concept specified by disease identifiers in CLNDISDB">;
        The data are strings. However, if there are multiple diseases associated with a given variant, 
           the diseases are pipe (|) separated (there are 178 instances of this case)

"""

# template code

#!/usr/bin/env python
from pprint import pprint

# Modify this function signature and fill in the details
def parse_line(vcf_line): # argument:string
    """
    Takes a string and returns a list
    :param line: string
    :return: list
    """

    # strip lines and specify INFO column
    strip_header = vcf_line.strip().split('\t')
    extract_info_column = strip_header[7]

    # Separate chunks delineated by semicolons in INFO string
    separate_semicolon_chunks = extract_info_column.split(';')

    # Further separate key:value chunks
    # define dictionaries before the loop
    af_exac = []
    clndn = []
    for chunk in separate_semicolon_chunks:
        key, value = chunk.split('=')
        if key == 'AF_EXAC':
            af_exac = value
        elif key == 'CLNDN':
            clndn = value



     if significance of AF_EXAC < 0.0001 # 'AF_EXAC < 0.0001'
            return list of CLNDN disease names, skip "not specified" and/or "not provided"
                # how to handle cases where disease names are piped " | " ?

        else:
            return list() # return empty list if AF_EXAC not significant


# note that from this function we want to return a list
pass



def update_dictionary(#key;value pair, something else here)
        # creating a dictionary here.
        # Note: we need to return a list from parse_line of AF_EXAC < 0.00001, and then create a dictionary of the CLNDN disease name and tally for each significant AF_EXAC
    key = CLNDN disease name #based on AF_EXAC < 0.0001
    value = tally of CLNDN disease names

# format? print("f {variable representing disease name} : {tally}) and this would be for each disease



# Modify this function signature and fill in the details
def read_file(clinvar, r)
    with open('clinvar_20190923_short.vcf', 'r') as f:
        for line in f:
            if line.startswith('#') #skip all lines that start with '#'
                continue

    calling from other two functions and returning here

    pass


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
