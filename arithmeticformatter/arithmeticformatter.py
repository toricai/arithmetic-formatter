
# length of dashes is 2 more characters than the largest number

def arithmetic_arranger(arr, answers = False):
    """Plan:
    print one line at a time
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

    # max number length = n
    # print top line
    # right justified numbers (width n+2), 4 characters of padding in between
    for n in range(0, len(top)):
        if n != 0:
            print("    ", end='')
        print(top[n].rjust(maxlength[n] + 2), end='')

    print()

    # print second line
    # one-character operator, right-justified numbers (width n+1), 4 char padding
    for n in range(0, len(operator)):
        if n != 0:
            print("    ", end='')
        print(operator[n], end='')
        print(bottom[n].rjust(maxlength[n] + 1), end='')

    print()

    # print dashes
    # dashes (width n+2), 4 char padding
    for n in range(0, len(top)):
        if n != 0:
            print("    ", end='')
        print("-" * (maxlength[n] + 2), end='')

    print()

    # print answers
    # compute answers with an if statement
    # right justified answers (width n+2), 4 characters of padding in between
    if answers:
        for n in range(0, len(top)):
            if operator[n] == '+':
                answer = int(top[n]) + int(bottom[n])
            else:
                answer = int(top[n]) - int(bottom[n])

            if n != 0:
                print("    ", end='')
            print(str(answer).rjust(maxlength[n] + 2), end='')

    print("""

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474

""")



arithmetic_arranger( ["32 - 698", "3801 - 2", "45 + 43", "123 + 49"], True)

# x = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----