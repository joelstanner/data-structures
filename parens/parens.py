# def Parens(string):
#     finalValue = 0
#     openCounter = 0
#     for char in string:
#         print "char, Final Value, Open Counter:{}, {},{}".format(char, finalValue, openCounter)

#         if char == "(":
#             openCounter += 1
#             if finalValue == 0:
#                 finalValue += 1

#         elif char == ")" and openCounter:
#             openCounter -= 1
#             if finalValue > 0:
#                 finalValue -= 1
#         elif char == ")" and finalValue == 0:
#             finalValue -= 1

#     return finalValue



# if (, open a new set -- then add one to final value if it's not already 1

def Parens(string):
    finalValue = 0
    openCounter = 0
    for char in string:
        print "char, Final Value, Open Counter:{}, {},{}".format(char, finalValue, openCounter)

        if char == "(":
            openCounter += 1
            finalValue += 1

        elif char == ")":
            finalValue -= 1
            if openCounter:
                openCounter -= 1

    if finalValue > 0:
        return 1

    elif finalValue < 0:
        return -1

    else:
        return 0
