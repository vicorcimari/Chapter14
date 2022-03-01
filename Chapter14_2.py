# Modify this function to return a list of string as defined above

def list_benefits():
    benefits_list = ["More organized code", "More readable code", "Easier code reuse",
                     "Allowing programmers to share and connect code together"]
    return benefits_list

    pass

# Modify this function to concatenate to each benefit -" is a benefit of functions!"


def build_sentence(benefit):
    return "%s is a benefit of function!" % benefit

    pass

def name_the_benefits_of_functions():

    list_of_benefits=list_benefits()

    print(build_sentence(list_of_benefits[0]))

    print(build_sentence(list_of_benefits[1]))

    print(build_sentence(list_of_benefits[2]))

    print(build_sentence(list_of_benefits[3]))


name_the_benefits_of_functions()