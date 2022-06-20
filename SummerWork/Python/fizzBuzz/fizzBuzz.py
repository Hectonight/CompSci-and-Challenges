def fizzbuzz(n):
    nums = []
    for num in range(1, n):
        if not num % 3:
            if not num % 5:
                nums.append("FizzBuzz")
            else:
                nums.append("Fizz")
        elif not num % 5:
            nums.append("Buzz")
        else:
            nums.append(num)
    return nums