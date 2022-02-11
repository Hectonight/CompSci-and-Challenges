# 1
def a_gives_value_to_b(d):
    d["b"] = d.get("a", 0)
    d["a"] = 0
    return d


# 2
def add_values_at_a_and_b(d):
    return d.get("a", 0) + d.get("b", 0)


# 3
def multiply_values_at_a_b_c(d):
    return d.get("a", 1) * d.get("b", 1) * d.get("c", 1)


# 4
def new_key_ab(d):
    if "a" in d and "b" in d:
        d["ab"] = d["a"] + d["b"]
        del d["a"]
        del d["b"]
    return d


# 5
def remove_ab(d):
    if "a" in d and "b" in d:
        if d["a"] == d["b"]:
            del d["a"]
            del d["b"]
    return d


# 6
def replace_a_or_b(d):
    if ("a" in d) ^ ("b" in d):
        val1 = "a" if "a" in d else "b"
        val2 = "b" if "a" in d else "a"
        d[val2] = d[val1]
        del d[val1]

    return d


# 7
def sorted_keys(d):
    return sorted(d.keys())


# 8
def num_unique_values(d):
    return len(set(d.values()))


def tester():
    print("Tester code. All tests should print true.")
    print()

    print("#1. a_gives_value_to_b")
    x = {'a': 1, 'b': 2, 'c': 3}
    y = {'a': 0, 'b': 1, 'c': 3}
    print(y == a_gives_value_to_b(x))
    x = {'b': 2, 'c': 3, 'd': 4}
    y = {'a': 0, 'b': 0, 'c': 3, 'd': 4}
    print(y == a_gives_value_to_b(x))
    x = {'a': 5, 'c': 7, 'd': 9}
    y = {'a': 0, 'b': 5, 'c': 7, 'd': 9}
    print(y == a_gives_value_to_b(x))
    x = {'c': 4, 'd': 6}
    y = {'a': 0, 'b': 0, 'c': 4, 'd': 6}
    print(y == a_gives_value_to_b(x))
    print()

    print("#2. add_values_at_a_and_b")
    x = {'a': 1, 'b': 2, 'c': 3}
    print(3 == add_values_at_a_and_b(x))
    x = {'b': 7, 'c': 1, 'd': 2}
    print(7 == add_values_at_a_and_b(x))
    x = {'a': 5, 'c': 7, 'd': 9}
    print(5 == add_values_at_a_and_b(x))
    x = {'c': 4, 'd': 6}
    print(0 == add_values_at_a_and_b(x))
    print()

    print("#3. multiply_values_at_a_b_c")
    check = True
    x = {'a': 5, 'b': 3, 'c': 4, 'd': 7}
    check = check and (60 == multiply_values_at_a_b_c(x))
    x = {'a': 7, 'b': 2, 'c': 4, 'd': 7}
    check = check and (56 == multiply_values_at_a_b_c(x))
    print(check)
    check = True
    x = {'a': 5, 'b': 3, 'd': 7}
    check = check and (15 == multiply_values_at_a_b_c(x))
    x = {'a': 6, 'c': 5, 'd': 8}
    check = check and (30 == multiply_values_at_a_b_c(x))
    x = {'b': 10, 'c': 7, 'd': 9}
    check = check and (70 == multiply_values_at_a_b_c(x))
    print(check)
    check = True
    x = {'a': 13, 'd': 100}
    check = check and (13 == multiply_values_at_a_b_c(x))
    x = {'b': 24, 'd': 1000}
    check = check and (24 == multiply_values_at_a_b_c(x))
    x = {'c': 17, 'd': 1000}
    check = check and (17 == multiply_values_at_a_b_c(x))
    x = {'d': 1000, 'e': 2000, 'f': 3000}
    check = check and (1 == multiply_values_at_a_b_c(x))
    print(check)
    print()

    print("#4. new_key_ab")
    x = dict(zip('abc', 'xyz'))
    y = {'ab': 'xy', 'c': 'z'}
    print(y == new_key_ab(x))
    x = dict(zip('abcd', 'pqrs'))
    y = {'ab': 'pq', 'c': 'r', 'd': 's'}
    print(y == new_key_ab(x))
    x = dict(zip('acd', 'xyz'))
    y = x.copy()
    print(y == new_key_ab(x))
    x = dict(zip('bcd', 'xyz'))
    y = x.copy()
    print(y == new_key_ab(x))
    x = dict(zip('cd', 'xy'))
    y = x.copy()
    print(y == new_key_ab(x))
    print()

    print("#5. remove_ab")
    x = {'a': 7, 'b': 7, 'c': 4}
    y = {'c': 4}
    print(y == remove_ab(x))
    x = {'a': "xyz", 'b': "xyz", 'c': 8, 'd': 9}
    y = {'c': 8, 'd': 9}
    print(y == remove_ab(x))
    x = {'a': 5, 'b': 7, 'c': 9}
    y = x.copy()
    print(y == remove_ab(x))
    x = {'a': 4, 'c': 6, 'd': 8}
    y = x.copy()
    print(y == remove_ab(x))
    x = {'b': 10, 'c': 20, 'd': 30}
    y = x.copy()
    print(y == remove_ab(x))
    x = {'d': 100, 'e': 1000, 'f': 10000}
    y = x.copy()
    print(y == remove_ab(x))
    print()

    print("#6. replace_a_or_b")
    x = {'a': 10, 'c': 100, 'd': 1000}
    y = {'b': 10, 'c': 100, 'd': 1000}
    print(y == replace_a_or_b(x))
    x = {'a': 10, 'c': 100, 'd': 1000}
    y = {'b': 10, 'c': 100, 'd': 1000}
    print(x == replace_a_or_b(y))
    x = {'a': 'xyz', 'c': 'qrs', 'd': 'tuv'}
    y = {'b': 'xyz', 'c': 'qrs', 'd': 'tuv'}
    print(y == replace_a_or_b(x))
    x = {'a': 'xyz', 'c': 'qrs', 'd': 'tuv'}
    y = {'b': 'xyz', 'c': 'qrs', 'd': 'tuv'}
    print(x == replace_a_or_b(y))
    x = {'a': 5, 'b': 6, 'c': 7}
    y = x.copy()
    print(y == replace_a_or_b(x))
    x = {'a': 5, 'b': 6, 'c': 7}
    y = x.copy()
    print(x == replace_a_or_b(y))
    x = dict(zip("cde", range(10, 13)))
    y = x.copy()
    print(y == replace_a_or_b(x))
    x = dict(zip("cde", range(10, 13)))
    y = x.copy()
    print(x == replace_a_or_b(y))
    print()

    print("#7. sorted_keys")
    x = {4: 'a', 1: 'b', 13: 'c'}
    print([1, 4, 13] == sorted_keys(x))
    x = dict(zip([5, 8, 9, 1, 4], "uvwxy"))
    print([1, 4, 5, 8, 9] == sorted_keys(x))
    x = dict(zip([5.6, 1.2, 8.9, 7.3], "ABCD"))
    print([1.2, 5.6, 7.3, 8.9] == sorted_keys(x))
    print()

    print("#8. num_unique_values")
    x = dict(zip("abcde", [4, 5, 6, 7, 8]))
    print(5 == num_unique_values(x))
    x = dict(zip("abcde", [10, 20, 30, 20, 10]))
    print(3 == num_unique_values(x))
    x = dict(zip("xyz", [1, 2, 1]))
    print(2 == num_unique_values(x))
    x = dict(zip("abcdef", [17, 18, 19, 17, 18, 19]))
    print(3 == num_unique_values(x))
    x = dict(zip("UVWXYZ", [100] * 6))
    print(1 == num_unique_values(x))
    print()


tester()
