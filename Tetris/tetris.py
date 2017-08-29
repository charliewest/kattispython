# Create the pieces

list_of_pieces = [
     [[0], [0, 0, 0, 0]],
     [[0, 0]],
     [[0, 0, 1], [1, 0]],
     [[1, 0, 0], [0, 1]],
     [[0, 0, 0], [1, 0], [1, 0, 1], [0, 1]],
     [[0, 0, 0], [2, 0], [0, 1, 1], [0, 0]],
     [[0, 0, 0], [0, 0], [1, 1, 0], [0, 2]]]

number_of_columns = 7
board = [0, 0, 0, 0, 0, 0, 0]

selected_piece = int(input()) - 1

number_of_possible_places = 0
column = 0
while column < number_of_columns:
    rotation_index = 0
    while rotation_index < len(list_of_pieces[selected_piece]):
        # Find the base
        rotation = list_of_pieces[selected_piece][rotation_index]
        base_index = rotation.index(0)
        print("Rotation " + str(rotation_index) + " has base index " + str(base_index))
        if column < base_index:
            # The piece will not fit with the base in this position
            break
        elif column + len(rotation) > number_of_columns:
            break
        base_board_index = column + base_index
        print("Evaluating " + str(column) + " for rotation " + str(rotation_index) + ", base at " + str(base_board_index))
        
        height_at_base = board[base_board_index]
        index = 0
        rotation_ok = True
        while index < len(rotation):
            if board[column - base_index + index] != height_at_base + rotation[index]:
                rotation_ok = False
                break
            index += 1
        if rotation_ok:
            number_of_possible_places += 1
        rotation_index += 1
    column += 1

print(number_of_possible_places)