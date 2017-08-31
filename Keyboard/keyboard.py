rows_cols = [int(n) for n in input().split()]

keyboard = []

for row_index in range(rows_cols[0]):
    keyboard.append([c for c in input()])

current_pos = (0, 0)
cost = 0
for character in input() + "*": # Get the WORD, add an asterisk for enter
    # Get target row and col
    low_column_index = 0
    for row_index, row in enumerate(keyboard):
        try:
            low_column_index = row.index(character)
            break
        except ValueError:
            pass
    print("Found the letter {} at [{}][{}]".format(keyboard[row_index][low_column_index],
                                                     row_index,
                                                     low_column_index))
    cost += 1 + abs(row_index - current_pos[0]) + \
            abs(low_column_index - current_pos[1])
    current_pos = (row_index, low_column_index)


print(cost)
print(keyboard)
    