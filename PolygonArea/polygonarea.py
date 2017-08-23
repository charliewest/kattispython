while True:
    number_of_points = int(input())

    if number_of_points == 0:
        exit() # This is the last TC

    x_list = []
    y_list = []

    for i in range(number_of_points):
        new_point = input().split()
        x_list.append(int(new_point[0]))
        y_list.append(int(new_point[1]))
    
    some_part = 0
    i = 0
    while i < number_of_points:
        if i + 1 < number_of_points:
            some_part += x_list[i] * y_list[i + 1] - x_list[i + 1] * y_list[i]
        else:
            some_part += x_list[i] * y_list[0] - x_list[0] * y_list[i]
        i += 1
    
    area = some_part / 2
    direction = "CCW" if area > 0 else "CW" 
    print(direction + " " + str(round(abs(area), 1)))
    