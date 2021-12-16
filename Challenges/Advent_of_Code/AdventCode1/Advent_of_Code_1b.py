file = open("AdventofCode1", "r").read().split("\n")
count = 0

for data in range(1, len(file) - 2):
    count += int(file[data])+int(file[data+1])+int(file[data+2]) > int(file[data - 1]) + int(file[data]) + int(file[data + 1])
print(count)
