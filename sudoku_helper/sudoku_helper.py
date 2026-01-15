def possible_numbers(row, column, box):

    all_digits = set(range(1, 10))

    row_set = {n for n in row if n != 0}
    column_set = {n for n in column if n != 0}
    box_set = {n for n in box if n != 0}

    used_digits = row_set | column_set | box_set

    possible = all_digits - used_digits

    return sorted(possible)



row =    [5, 3, 0, 0, 7, 0, 0, 0, 0]
column = [6, 0, 0, 1, 9, 5, 0, 0, 0]
box =    [5, 3, 0, 6, 0, 0, 0, 9, 8]

result = possible_numbers(row, column, box)
print("Possible numbers:", result)