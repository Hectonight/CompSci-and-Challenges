import os
import json

path = os.path.realpath(__file__)
path = path[:path.rfind("/") + 1]

f = open(path + "formulas.json", "w")

equations = dict()
while True:
    equation = input("Enter the name of a new formula. ")
    if "q" == equation:
        break
    equations[equation] = {
        "Equation": input("Equation: "),
        "Use": input("Use to: ")
    }


f.write(json.dumps(equations))
f.close()
