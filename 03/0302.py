import re
# read input file
count = 0
sections = []
# with open(r"C:\GitHub\aoc2024\03\03_test.txt") as f:
with open(r"C:\GitHub\aoc2024\03\03.txt") as f:
    lines = f.readlines()
    for line in lines:
        sections.append(line.strip())

totSum = 0
oneLineStr = ""
for section in sections:
    oneLineStr += section
toTmpString = True

list_match = re.findall(r'mul\([0-9]+\,[0-9]+\)|don\'t\(\)|do\(\)', oneLineStr)
# print("tmpString",tmpString)
parsedSection = "".join(list_match)
parsedSection = parsedSection.replace("don't()", "|").replace("do()","=")
print("parsedSection:", parsedSection)
i = 0
tmpString = ""
while i < len(parsedSection):
    if parsedSection[i] == "|":
        toTmpString = False
    if parsedSection[i] == "=":
        toTmpString = True
    if toTmpString and parsedSection[i] != "=":
        tmpString += parsedSection[i]
    i += 1
print("tmpString:", tmpString)
listTmp = (tmpString.replace("mul",";")).split(";")
listTmp.pop(0)
for coppia in listTmp:
    coppia = coppia.replace("(", "").replace(")", "").split(",")
    #make list of str in list of int
    coppia = [int(i) for i in coppia]
    # print("coppia:", coppia)
    totSum += coppia[0]*coppia[-1]

print("totSum:", totSum)