def Parens(unicode):
    '''Returns 0 if string is balanced (all parentheses are matched)
       Returns 1 if string is open (has an open paren that is unclosed)
       Returns -1 if string is broken (closed paren not preceded by open one)
       '''

    openParens = 0
    for char in unicode:

        if char == u"(":
            openParens += 1

        elif char == u")":
            if openParens > 0:
                openParens -= 1
            else:
                return -1

    if openParens:
        return 1
    else:
        return 0
