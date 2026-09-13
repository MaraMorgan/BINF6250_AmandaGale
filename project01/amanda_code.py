from pprint import pprint


def parse_line(this_line):
    """Takes string and returns a list."""

    print(this_line.strip())
    clndn_list = []   # list to track clndn

    # if line starts with #, skip
    if not this_line.startswith('#'):
        # search for AF_EXAC
        af_start = this_line.find('AF_EXAC=')

        if af_start != -1:
            print("AF_EXAC entry found")
            # extract AF_EXAC
            afexac_line = this_line[af_start:]
            af_end = afexac_line.find(';')
            ##print("AF_EXAC string:", afexac_line[0:af_end])
            af_value = float(afexac_line[0:af_end].split('=')[1])
            print("AF_EXAC value:", af_value)

            # check af_exac significance
            if af_value >= 0.0001:
                print("AF value not rare.\n")
                pass
            else:
                print("Rare AF value found!")
                clndn_start = this_line.find("CLNDN=")
                clndn_line = this_line[clndn_start:]
                # extract clndnd string
                clndn_end = clndn_line.find(';')
                ##print("CLNDN string:", clndn_line[0:clndn_end])
                clndn_value = clndn_line[0:clndn_end].split('=')[1]
                # separate elements by pipe into separate list elements
                clndn_list = clndn_value.split('|')
                # drop list elements that are not_specified or not_provided
                if 'not_provided' in clndn_list:
                    clndn_list = clndn_list.remove('not_provided')
                if 'not_specified' in clndn_list:
                    clndn_list = clndn_list.remove('not_specified')
                print(f"CLNDN list: {clndn_list}")

        # AF_EXAC not present
        else:
            print('Skipping line, not an AF_EXAC entry.\n')

    # line starts with #
    else:
        print("Skipping line, not a legitimate entry.\n")

    return clndn_list


def update_dictionary(clndn_dict, clndn_list):
    """Takes in dictionary and list and returns a dictionary."""

    for disease in clndn_list:
        if disease in clndn_dict:   # if disease exists in dictionary
            clndn_dict[disease] += 1   # add to counter
        else:    # if disease does not exist yet
            clndn_dict[disease] = 1    # initialize counter

    return clndn_dict


def read_file(filename):

    clndn_dict = {}
    i = 1
    # loop through lines of file
    with open(filename, 'r') as f:
        for line in f:
            if i < 100:
                # parse the lines of the file for disease
                clndn_list = parse_line(line)
                if clndn_list:   # if disease list not empty, update dict
                    print("Diseases associated with variant. Updating Dictionary.\n")
                    update_dictionary(clndn_dict, clndn_list)
                i += 1

    print("Final disease count:")
    return clndn_dict


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))

