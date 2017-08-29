list_of_pieces = [
     [[0], [0, 0, 0, 0]],
     [[0, 0]],
     [[0, 0, 1], [1, 0]],
     [[1, 0, 0], [0, 1]],
     [[0, 0, 0], [1, 0], [1, 0, 1], [0, 1]],
     [[0, 0, 0], [2, 0], [0, 1, 1], [0, 0]],
     [[0, 0, 0], [0, 0], [1, 1, 0], [0, 2]]]

input_list = input().split()

c = int(input_list[0]) # number of columns
p = int(input_list[1]) # piece number

board = [int(v) for v in input().split()]

piece_index = p - 1

# print(list_of_pieces[p - 1])
# print(board)

number_of_possible_positions = 0

rotation_i = 0
for rotation in list_of_pieces[piece_index]: # check each rotation by itself
    
    # print("Evaluating between 0 and {} for rotation {}.".format(len(board) - len(rotation), rotation_i))
    
    for evaluated_index in range((len(board) - len(rotation)) + 1):
        # go through the different positions
        # print("Testing board index {}.".format(evaluated_index, rotation_i))

        test_arr = []
        
        for evaluated_piece_index in range(len(rotation)):
            test_arr.append(board[evaluated_index + evaluated_piece_index] -
                            rotation[evaluated_piece_index])
        
        if len(set(test_arr)) == 1:
            ## By putting the elements in a set we remove duplicates 
            # print("We have a match for rotation {} on index {}".format(rotation_i, evaluated_index))
            number_of_possible_positions += 1
            
        # print(test_arr)
        
    rotation_i += 1
    
print(number_of_possible_positions)