def uncensor(txt, vowels):
    if '*' not in txt:
        return txt
    ready = txt.split('*')
    final = ""
    for num in range(len(ready) - 1):
        final = final + ready[num]
        final = final + vowels[num]
    if txt[-1] != '*':
        final = final + ready[-1]
    return final


