from itertools import combinations


def KillerSudokuCalc(total: int, number_of_nums: int, Not=None):
    if Not is None:
        Not = []
    FinalRange = [num for num in list(range(1, 10)) if num not in Not]
    FinalLst = list(combinations(FinalRange, number_of_nums))
    FinalLst = [combination for combination in FinalLst if sum(combination) == total]
    return FinalLst


print(KillerSudokuCalc(10, 3, [4, 6, 9]))
print(KillerSudokuCalc(16, 3, [4, 2, 6, 9]))
