# read input file
# with open(r"C:\GitHub\aoc2024\02\02_test.txt") as f:
with open(r"C:\GitHub\aoc2024\02\02.txt") as f:
    lines = f.readlines()

reports = []
for line in lines:
    line = line.strip()
    line = line.split()
    
    reports.append([int(numeric_string) for numeric_string in line])
#make array of int
# reports = [int(i) for i in reports]
sumSafe = 0
safeReports = []
# print(reports)
for report in reports:
    isSafe = False
    if ((report == sorted(report, reverse = True)) or (report == sorted(report, reverse = False)) ):
        for i in range(len(report)):
            try:
                level = report[i]
                nextLevel = report[i+1]
                diffLevels = abs(level - nextLevel)
                if (diffLevels <= 3 and diffLevels >= 1) :
                    isSafe = True
                else:
                    isSafe = False
                    break
            except:
                continue
    if isSafe == True:
        safeReports.append(report)
# print(safeReports)
print(len(safeReports))