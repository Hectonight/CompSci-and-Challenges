# 1: Given 3 sets, return a set of all
# the elements that are in exactly one
# of the sets, but not in 2 or 3 of them.
def combo3(a, b, c):
    return (a ^ b | c) - ((a & c) | (b & c))


# 2: Given 3 sets, return a set of all the
# elements that are in exactly 2 of the sets,
# not just 1 set, and not all 3.
def combo4(a, b, c):
    return ((a & b) - c) | ((a & c) - b) | ((b & c) - a)


# 3: Given two sets, return True only if
# the sets are different and they overlap
# (they have some intersection) BUT neither set is
# a subset of the other one. And they are not the same.
# In other words, the sets look like a
# "classic" Venn diagram.
def overlap_not_subsets(a, b):
    return not ((a >= b) or (a < b) or a.isdisjoint(b))


# 4: Given a set of numbers, return True only if
# all the numbers in the list are even numbers between
# 1000 and 2000 (inclusive).
# Hint, use the given set valid_nums
def all_even_thousand(S):
    valid_nums = set(range(1000, 2001, 2))
    return S <= valid_nums


# 5: Given a set of numbers, return True only if
# all the numbers in the set are multiples of 10
# between 500 and 600 (inclusve). Create your own
# set of valid numbers for this one.
def all_tens_five_hundred(S):
    return S <= set(range(500, 601, 10))


# 6: Given a string, return True only if all the
# letters in the string are vowels. There may be
# other characters, but these should be disregarded.
# All letters will be all-caps. You can use the
# two given sets.
def all_letters_are_vowels(s):
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    vowels = set("AEIOU")
    return set(s).isdisjoint(alphabet - vowels)


# 7: Given a string, return True only if NONE
# of the letters in the string are vowels.
# All letters will be all-caps.
# You can use the given set.
def no_vowels(s):
    vowels = set("AEIOU")
    return set(s).isdisjoint(vowels)


# 8: Given three sets a, b, c, return True
# only if the intersection of a and b is disjoint
# from c (does not overlap with c).
def intersection_disjoint(a, b, c):
    return c.isdisjoint(a & b)


def tester():
    import random
    print("Tester code. All tests should be True.")
    print()

    print("Tester for #1: combo3")
    a = {0, 1, 2, 3, 4, 5}
    b = {2, 4, 6}
    c = {1, 3, 5, 7}
    print({0, 6, 7} == combo3(a, b, c))
    a = {"car", "truck", "boat"}
    b = {"boat", "fish", "dolphin"}
    c = {"fish", "truck", "boat", "house"}
    print({"car", "dolphin", "house"} == combo3(a, b, c))
    a = {1, 2, 3}
    b = {0, 2, 3, 4}
    c = {3, 4, 5}
    print({0, 1, 5} == combo3(a, b, c))
    print()

    print("Tester for #2: combo4")
    a = {0, 1, 2, 3, 4, 5, 6}
    b = {2, 4, 6}
    c = {1, 2, 3, 4, 5, 7}
    print({1, 3, 5, 6} == combo4(a, b, c))
    a = {"car", "truck", "boat"}
    b = {"boat", "fish", "dolphin", "car"}
    c = {"fish", "truck", "boat", "house"}
    print({"car", "truck", "fish"} == combo4(a, b, c))
    a = {1, 2, 3}
    b = {0, 2, 3, 4}
    c = {3, 4, 5}
    print({2, 4} == combo4(a, b, c))
    print()

    print("Tester code for #3: overlap_not_subsets")
    a = {1, 2}
    b = {2, 3}
    print(overlap_not_subsets(a, b))
    a = {1, 2, 3, 4, 5}
    b = {2, 3, 4, 5, 6}
    print(overlap_not_subsets(a, b))
    a = {5, 6, 7, 8, 9}
    b = {1, 2, 3, 4, 5}
    print(overlap_not_subsets(a, b))
    a = {5, 6, 7, 8}
    b = {1, 2, 3, 4}
    print(not overlap_not_subsets(a, b))
    a = {10, 20, 30, 40}
    b = {20, 40}
    print(not overlap_not_subsets(a, b))
    a = {100, 200, 300}
    b = {50, 100, 150, 200, 250, 300}
    print(not overlap_not_subsets(a, b))
    print(not overlap_not_subsets(a, a))
    print(not overlap_not_subsets(b, b))
    print()

    print("Tester code for #4: all_even_thousand")
    print(all_even_thousand(set(range(1000, 2001, 2))))
    print(all_even_thousand({1000, 1500, 1900}))
    print(all_even_thousand({random.randrange(1000, 2001, 2) for x in range(100)}))
    print(not all_even_thousand({1000, 1500, 2500}))
    print(not all_even_thousand({1000, 1400, 1001}))
    print(not all_even_thousand({800, 1205, 3000}))
    print()

    print("Tester code for #5: all_tens_five_hundred")
    print(all_tens_five_hundred({510, 590, 550}))
    print(all_tens_five_hundred({500, 520, 580, 540, 560, 570}))
    print(all_tens_five_hundred(set()))
    print(not all_tens_five_hundred({520, 525, 530, 545}))
    print(not all_tens_five_hundred({490, 540, 590, 620}))
    print(not all_tens_five_hundred({499, 573, 581, 642}))
    print()

    print("Tester code for #6: all_letters_are_vowels")
    print(all_letters_are_vowels("AA EE??! (IOU)IOAA___++E/.$$$!![]<>?"))
    print(all_letters_are_vowels("12345OA____096EIO%%%"))
    print(all_letters_are_vowels("@#$%^5678"))
    print(not all_letters_are_vowels("COMPUTER SCIENCE"))
    print(not all_letters_are_vowels("1234ABCDEF???!!!"))
    print(not all_letters_are_vowels("UVWXYZ123"))
    print()

    print("Tester code for #7: no_vowels")
    print(no_vowels("??!@#$%789"))
    print(no_vowels("QRSTMNXYZ"))
    print(no_vowels("123456"))
    print(not no_vowels("ALPHABET SOUP"))
    print(not no_vowels("PYTHON CODE"))
    print(not no_vowels("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG??!! 123"))
    print()

    print("Tester code for #8: intersection_disjoint")
    a = {1, 2, 3}
    b = {2, 3, 4}
    c = {4, 5, 1}
    print(intersection_disjoint(a, b, c))
    a = {10, 20, 30}
    b = {30, 40, 50}
    c = {40, 50, 10, 20}
    print(intersection_disjoint(a, b, c))
    a = {1, 2, 3}
    b = {4, 5, 6}
    c = {7, 8}
    print(intersection_disjoint(a, b, c))
    a = {1, 2, 3}
    b = {3, 4, 5}
    c = {3, 6, 9}
    print(not intersection_disjoint(a, b, c))
    a = {1, 2, 3}
    b = {2, 3, 4}
    c = {2, 4, 8}
    print(not intersection_disjoint(a, b, c))
    a = {1, 2}
    b = {1, 3}
    c = {1}
    print(not intersection_disjoint(a, b, c))


tester()
