def digit_to_eng(digit):
    if type(digit) != int:
        raise TypeError('digit is not type int')
    if len(str(digit)) != 1:
        raise Exception('digit is not in range of 0-9')

    eng = None

    if digit == 1:
        eng = 'one'
    elif digit == 2:
        eng = 'two'
    elif digit == 3:
        eng = 'three'
    elif digit == 4:
        eng = 'four'
    elif digit == 5:
        eng = 'five'
    elif digit == 6:
        eng = 'six'
    elif digit == 7:
        eng = 'seven'
    elif digit == 8:
        eng = 'eight'
    elif digit == 9:
        eng = 'nine'

    return eng


def num_to_eng(num):
    if type(num) != int:
        raise TypeError('number is not type int')
    if num not in range(1, 1000):
        raise Exception('number is not in range of 1-999')
    skip_two = False
    final_ans = []
    count = len(str(num))

    for digit_str in str(num):
        digit = int(digit_str)
        eng_digit = digit_to_eng(int(digit))
        if eng_digit is not None or skip_two:
            if count == 2 and digit != 1:
                if digit == 2:
                    eng_digit = 'twenty'
                elif digit == 3:
                    eng_digit = 'thirty'
                elif digit == 8:
                    eng_digit += 'y'
                else:
                    eng_digit += 'ty'
            if skip_two:
                if digit == 0:
                    eng_digit = 'ten'
                if digit == 1:
                    eng_digit = 'eleven'
                if digit == 2:
                    eng_digit = 'twelve'
                if digit == 3:
                    eng_digit = 'thirteen'
                if digit == 5:
                    eng_digit = 'fifteen'
                if digit == 8:
                    eng_digit = 'eighteen'

            if count == 3:
                final_ans.append(eng_digit)
                final_ans.append('hundred')
            elif digit != 1 or count != 2:
                final_ans.append(eng_digit)
            else:
                skip_two = True
        count -= 1

    return ' '.join(final_ans)


output = num_to_eng(int(input('Number 1-999: ')))
print(output)
