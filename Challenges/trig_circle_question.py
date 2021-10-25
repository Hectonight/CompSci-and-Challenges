def square_areas_difference(r):
    big = (2 * r) ** 2
    small = ((((r ** 2) / 2) ** (1 / 2)) * 2) ** 2
    return round(big - small)


print(square_areas_difference(5))
