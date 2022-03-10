import os
import shelve

path = os.path.realpath(__file__)
path = path[:path.rfind("/") + 1]

# 6. Open the same shelf file from before. Don't forget the import.
db = shelve.open(path + "data")

# 7. Write a loop that displays each player, and a list of their
# times. Please sort each list before you print it.
for user, times in db.items():
    print(f"User: {user} | Times: {sorted(times)}")

# 8. Close the shelf file.
db.close()
