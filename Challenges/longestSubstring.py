def longest_substring(digits):
    substrings = []
    current_substring = None
    for digit in str(digits):
        if current_substring is None:
            current_substring = digit
        if (int(current_substring[-1]) % 2) != (int(digit) % 2):
            current_substring += digit
        else:
            substrings.append(int(current_substring))
            current_substring = digit

    substrings.append(int(current_substring))

    sublength = []
    for substring in substrings:
        sublength.append(len(str(substring)))
    return substrings[sublength.index((max(sublength)))]


print(longest_substring(12359045382904238509876543298765432987654328765432987654387654346125521))
