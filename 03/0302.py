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
acceptableValues = []
notAcceptableValues = []
for section in sections:
    print("section: ",section)
    # while "don't" in section:
    parsedSection = section.replace("don't()", "|").replace("do()","=")
    print("parsedSection:", parsedSection)
    parsedSectionList = parsedSection.split("|")
    i = 0
    j = 0
    tmpString = ""
    toTmpString = True
    while i < len(parsedSection):
        # this_mulvalue = re.findall("mul\([0-9]+\,[0-9]+\)", parsedSectionList[i])
        if parsedSection[i] == "|":
            toTmpString = False
            # i += 1
            # break
        if parsedSection[i] == "=":
            toTmpString = True
        if toTmpString and parsedSection[i] != "=":
            tmpString += parsedSection[i]
        i += 1
    
    print("tmpString",tmpString)
    this_mulvalue = re.findall("mul\([0-9]+\,[0-9]+\)", tmpString)
    # print("this_mulvalue:", this_mulvalue)
    for mulvalue in this_mulvalue:
        print("mulvalue:", mulvalue)
        mulvalue = mulvalue.replace("mul(", "").replace(")", "").split(",")
        mul = int(mulvalue[0])*int(mulvalue[-1])
        totSum += mul
    # parsedSectionList = parsedSection.split("|")
    # for i in range(len(parsedSectionList)):
    #     if  i % 2 == 0:
    #         this_mulvalue = re.findall("mul\([0-9]+\,[0-9]+\)", parsedSectionList[i])
    #         acceptableValues.append(this_mulvalue)
    #         # notAcceptableValues.append()
    #         print("this_mulvalue:", this_mulvalue)
    # for sublist in acceptableValues:
    #     for mulvalue in sublist:
    #         mulvalue = mulvalue.replace("mul(", "").replace(")", "").split(",")
    #         totSum += int(mulvalue[0])*int(mulvalue[-1])

print("totSum:", totSum)


# no 389966681, too high
# no 107307267, too high
# no 29279936, too low