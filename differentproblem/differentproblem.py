output = []
while True:
    inputstring = input()
    if len(inputstring) > 0:
        pairsplit = inputstring.split()
        output.append(abs(int(pairsplit[0]) - int(pairsplit[1])))
    else:
        break

for line in output:
    print(line)
