# Test if substrings in a string repeats
def repeated(s: str):
    return s in {s[:num] * (len(s) // num) for num in range(1, len(s) + 1) if s[:num] != s}


print(repeated("a"), repeated("ababab"), repeated("aba"), repeated("abcabcabcabc"), repeated("aaxxtaaxztaaxxt"))
