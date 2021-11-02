def hours_minutes_seconds(seconds):
    """Given an int number of seconds, return a tuple
    of the form (h, m, s)"""
    s = seconds % 60
    m = seconds // 60
    h = m // 60
    m -= h * 60
    return h, m, s


def compound_interest_monthly(principal, rate, time):
    """Given a principal, rate, and time, find the
    final amount using the compound interest formula.
    Please round to the nearest 0.01 (2 places)
    You can assume that we are always compounding monthly,
    so n = 12."""
    return round(principal * ((1 + (rate / 12)) ** (12 * time)), 2)


def absolute_deviation(a, b, c, d):
    """Return the average absolute deviation of four numbers:
    a, b, c, d."""
    average = (a + b + c + d) / 4
    return ((abs(average - a)) + (abs(average - b)) + (abs(average - c)) + (abs(average - d))) / 4


def digits_before_after(x):
    """Given a floating-point number x, return a pair of numbers
    listing the number of digits before the "." and the number of digits after.
    It is guaranteed that x has a decimal point somewhere in the number."""
    nums = str(x).split('.')
    return len(nums[0]), len(nums[1])


print("Tester for hours_minutes_seconds")
print(hours_minutes_seconds(3800))
print(hours_minutes_seconds(12350))
print(hours_minutes_seconds(712))
print(hours_minutes_seconds(18493))
print()

print("Tester for compound_interest")
print(compound_interest_monthly(1000, 0.05, 10))
print(compound_interest_monthly(200, 0.3, 4))
print(compound_interest_monthly(7900, 0.24, 8.25))
print()

print("Tester for absolute_deviation")
print(absolute_deviation(9, 2, 6, 4))
print(absolute_deviation(50, 32, 75, 81))
print(absolute_deviation(47.3, 48.1, 49.2, 46.5))
print()

print("Tester for digits_before_after")
print(digits_before_after(12.345))
print(digits_before_after(81245.4))
print(digits_before_after(9.10563))
print(digits_before_after(2378965.235781901124))
