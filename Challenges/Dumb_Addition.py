def dumb_add(num1, num2):
    if type(num1) != int:
        raise TypeError('num1 is not type int')
    if type(num2) != int:
        raise TypeError('num2 is not type int')

    digits1 = []
    digits2 = []

    num_digits1 = len(str(num1))
    num_digits2 = len(str(num2))

    if num_digits1 == num_digits2:
        pass
    elif num_digits1 > num_digits2:
        for num in range(num_digits1 - num_digits2):
            digits2.append(0)
    elif num_digits1 < num_digits2:
        for num in range(num_digits2 - num_digits1):
            digits1.append(0)

    for digit in str(num1):
        digits1.append(int(digit))
    for digit in str(num2):
        digits2.append(int(digit))

    dumb_digits = []
    for d1, d2 in zip(digits1, digits2):
        dumb_digits.append(str(d1 + d2))

    return int(''.join(dumb_digits))


output = dumb_add(num1=int(input()), num2=int(input()))
print(output)
