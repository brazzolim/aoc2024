# read input file
with open(r"C:\GitHub\aoc\2024\01\01.txt") as f:
    lines = f.readlines()

leftCol = []
rightCol = []
for line in lines:
    line = line.strip()
    # print(line.split())
    leftCol.append(line.split()[0])
    rightCol.append(line.split()[-1])

#make int values in array
leftCol = [int(i) for i in leftCol]
rightCol = [int(i) for i in rightCol]

#order the lists
leftCol = sorted(leftCol)
rightCol = sorted(rightCol)

totSum = 0
for i in range(len(leftCol)):
    this_totValuesEquals = []
    valueToCheck = leftCol[i]
    for j in range(len(rightCol)):
        if rightCol[j] == valueToCheck:
            this_totValuesEquals.append(valueToCheck)
    totSum += valueToCheck*len(this_totValuesEquals)

print(totSum)