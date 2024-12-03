import re
# read input file
count = 0
sections = []
with open(r"C:\GitHub\aoc2024\03\03_test.txt") as f:
# with open(r"C:\GitHub\aoc2024\03\03.txt") as f:
    lines = f.readlines()
    for line in lines:
        sections.append(line.strip())

totSum = 0
allMulValues = []
for section in sections:
    print(section)
    this_mulvalue = re.findall("mul\([0-9]+\,[0-9]+\)", section)
    # print(this_mulvalue)
    for mulvalue in this_mulvalue:
        mulvalue = mulvalue.replace("mul(", "").replace(")", "").split(",")
        # print(mulvalue)
        totSum += int(mulvalue[0])*int(mulvalue[-1])

print(totSum)