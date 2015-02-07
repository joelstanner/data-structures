def Parens(string):
    openParens = 0
    for char in string:
        print "char, Final Value, Open Parens:{}, {}".format(char, openParens)

        if char == "(":
            openParens += 1

        elif char == ")":
            if openParens > 0:
                openParens -= 1
            else:
                return -1

    if openParens:
        return 1
    else:
        return 0
