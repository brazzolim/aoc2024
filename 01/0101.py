# read input file
with open(r"C:\GitHub\aoc2024\01\01.txt") as f:
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
i=0
while i < len(leftCol):
    if leftCol[i] < rightCol[i]:
        totSum += rightCol[i] - leftCol[i]
    else:
        totSum += leftCol[i] - rightCol[i]
    i += 1

print(totSum)