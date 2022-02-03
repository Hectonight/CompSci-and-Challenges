# Problems on sets.

# 1
def more_unique_letters(s, t):
    return s if len(set(s)) >= len(set(t)) else t


# 2
def sum_unique(L):
    return sum(set(L))


# 3
def how_many_extra(big, small):
    return len(big - small)


# 4
def how_many_unique_consonants(s):
    vowels = set("AEIOU")
    return len(set(s) - vowels)


# 5
def remove_smallest_extra(big, small):
    big.remove(min(big - small))
    return big


# 6
def add_smallest_extra(big, small):
    small.add(min(big - small))
    return small


# 7
def combo1(a, b, c):
    return a & (b ^ c)


# 8
def combo2(a, b, c):
    return (a | b) - c


def tester():
    print("Tester code. All tests should get true.")
    print()

    print("Tester #1 for more_unique_letters")
    print("Maine" == more_unique_letters("Mississippi", "Maine"))
    print("Wyoming" == more_unique_letters("Wyoming", "Hawaii"))
    print()

    print("Tester for #2 sum_unique")
    print(10 == sum_unique([1, 2, 3, 4, 1, 1, 1, 2, 3, 4]))
    print(20 == sum_unique([13, 7, 0, 7, 7, 7, 13]))
    print(30 == sum_unique([20, 15, -5, -5, -5, 15, 15, 20]))
    print()

    print("Tester for #3 how_many_extra")
    print(1 == how_many_extra({1, 3, 5}, {1, 5}))
    print(2 == how_many_extra({20, 30, 40, 50, 60}, {20, 30, 60}))
    print(3 == how_many_extra(set("apple"), set("aaaaa")))
    print()

    print("Tester for #4 how_many_unique_consonants")
    print(how_many_unique_consonants("MISSISSIPPI") == 3)
    print(how_many_unique_consonants("ARKANSAS") == 4)
    print(how_many_unique_consonants("INDIANA") == 2)
    print()

    print("Tester for #5 remove_smallest_extra")
    print(remove_smallest_extra({9, 7, 5, 3, 1}, {1, 5}) == {9, 7, 5, 1})
    print(remove_smallest_extra({2, 4, 6, 8}, {2, 8}) == {2, 6, 8})
    print(remove_smallest_extra({10, 20, 30, 40, 50, 60, 70, 80, 90}, {10, 50}) == {10, 30, 40, 50, 60, 70, 80, 90})
    print()

    print("Tester for #6 add_smallest_extra")
    print(add_smallest_extra({9, 7, 5, 3, 1}, {1, 5}) == {1, 3, 5})
    print(add_smallest_extra({2, 4, 6, 8}, {2, 8}) == {2, 4, 8})
    print(add_smallest_extra({10, 20, 30, 40, 50, 60, 70, 80, 90}, {10, 50}) == {10, 20, 50})
    print()

    print("Tester for #7 combo1")
    a = {1, 2, 3, 4}
    b = {2, 4, 5}
    c = {1, 4, 5}
    print(combo1(a, b, c) == {1, 2})
    a = {7, 8, 9}
    b = {0, 7, 8}
    c = {1, 8, 9}
    print(combo1(a, b, c) == {7, 9})
    print()

    print("Tester for #8 combo2")
    a = {1, 3}
    b = {2, 4}
    c = {2, 3}
    print(combo2(a, b, c) == {1, 4})
    a = {"apple", "banana", "carrot"}
    b = {"banana", "donut", "eggplant"}
    c = {"apple", "eggplant"}
    print(combo2(a, b, c) == {"banana", "carrot", "donut"})
    print()


tester()
