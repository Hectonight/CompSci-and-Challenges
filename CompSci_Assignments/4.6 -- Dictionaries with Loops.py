# 4.6: Problems on dictionaries with loops

# 1
def five_dollar_store_total(items):
    return sum({"Pencil": 0.5, "Candy": 2.0, "Smart Phone": 100.0}.get(item, 5.0) for item in items)


# 2
def double_fish(menu):
    return {food: (2 if "fish" in food else 1) * price for food, price in menu.items()}


# 3
def compress_list(L):
    return {index: val for index, val in enumerate(L) if val != 0}


# 4
def expand_list(d, list_size):
    return [d.get(val, 0) for val in range(list_size)]


# 5
def letter_spans(s):
    return {char: s.rfind(char) - s.find(char) for char in set(s)}


# 6
def replace_all(text, table):
    for chars1, chars2 in table.items():
        text = text.replace(chars1, chars2)
    return text


# 7
def all_keys(d, val):
    return {key for key in d if d[key] == val}


# 8
def merge_counts(survey1, survey2):
    return {key: survey1.get(key, 0) + survey2.get(key, 0) for key in list(survey1) + list(survey2)}


def tester():
    print()

    print("1. five_dollar_store_total")
    print(102.5 == five_dollar_store_total(["Candy", "Smart Phone", "Pencil"]))
    print(112 == five_dollar_store_total(["Candy", "Book", "Sandwich", "Smart Phone"]))
    print(11.5 == five_dollar_store_total(["Candy", "Candy", "Candy", "Pencil", "Stapler"]))
    print()

    print("2. double_fish")
    menu1 = {"tuna fish": 10, "hamburger": 7, "bluefish": 15, "swordfish": 12, "spaghetti": 14}
    menu2 = {"tuna fish": 20, "hamburger": 7, "bluefish": 30, "swordfish": 24, "spaghetti": 14}
    print(double_fish(menu1) == menu2)
    menu1 = {"catfish": 8, "fish sticks": 5, "grilled cheese": 3, "soup": 4}
    menu2 = {"catfish": 16, "fish sticks": 10, "grilled cheese": 3, "soup": 4}
    print(double_fish(menu1) == menu2)
    print()

    print("3. compress_list")
    a = [0, 111, 0, 0, 444, 0, 0, 0, 0, 0]

    d1 = {1: 111, 4: 444}
    print(d1 == compress_list(a))
    b = [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 42]
    d2 = {50: 17, 99: 42, 0: 6}
    print(d2 == compress_list(b))
    print()

    print("4. expand_list")
    print(a == expand_list(d1, 10))
    print(b == expand_list(d2, 100))
    print()

    print("5. letter_spans")
    print(letter_spans("cbacbc") == {"a": 0, "b": 3, "c": 5})
    print(letter_spans("dictionaries are cool") == {'d': 0, 'i': 8, 'c': 15, 't': 0, 'o': 14, 'n': 0, 'a': 6, 'r': 6,
                                                    'e': 5, 's': 0, ' ': 4, 'l': 0})
    print()

    print("6. replace_all")
    print(replace_all("rabbits are fast", {"rabbits": "bunnies", "fast": "quick"}) == "bunnies are quick")
    print(replace_all("5 + [1 + 4] ** 2", {"[": "(", "]": ")", "**": "^"}) == "5 + (1 + 4) ^ 2")
    print(replace_all("1 + 2 + 3 + 3 + 2 + 1", {"1": "one", "2": "two", "3": "three",
                                                "+": "plus"}) == "one plus two plus three plus three plus two plus one")
    print()

    print("7. all_keys")
    d = {5: 10, 6: 11, 7: 10, 8: 11, 9: 10}
    print(all_keys(d, 10) == {7, 9, 5})
    print(all_keys(d, 11) == {6, 8})
    print(all_keys(d, 17) == set())
    print()

    print("8. merge_counts")
    ice_cream1 = {"chocolate": 5, "vanilla": 10, "strawberry": 15}
    ice_cream2 = {"chocolate": 2, "vanilla": 8, "rocky road": 3}
    ice_cream_total = merge_counts(ice_cream1, ice_cream2)
    print(ice_cream_total == {"chocolate": 7, "vanilla": 18, "strawberry": 15, "rocky road": 3})

    favorite_subject1 = {"science": 10, "math": 20}
    favorite_subject2 = {"math": 4, "english": 8, "lunch": 1000}
    favorite_subject_total = merge_counts(favorite_subject1, favorite_subject2)
    print(favorite_subject_total == {"science": 10, "math": 24, "english": 8, "lunch": 1000})


tester()
