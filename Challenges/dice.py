def dice(num):
    if num == 0:
        return ''
    num_left = num
    num_di = num / 6
    num_di = int(num_di) + 1 if int(num_di) < num_di else int(num_di)
    dice_coords = []
    for num in range(num_di):
        dice_coords.append([['-', '-', '-'],
                            ['-', '-', '-'],
                            ['-', '-', '-']])

    for di in dice_coords:
        num_use = 6 if num_left > 6 else num_left

        num_left -= num_use
        if num_use == 6:
            di[0][0] = 'O'
            di[0][2] = 'O'
            di[1][0] = 'O'
            di[1][2] = 'O'
            di[2][0] = 'O'
            di[2][2] = 'O'
        if num_use == 5:
            di[0][0] = 'O'
            di[0][2] = 'O'
            di[1][1] = 'O'
            di[2][0] = 'O'
            di[2][2] = 'O'
        if num_use == 4:
            di[0][0] = 'O'
            di[0][2] = 'O'
            di[2][0] = 'O'
            di[2][2] = 'O'
        if num_use == 3:
            di[0][0] = 'O'
            di[1][1] = 'O'
            di[2][2] = 'O'
        if num_use == 2:
            di[0][0] = 'O'
            di[2][2] = 'O'
        if num_use == 1:
            di[1][1] = 'O'
    final_answ = ''
    first_di = True
    for di in dice_coords:
        first_row = True
        if not first_di:
            final_answ += ', '
        first_di = False
        for row in di:
            if not first_row:
                final_answ += '/'
            final_answ += f'{row[0]}{row[1]}{row[2]}'
            first_row = False

    return final_answ


print(dice(9))
