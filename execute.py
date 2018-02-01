def parse_token(token):
    token = token.split()
    return token

def number_is_int(a1,a2):
    return (not '.' in str(a1) and not '.' in str(a2))

def execute(line):
    line = parse_token(line)
    print(line)
    id=0
    arr=[]
    tmpRes="empty"
    for item in line:
        if id>=2:
            if (id == 2):
                arr.append(float(line[id - 2])) if '.' in line[id-2] else arr.append(int(line[id-2]))
                arr.append(float(line[id - 1])) if '.' in line[id - 1] else arr.append(int(line[id - 1]))
            if item=='+':
                a1 = arr.pop()
                a2 = arr.pop()
                if number_is_int(a1, a2):
                    tmpRes = int(a2) + int(a1)
                else:
                    tmpRes = float(a2) + float(a1)
            if item=='-':
                a1 = arr.pop()
                a2 = arr.pop()
                if number_is_int(a1, a2):
                    tmpRes = int(a2) - int(a1)
                else:
                    tmpRes = float(a2) - float(a1)
            if item=='*':
                a1 = arr.pop()
                a2 = arr.pop()
                if number_is_int(a1, a2):
                    tmpRes = int(a2) * int(a1)
                else:
                    tmpRes = float(a2) * float(a1)
            if item=='/':
                a1 = arr.pop()
                a2 = arr.pop()
                if number_is_int(a1, a2):
                    tmpRes = int(int(a2) / int(a1))
                else:
                    tmpRes = float(a2) / float(a1)
            arr.append(item) if tmpRes=="empty" else arr.append(tmpRes)
            tmpRes="empty"
        id+=1
    if id == 2:
        return "Error. Incorrect input line."
    return arr.pop()
