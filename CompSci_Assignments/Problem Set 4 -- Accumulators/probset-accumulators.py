# Problem set on functions and accumulators
# KEY

# Returns the sum of the ones digits in nums. For example:
# sum_ones([51, 82, 43, 94]) -> 1 + 2 + 3 + 4 -> 10
# You can get the ones digit of a number x by doing x % 10
def sum_ones(nums):
    sum_of_ones = 0
    for num in nums:
        sum_of_ones += num % 10
    return sum_of_ones


# Returns the sum of the odd numbers from a to b, inclusive.
# For example, add_odds_between(11, 25) ->
# 11 + 13 + 15 + 17 + 19 + 21 + 23 + 25 = 133
# Both parameters a and b are guaranteed to be odd.
def add_odds_between(a, b):
    final_num = 0
    for num in range(a, b + 1, 2):
        final_num += num
    return final_num


# Returns the geometric mean of nums. The geometric
# mean is the product of all the numbers, to the power
# of 1/len(nums). For example,
# geometric_mean([2.5, 2, 4, 0.8]) -> 16^(1/4) -> 2.0
def geometric_mean(nums):
    geometricMean = 1
    for num in nums:
        geometricMean *= num
    geometricMean **= 1 / len(nums)
    return round(geometricMean, 1)


# Returns all the strings in the list words, with
# a dot separating each word. For example:
# string_dots(["abc", "de", "fghi"]) -> "abc.de.fghi."
def string_dots(words):
    final_str = ''
    for word in words:
        final_str += word + '.'
    return final_str


print("Tester code for sum_ones")
print("Should be 10: ", sum_ones([51, 82, 43, 94]))
print("Should be 15: ", sum_ones([19, 76]))
print("Should be 4:  ", sum_ones([70, 20, 81, 32, 51, 40]))
print()

print("Tester code for add_odds_between")
print("Should be  133: ", add_odds_between(11, 25))
print("Should be  384: ", add_odds_between(93, 99))
print("Should be  1311: ", add_odds_between(35, 79))
print("Should be 3685297: ", add_odds_between(1057, 3981))
print()

print("Tester code for geometric_mean")
print("Should be 2.0:  ", geometric_mean([2.5, 2, 4, 0.8]))
print("Should be 3.0:  ", geometric_mean([0.5, 27, 2]))
print("Should be 10.0: ", geometric_mean([100, 1, 4, 25, 10]))
print()

print("Tester code for string_dots")
print("Should be 192.168.1.1.:        ", string_dots(["192", "168", "1", "1"]))
print("Should be abc.xy.z.:           ", string_dots(["abc", "xy", "z"]))
print("Should be l.mn.opq.rstu.vwxyz.:", string_dots(["l", "mn", "opq", "rstu", "vwxyz"]))
print()
