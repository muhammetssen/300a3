import random as rand


def QueensLasVegas(n):
    r = 0
    column = []
    chosens = []
    avail_columns = [x for x in range(n)]
    logs = []
    while len(avail_columns) != 0 and r <= (n-1):
        avail_columns = [x for x in range(n)]
        unaval = set({})
        for i in range(len(chosens)):
            unaval.add(chosens[i])
            swift = r-i

            if chosens[i]-swift >= 0:
                unaval.add(chosens[i]-swift)

            if chosens[i]+swift < n:
                unaval.add(chosens[i]+swift)

        for c in unaval:
            avail_columns.remove(c)

        if len(avail_columns) == 0:
            return None, logs
        logs.append(f"Step {r+1}: Columns: {column}")
        logs.append(f"Step {r+1}: Available: {avail_columns}")

        chosen = rand.choice(avail_columns)
        chosens.append(chosen)
        column.append(chosen)
        r += 1

    return column, logs


values = [6, 8, 10,16]


def runner(n):
    for value in values:
        solution, logs = QueensLasVegas(value)
        with open(f"result_{value}.txt", 'w+') as f:
            if solution == None:
                f.write("Unsuccessful\n")
            else:
                f.write("Successful\n")
            f.write("\n".join(logs))
            f.write("\n")
            if solution != None:
                f.write(f"Step {value+1}: Columns = {solution}")


def propabilities():
    for value in values:
        count = 0
        for i in range(10000):
            solution, logs = QueensLasVegas(value)
            if solution != None:
                count += 1
        print(f"LasVegas algorithm With n = {value}")
        print(f"Number of successful placements is {count}")
        print("Number of trials is 10000")
        print(f"Probabilty that it will come to a solution is {count / 10000}")


def result_mini():
    for value in values:
        s = 0
        us = 0
        while s < 2:
            solution, logs = QueensLasVegas(value)
            if solution == None:
                continue
            s += 1
            with open(f"result_mini.txt", 'a+') as f:
                f.write(f"n={value}, ")
                f.write("Successful\n")
                f.write("\n".join(logs))
                f.write("\n")
                f.write(f"Step {value+1}: Columns = {solution}\n")
                f.write("\n")
        while us < 2:
            solution, logs = QueensLasVegas(value)
            if solution != None:
                continue
            us += 1
            with open(f"result_mini.txt", 'a+') as f:
                f.write(f"n={value}, ")
                f.write("Unsuccessful\n")
                f.write("\n".join(logs))
                f.write("\n\n\n")

# result_mini()
propabilities()