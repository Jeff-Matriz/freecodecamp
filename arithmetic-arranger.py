import operator

#valid operations
ops = {"+": operator.add, "-": operator.sub}

def arithmetic_arranger(problems, compute):
    if len(problems) > 5:
        return "Error: Too many problems."
    toptier = ""
    bottomtier = ""
    lines = ""
    totals = ""
    for n in problems:
        number0 = n.split()[0]
        operator = n.split()[1]
        number1 = n.split()[2]

        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        if not number0.isdigit() or not number1.isdigit():
            return "Error: Numbers must only contain digits."
        if len(number0) > 4 or len(number1) > 4:
            return "Error: Numbers cannot be more than four digits"

        total = ops[operator](int(number0), int(number1))
        operatorDistance = max(len(number0), len(number1)) + 2

        number1 = operator + number1.rjust(operatorDistance - 1)
        toptier = toptier + number0.rjust(operatorDistance) + (4 * " ")
        bottomtier = bottomtier + number1 + (4 * " ")
        lines = lines + len(number1) * "_" + (4 * " ")
        totals = totals + str(total).rjust(operatorDistance) + (4 * " ")
    if compute:
        print(toptier)
        print(bottomtier)
        print(lines)
        print(totals)


if __name__ == "__main__":
    print("Enter operations[x + y]:")
    count = 1
    list = []       
    
    def start():
        global count
        x = input(f"Entry{count}: ")
        list.append(x)
        
        count = count + 1
        y = input("Add more? y/n: ")
        if y == 'y':
            start()
        else:
            arithmetic_arranger(list, True)
            
start()