import os
import time
import random
import shelve

path = os.path.realpath(__file__)
path = path[:path.rfind("/") + 1]

# 1. Create a new shelf file here. Don't forget the import.
db = shelve.open(path + "data")

print("Math problem game! Try to get the answer as fast as possible.")
print("For each prompt, enter an answer, or type any letter to quit.")
print()
username = input("Enter your username. ")

# 2. Create an empty list for all the times. - Comment Made more Permanent Solution
times = db.get(username, [])

while True:

    a = random.randrange(1, 10)
    b = random.randrange(1, 10)
    c = a + b

    # 3. Add code around the line "entry = ..." to get the time
    # it takes the user to enter the answer. Hint, time.time()
    # will return the current time since midnight 1/1/1970, at the 
    # instant the function is called. You can use this function,
    # with some variables etc. to find the time in seconds
    # that the input step takes. Please round to 1 decimal place.

    t1 = time.time()
    entry = input("Solve: " + str(a) + " + " + str(b) + " = ")
    t2 = time.time()
    timeTaken = round(t2-t1, 1)

    try:
        entry = int(entry)
    except:
        break

    if entry == c:
        print("Right! Your time will be recorded.")

        # 4. Add the time to the list of times that you created in Step 2.
        times.append(timeTaken)
    else:
        print("Wrong! Your time will not be recorded.")

# 5. Create an entry in the log. Key: Username. Value: List of times.
db[username] = times

# 6. Close the shelf file.
db.close()
