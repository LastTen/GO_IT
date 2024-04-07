def string_to_codes(string: str) -> dict:
    codes = {x: ord(x) for x in string}

    # for ch in string:
    #     if ch not in codes:
    #         codes[ch] = ord(ch)
    return codes


print(string_to_codes("akakkfkf"))
