def disemvowel(string_):
    intab = "aeiouAEIOU"
    trantab = str.maketrans("", "", intab)

    return string_.translate(trantab)


print(disemvowel("This website is for losers LOL!"))


def translate(str):
    intab = "aeiou"
    outtab = "12345"
    trans = str.maketrans(intab, outtab)
    return str.translate(trans)


str = "This is string example"
print(translate(str))
