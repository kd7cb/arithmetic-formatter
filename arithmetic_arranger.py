def arithmetic_arranger(problems, tof = False):
    #check problem length
    arranged_problems = ""
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
        exit()

    #check if contains other operator
    for i in range(len(problems)):
        if problems[i].find('/') == -1 and problems[i].find('*') == -1:
            pass
        else:
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems
            exit()

    dataMatrix = [dict() for x in range(len(problems))]
    #dataMatrix = [{'top':0,'op':"0",'bot':0} for k in range(len(problems))]

    for i in range(len(problems)):
        dataMatrix[i] = {
            idx: ele
            for idx, ele in enumerate(problems[i].split(" "))
        }

    #[i][0] = top operand
    #[i][1] = operator
    #[i][2] = bottom operand

    #check number of digits
    for i in range(len(problems)):
        if len(dataMatrix[i][0]) > 4 or len(dataMatrix[i][2]) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems
            exit()

    #check numbers contain digits
    for i in range(len(problems)):
        if dataMatrix[i][0].isdigit() == False or dataMatrix[i][2].isdigit(
        ) == False:
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems
            exit()

    #generate lines
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for i in range(len(problems)):
        if len(dataMatrix[i][0]) > len(dataMatrix[i][2]):
            longest = len(dataMatrix[i][0])
        else:
            longest = len(dataMatrix[i][2])

        topspace = " " * (longest + 2 - len(dataMatrix[i][0]))
        botspace = " " * (longest - len(dataMatrix[i][2]) + 1)
        answer = str(eval(dataMatrix[i][0] + dataMatrix[i][1] + dataMatrix[i][2]))

        if i == len(problems)-1:
            line1 = line1 + topspace + dataMatrix[i][0]
            line2 = line2 + dataMatrix[i][1] + botspace + dataMatrix[i][2]
            line3 = line3 + "-" * (longest + 2)
            line4 = line4 + " "*(longest+2-len(answer)) + answer
        else:
            line1 = line1 + topspace + dataMatrix[i][0] + " " * 4
            line2 = line2 + dataMatrix[i][1] + botspace + dataMatrix[i][2] + " " * 4
            line3 = line3 + "-" * (longest + 2) + " " * 4
            line4 = line4 + " "*(longest+2-len(answer)) + answer + " "*4

    if tof == True:
        arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    else:
        arranged_problems = line1 + '\n' + line2 + '\n' + line3

    return arranged_problems
