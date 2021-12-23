equation = input("Equation\n")


def derivative(eq):
    if "x" not in eq:
        return "0"
    eqS = eq.replace("-", "+-")
    eqS = eqS.replace("^+-", "^-")
    if eqS.startswith("+"):
        eqS = eqS[1:]

    eqS = eqS.split("+")
    for sub in range(len(eqS)):
        eqS[sub] = eqS[sub].split("x^") if "x^" in eqS[sub] else eqS[sub].split("x")
    eqF = []
    for sub in eqS:
        if len(sub) == 1:
            continue
        if sub[1] == "":
            if sub[0] in ["", "-"]:
                eqF.append(sub[0]+"1")
            else:
                eqF.append(sub[0])

        else:
            eqF.append(str(int(sub[0]) * int(sub[1])) + "x^" + str(int(sub[1]) - 1))

    print(eqS, eqF)
    Final = "+".join(eqF)
    Final.replace("+-", "-")
    Final = Final.replace("+-", "-")
    for op in ["+", "-"]:
        Final = Final.replace(f"x^1{op}", f"x{op}")
        Final = Final.replace(f"{op}1x", f"{op}x")
        Final = Final.replace(f"{op}0x", "")

    Final = Final.replace("x^0", "")
    Final = 0 if Final == "" else Final

    return Final


print(derivative(equation))
