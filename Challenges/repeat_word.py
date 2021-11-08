def repeated(s):
    for num in range(1, len(s)):
        parts = [s[i:i+num] for i in range(0, len(s), num)]
        if len(set(parts)) == 1:
            return True
    return False
