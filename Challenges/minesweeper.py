def num_grid(lst):
    final_lst = lst
    num_row = -1

    for row in lst:
        num_row += 1
        number = -1
        for num in row:
            number += 1
            if num != '#':
                final_lst[num_row][number] = '0'
                if number != 0:
                    if final_lst[num_row][number - 1] == '#':
                        final_lst[num_row][number] = str(int(final_lst[num_row][number]) + 1)
                if number != 4:
                    if final_lst[num_row][number + 1] == '#':
                        final_lst[num_row][number] = str(int(final_lst[num_row][number]) + 1)
                if num_row != 0:
                    if final_lst[num_row - 1][number] == '#':
                        final_lst[num_row][number] = str(int(final_lst[num_row][number]) + 1)
                    if number != 0:
                        if final_lst[num_row - 1][number - 1] == '#':
                            final_lst[num_row][number] = str(int(final_lst[num_row][number]) + 1)
                    if number != 4:
                        if final_lst[num_row - 1][number + 1] == '#':
                            final_lst[num_row][number] = str(int(final_lst[num_row][number]) + 1)
                if num_row != 4:
                    if final_lst[num_row + 1][number] == '#':
                        final_lst[num_row][number] = str(int(final_lst[num_row][number]) + 1)
                    if number != 0:
                        if final_lst[num_row + 1][number - 1] == '#':
                            final_lst[num_row][number] = str(int(final_lst[num_row][number]) + 1)
                    if number != 4:
                        if final_lst[num_row + 1][number + 1] == '#':
                            final_lst[num_row][number] = str(int(final_lst[num_row][number]) + 1)

    return final_lst


var = num_grid([
    ['-', '-', '#', '-', '-'],
    ['-', '#', '-', '-', '#'],
    ['-', '-', '#', '#', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-']
])

for row in var:
    print(row)