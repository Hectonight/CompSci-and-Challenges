import numpy as np
import pandas as pd
import random

print('This is a simulation based off the youtube video "Simulating the Evolution of Aggression" by Primer  '
      'https://www.youtube.com/watch?v=YNMkADpvO4w\n')

num_organisms = int(input("How many organisms are there?\n"))
num_cycles = int(input("How many cycles will this program go through?\n"))
percent = float(input("About what percentage of the organisms are pray?\n"))
num_of_food = int(input("How many pairs of food are there?\n"))
print()

percent /= 100
typing = np.random.choice(["pray", "predator"], size=num_organisms, p=[percent, 1 - percent])

organisms = pd.DataFrame(
    {
        "Type":
            [types for types in typing],
        "Food Num":
            None,
        "Survives":
            None
    }
)

food = pd.DataFrame(
    {
        "Organism One":
            [None for none in range(num_of_food)],
        "Organism Two":
            None
    }
)

print("Cycle", 0)
print("Total:", len(organisms))
print("Predators:", organisms["Type"].tolist().count("predator"))
print("Pray:", organisms["Type"].tolist().count("pray"))
print()

for cycle in range(num_cycles):
    organ = organisms.index.values.tolist()
    order = np.asarray(organ)
    np.random.shuffle(order)
    organisms.loc[:, "Food Num"] = None
    food.loc[:, "Organism One"] = None
    food.loc[:, "Organism Two"] = None
    possible_food = list(range(num_of_food))

    for organism in order:
        if len(possible_food) == 0:
            break
        food_num = random.choice(possible_food)
        if food.loc[food_num, "Organism One"] is None:
            food.loc[food_num, "Organism One"] = organism
            organisms.loc[organism, "Food Num"] = food_num
        else:
            food.loc[food_num, "Organism Two"] = organism
            organisms.loc[organism, "Food Num"] = food_num
            possible_food.remove(food_num)

    for organism in organ:
        if organisms.loc[organism, "Food Num"] is None:
            organisms.loc[organism, "Survives"] = True
            continue
        Typing1 = organisms.loc[organism, "Type"]
        Food_Num_Present = organisms.loc[organism, "Food Num"]
        Org1 = food.loc[Food_Num_Present, "Organism One"]
        Org2 = food.loc[Food_Num_Present, "Organism Two"]
        Other_Org = Org1 if Org1 != organism else Org2
        if Other_Org is not None:
            Typing2 = organisms.loc[Other_Org, "Type"]
            if Typing1 != Typing2:
                if Typing1 == "predator":
                    organisms.loc[organism, "Survives"] = True
                else:
                    organisms.loc[organism, "Survives"] = bool(random.randrange(2))
            else:
                if Typing1 == "predator":
                    organisms.loc[organism, "Survives"] = False
                else:
                    organisms.loc[organism, "Survives"] = True

        else:
            organisms.loc[organism, "Survives"] = True
            new_index = organisms.index.values.tolist()[-1] + 1
            organismsAdd = pd.DataFrame([[Typing1, None, True]], columns=["Type", "Food Num", "Survives"],
                                        index=[new_index])
            organisms = organisms.append(organismsAdd)

    #print()
    #print(organisms)
    #print()

    for organism in organ:
        if not organisms.loc[organism, "Survives"]:
            organisms = organisms.drop([organism])

    print("Cycle", cycle + 1)
    print("Total:", len(organisms))
    print("Predators:", organisms["Type"].tolist().count("predator"))
    print("Pray:", organisms["Type"].tolist().count("pray"))
    print()
