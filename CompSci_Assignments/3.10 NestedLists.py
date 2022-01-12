print("3.10 Homework: Nested list problems")
print("For all problems please use the list variable.")
print("For example, on #1, do not just print 'E', use the list variable words for full credit.")
print()
print()

words = ["Math", "Science", "English", "History", "Phys Ed"]

print("#1 -- #5")
print("words = ", words)
print()
print()

print("1. Print the E in 'English'")

print(words[2][0])

print("2. Print the d at the end of 'Phys Ed'. Please use negative indices.")

print(words[-1][-1])

print("3. Print the last 3 items: English History, Phys Ed, on separate lines.")

for word in words[2:]:
    print(word)

print("4. Create a list with the number of words in each subject.")
print("Should be [1, 1, 1, 1, 2]. Hint, count the spaces.")
print("Print the list when done.")

print([1 + word.count(" ") for word in words])

print("5. Create a new list with the abbreviated words, which are the first")
print("three letters of each word, in all-caps. Should be: ['MAT', 'SCI', 'ENG', 'HIS', 'PHY']")
print("Print this list when done.")

print([word[:3].upper() for word in words])
print()

nums = [[10, 20], [[5, 6], [7, 8]]]

print("#6 -- #15:")
print("nums = ", nums)

print("6. Loop over nums and print each item.")
for num in nums[0]:
    print(num)
for nums1 in nums[1]:
    for num in nums1:
        print(num)

print("7. Print the 10.")

print(nums[0][0])

print("8. Print the 20.")

print(nums[0][1])

print("9. Print the [5, 6]")

print(nums[1][0])

print("10. Print the [7, 8]")

print(nums[1][1])

print("11. Print the 5.")

print(nums[1][0][0])

print("12. Print the 8.")

print(nums[1][1][1])

print("13. Add a list to nums so that nums is now:")
print("[[10, 20], [[5, 6], [7, 8]], [1, 2, 3]]")
print("Please use append.")
print("Print the new list when done.")

nums.append([1, 2, 3])
print(nums)

print("14. Add a list [9, 10] to the [[5, 6], [7, 8]] part")
print("So that the whole list is now:")
print("[[10, 20], [[5, 6], [7, 8], [9, 10]], [1, 2, 3]]")
print("Please use append.")
print("Print the new list when done.")

nums.insert(-1, [9, 10])
print(nums)

print("15. Add 30 to the [10, 20] part")
print("So that the whole list is now:")
print("[[10, 20, 30], [[5, 6], [7, 8], [9, 10]], [1, 2, 3]]")
print("Please use append.")
print("Print the new list when done.")

nums[0].append(30)
print(nums)
