n = int(input("Enter a number. "))
count = 0
maximum = 0

while n != 1:
    n = n // 2 if n % 2 == 0 else 3*n+1
    count += 1
    maximum = max(maximum, n)

print("Total steps: " + str(count))
print("Maximum n: " + str(maximum))
