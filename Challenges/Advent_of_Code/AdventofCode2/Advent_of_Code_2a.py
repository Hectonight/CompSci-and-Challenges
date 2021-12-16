file = open("AdventofCode2", "r").read().split("\n")
horiz, depth = 0, 0

for num in file:
    change = num.replace("up ", "-").replace("down ", "").split(" ")
    if change[0] == "forward":
        horiz += int(change[1])
    else:
        depth += int(change[0])

print("Horizantal:", horiz)
print("Depth:", depth)
print("Horizantal * Depth:", depth * horiz)
