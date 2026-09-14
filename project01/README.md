# Introduction
This project parses data from a specialized ClinVar VCF file. The AF_EXAC key describes the allele frequencies and the CLNDN key gives the names of the diseases associated with it. The goal is to identify rare variants and tally the diseases linked to them. A variant is considered rare if its AF_EXAC value is below 0.0001. For each rare variant, the program extracts its associated diseases from CLNDN, splitting multiple diseases apart where needed and excluding placeholder values that don't represent real diagnoses. The program reads the file one line at a time and tallies each disease into a running dictionary, printing the final counts once the file is done.

The program is structured into three functions, each with a single responsibility.  parse_line judges one line and returns its associated diseases if it's rare, update_dictionary folds those diseases into the running tally, and read_file coordinates the process, looping through the file and calling the other two.

Our group, Amanda, Mara, and Ildiko, collaborated using a GitHub fork-and-pull-request workflow, with Amanda as group leader.  It was a valuable exercise in working asynchronously through GitHub, making decisions and writing code as a group, and writing a substantial amount of string operations to parse a VCF file.

# Pseudocode

### read_file()

    # initialize empty dict
    # open file
    # loop through lines of file
        # call parse_line
        # if list not empty
            # call update_dictionary
    # return dictionary


### parse_line()
    """Takes a line from a vcf file as a string and returns a list of CLNDN 
    diseases or an empty string where applicable."""

    # initialize empty list
    # skip line if # at start
    # check for AF_EXAC
    # if AF_EXAC exists:
        # extract AF_EXAC using find function and string truncating method
        # if not significant
           # skip line
        # else
            # parse CLNDN using same method as AF_EXAC
            # separate things by pipe into separate list elements
            # drop list elements that are not_specified or not_provided
            # remove potential duplicates

    ## AF_EXAC not present
    # else:
        # skip line, return None or return empty list

    # return list


### update_dictionary()
    """Takes in dictionary and list and returns a dictionary."""
    # loop over elements in list
        # if key exists in dictionary
            # add one to value
        # else
            # initialize key with value of 1

    # return dictionary

# Successes
We originally coded individually and then compared our code, and found that comparing our different approaches was one of the most useful parts of the process. Amanda's version follows the instructions very literally.  Her read_file does no filtering of its own and simply passes every line to parse_line, which then has to check for header lines, check for AF_EXAC, and handle everything else itself, making parse_line longer and more complex. Ildiko and Mara both instead had read_file filter out header lines before anything reaches parse_line, which is more efficient, but relies on read_file taking on some of the checking that the instructions describe as parse_line's job. Both approaches produce functional, correct programs. Since neither approach was wrong, working through this tradeoff, strict adherence to the assignment's described function boundaries versus overall efficiency, was a genuinely useful exercise.

A related difference came up in how each of us located AF_EXAC within a line. Amanda's parse_line searches the raw line directly for the substring AF_EXAC using Python's find function. Ildiko and Mara both first split the line into its tab-separated columns, then searched specifically within the INFO column. Comparing the two showed a similar tradeoff.  Amanda's method is more contained within a single function, while the other isolates the search to a smaller, more relevant piece of text first.

We also picked up a useful debugging habit from Amanda that proved powerful for writing correct code in a program with substantial string operations: adding a print statement after nearly every step while writing a function, so the logic can be watched working, or failing, line by line, rather than only discovering a problem after the function returns an unexpected result. Once a section is confirmed working, the print statements are commented out rather than deleted, so they remain available for troubleshooting later. This was a game changer!

On the collaboration side, our biggest success was working through Git and GitHub together as a group with mixed experience levels. Amanda walked Mara and Ildiko through forking, branches, and pull requests, and the three of us practiced the push, pull, and pull-request cycles together, successfully sharing our work throughout the project and allowing for asynchronous collaboration. This is a skill that will serve us well in our future careers as bioinformaticians.

# Struggles
One of the biggest struggles for this project was that both Ildiko and Mara were more novice Python users and were quite rusty going into this exercise, having not written Python in some time. Relearning how to code, alongside learning Git and GitHub for the first time, made for a genuinely challenging combination.  Amanda was a very gracious group leader and patient teacher, explaining the theory behind much of her more sophisticated code.

On the Git and GitHub side specifically, it took real time and repetition to get comfortable with the workflow.  Understanding the difference between a start branch and a PR branch and why both are needed to open a pull request, learning that git add alone does not save anything until git commit is run, and discovering that forks do not automatically sync with each other. A teammate's push to their own fork, or to the original repository, has to be manually pulled in before it shows up anywhere else. This caused real confusion at one point when a teammate's new file did not appear locally even though it was visible on GitHub, which turned out to be because we were looking at two different repositories, a fork and the original, that looked nearly identical.

We also ran into a smaller but instructive snag when trying to run a finished script.  A FileNotFoundError on the VCF file, which turned out to be a working-directory issue rather than a missing-file issue. Python looks for a relative filename starting from wherever the terminal is standing, not from wherever the script itself is saved, and VS Code's run button does not always use the terminal tab that is currently active. Using different IDE's did not pose any unexpected issues for the collaboration.

Even though we worked well together as a group, it took a little time to hit our stride, particularly while getting used to a new class's teaching style and expectations. Adjusting to a new platform and workflow, on top of the technical learning curve, meant our first several sessions together were as much about figuring out how to collaborate effectively as they were about the assignment itself.

# Personal Reflections
## Group Leader:  Amanada
Group leader's reflection on the project

## Other member:  Ildiko
Coming into this project, I had not written Python in a while, so my first goal was simply to get comfortable writing code again. I had never written pseudocode before, and I found that starting with plain-English pseudocode before writing any real code helped a great deal, since it let me work out the logic without also fighting rusty syntax at the same time. The more organized and well-planned my pseudocode was, the easier it was to translate into actual code.

The most valuable thing I picked up from this project was Amanda's print-statement debugging habit.  Adding print statements at almost every step while writing a function, watching it process real data line by line, and only commenting them out once things worked. This made it dramatically easier to catch a mistake exactly where it happened, rather than getting a wrong final answer and working backward to find out why. It saved so much time troubleshooting bad code. I plan to use this consistently going forward, especially while my Python is still rusty.

Overall, I really enjoyed working with Amanda and Mara. Amanda has more experience with both Python and GitHub, and she was a patient, thorough teacher rather than someone who just handed us answers. When our approaches diverged, whether in code design or in how to interpret the instructions, we talked it through as a group, asked each other real questions, and reached a shared decision rather than any one person deciding for the group. That collaborative problem-solving was, honestly, the best part of this project.

## Other member:  Mara
Other members' reflections on the project

# Generative AI Appendix
Generative AI was not used in this project
