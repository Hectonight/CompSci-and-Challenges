def majority(items):
    maxChar = ""
    maxVal = 0

    for char in set(items):
        num = items.count(char)

        if maxVal <= num:
            maxChar = char if maxVal != num else None
            maxVal = num

    return maxChar if maxVal > len(items) / 2 else None