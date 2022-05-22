
# length of dashes is 2 more characters than the largest number

def arithmetic_arranger(arr, answers = False):
    """Plan:
    solution += one line at a time
    max number length = n
    first line: right justified numbers (width n+2), 4 characters of padding in between
    second line: one-character operator, right-justified numbers (width n+1), 4 char padding
    third line: dashes (width n+2), 4 char padding
    """

    top = []
    operator = []
    bottom = []
    maxlength = []
    solution = ''

    for operation in arr:
        split = operation.split(" ")

        top.append(split[0])
        operator.append(split[1])
        bottom.append(split[2])

    # Error checking
    if len(operator) > 5:
        raise ValueError("Too many problems.")
    
    okops = ['+', '-']
    for x in operator:
        if x not in okops:
            raise ValueError("Operator must be '+' or '-'.")

    if len(max(top, key=len)) > 4 or len(max(bottom, key=len)) > 4:
        raise ValueError("Numbers canot be more than four digits.")

    numberstop= all(map(str.isdigit, top))
    numbersbottom = all(map(str.isdigit, bottom))
    if numberstop == False or numbersbottom == False:
        raise ValueError("Numbers must only contain digits.")

    # set max length array
    for n in range(0, len(top)):
        maxlength.append(len(top[n]))
        if (len(bottom[n]) > maxlength[n]):
            maxlength[n] = len(bottom[n])

    # create top line
    # (max number length = n)
    # right justified numbers (width n+2), 4 characters of padding in between
    for n in range(0, len(top)):
        if n != 0:
            solution += "    "
        solution += top[n].rjust(maxlength[n] + 2)

    solution += "\n"

    # add second line
    # one-character operator, right-justified numbers (width n+1), 4 char padding
    for n in range(0, len(operator)):
        if n != 0:
            solution += "    "
        solution += operator[n]
        solution += bottom[n].rjust(maxlength[n] + 1)

    solution += "\n"

    # add dashes
    # dashes (width n+2), 4 char padding
    for n in range(0, len(top)):
        if n != 0:
            solution += "    "
        solution += "-" * (maxlength[n] + 2)

    # add answers
    # compute answers with an if statement
    # right justified answers (width n+2), 4 characters of padding in between
    if answers:
        solution += "\n"
        for n in range(0, len(top)):
            if operator[n] == '+':
                answer = int(top[n]) + int(bottom[n])
            else:
                answer = int(top[n]) - int(bottom[n])

            if n != 0:
                solution += "    "
            solution += str(answer).rjust(maxlength[n] + 2)

    return solution

# functional test
x = ["32 - 698", "3801 - 2", "45 + 43", "123 + 49"]
ret = arithmetic_arranger(x, True)

print(ret)

assert ret == """   32      3801      45      123
- 698    -    2    + 43    +  49
-----    ------    ----    -----
 -666      3799      88      172""", "Return value didn't match what was expected"