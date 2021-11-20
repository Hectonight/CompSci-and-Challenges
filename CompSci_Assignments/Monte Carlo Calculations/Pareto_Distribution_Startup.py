from random import paretovariate


def trial(alpha):
    p = paretovariate(alpha)
    income = 2 * (p - 1)
    return income - 5


alphas = [1.1, 1.25, 2.0, 2.5, 2.8, 3, 5.0]
for alpha1 in alphas:
    incomes = []
    if alpha1 != 1.1:
        print()
    print("Alpha of", alpha1)
    for num in range(1000):
        incomes.append(trial(alpha1))
    net = sum(incomes)
    over5 = len([gain for gain in incomes if gain > 0])
    over50 = len([gain for gain in incomes if gain > 45])
    print("The net profit made by the venture capital firm was", net)
    print("The number of startups out of 1000 where f was over 5 was", over5)
    print("The number of startups out of 1000 where f was over 50 was", over50)
