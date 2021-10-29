# Proof of correct results for num_recipricals
# CodingBat returns timed out for some reason but the code runs instantly

def num_reciprocals(goal):
    count = 0
    sum = 0
    while goal > sum:
        count += 1
        sum += (1 / count)

    return count


print(num_reciprocals(1), "Should Be: 1")
print(num_reciprocals(2), "Should Be: 4")
print(num_reciprocals(3), "Should Be: 11")
print(num_reciprocals(4), "Should Be: 31")
print(num_reciprocals(5), "Should Be: 83")
print(num_reciprocals(10), "Should Be: 12367")
