def looper(n):
    found = False
    for num in range(2, n + 1):
        print(num, n)
        if n % num == 0:
            found = True
            if num not in num_power.keys():
                num_power[num] = 1
            else:
                num_power[num] += 1
            return [found, n // num]

    return [found, None]


def is_economical(n):
    global num_power
    num_power = {}
    continuing = True
    n_use = n
    while continuing:
        looper_result = looper(n_use)
        continuing = looper_result[0]
        n_use = looper_result[1]

    totalDigits = 0
    for exp in num_power:
        totalDigits += len(str(exp))
        if num_power[exp] > 1:
            totalDigits += len(str(num_power[exp]))
    print(totalDigits)
    print(len(str(n)))
    print(num_power)
    if totalDigits == len(str(n)):
        return "Equidigital"
    if totalDigits < len(str(n)):
        return "Frugal"
    else:
        return "Wasteful"


# print(is_economical(24))

print(is_economical(14), "Equidigital", "Example #1")
print(is_economical(125), "Frugal", "Example #2")
print(is_economical(1024), "Frugal", "Example #3")
print(is_economical(30), "Wasteful", "Example #4")
print(is_economical(81), "Equidigital")
print(is_economical(243), "Frugal")
print(is_economical(5), "Equidigital")
print(is_economical(6), "Wasteful")
print(is_economical(1267), "Equidigital")
print(is_economical(1701), "Frugal")
print(is_economical(1267), "Equidigital")
print(is_economical(12871), "Equidigital")
print(is_economical(88632), "Wasteful")
