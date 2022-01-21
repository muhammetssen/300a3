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


values = [6, 8, 10]


def runner():
    for value in values:
        count = 0
        s = 0
        us = 0
        for i in range(10000):
            solution, logs = QueensLasVegas(value)
            with open(f"result_{value}.txt", 'a+') as f:
                if solution == None:
                    f.write("Unsuccessful\n")
                    if us < 2:
                        us += 1
                        with open(f"result_mini.txt", 'a+') as mini_f:
                            mini_f.write(f"n={value}, ")
                            mini_f.write("Unsuccessful\n")
                            mini_f.write("\n".join(logs))
                            mini_f.write("\n\n\n")
                            mini_f.close()

                else:
                    f.write("Successful\n")
                    if s < 2:
                        s += 1
                        with open(f"result_mini.txt", 'a+') as mini_f:
                            mini_f.write(f"n={value}, ")
                            mini_f.write("Successful\n")
                            mini_f.write("\n".join(logs))
                            mini_f.write("\n")
                            mini_f.write(
                                f"Step {value+1}: Columns = {solution}\n")
                            mini_f.write("\n")
                            mini_f.close()
                f.write("\n".join(logs))
                f.write("\n")
                if solution != None:
                    count += 1
                    f.write(f"Step {value+1}: Columns = {solution}\n")
                f.write("\n")

        print(f"LasVegas algorithm With n = {value}")
        print(f"Number of successful placements is {count}")
        print("Number of trials is 10000")
        print(
            f"Probabilty that it will come to a solution is {count / 10000}\n")


# result_mini()
runner()
