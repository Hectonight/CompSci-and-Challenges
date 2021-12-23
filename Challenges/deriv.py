equation = input("Equation\n")


def derivative(eq):
    eqO = [oper for oper in str(eq) if oper in ["+", "-"]]
    eqS = eq.replace("-", "+").split("+")
    eqD = []
    eqF = []
    for sub in eqS:
        eqD.append(sub.split("x^") if "x^" in sub else sub.split("x"))
    for sub in eqD:
        eqF.append(str(int(sub[0]) * int(sub[1])) + "x^" + str(int(sub[1]) - 1))
    count = 0
    while len(eqF) > 2:
        eqF = [eqO[count].join(eqF[0:2])] + eqF[2:]
        count += 1
    Final = eqO[-1].join(eqF)
    Final = Final.replace("x^1+", "x+")
    Final = Final.replace("x^1-", "x-")
    Final = Final.replace("x^0", "")
    return Final


print(derivative(equation))
