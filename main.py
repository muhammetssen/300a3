import random as rand
from sys import argv


def part1():
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
            for i in range(10000):
                solution, logs = QueensLasVegas(value)
                with open(f"result_{value}.txt", 'a+') as f:
                    if solution == None:
                        f.write("Unsuccessful\n")

                    else:
                        f.write("Successful\n")
                    f.write("\n".join(logs))
                    f.write("\n")
                    if solution != None:
                        count += 1
                        f.write(f"Step {value+1}: Columns: {solution}\n")
                    f.write("\n")

            print(f"LasVegas algorithm With n = {value}")
            print(f"Number of successful placements is {count}")
            print("Number of trials is 10000")
            print(
                f"Probabilty that it will come to a solution is {count / 10000}\n")

    runner()

def part2():
    def is_valid(state):
        chosens = []
        n = len(state)
        for r, s in enumerate(state):
            unaval = set({})
            for i in range(len(chosens)):
                unaval.add(chosens[i])
                swift = r-i

                if chosens[i]-swift >= 0:
                    unaval.add(chosens[i]-swift)

                if chosens[i]+swift < n:
                    unaval.add(chosens[i]+swift)
            if s in unaval:
                return False
            chosens.append(s)
        return True


    def solver(n, current_state):
        if len(current_state) == n:
            if is_valid(current_state):
                return [current_state]
            return [None]
        r = len(current_state)
        avail_columns = [x for x in range(n)]
        unaval = set({})
        for i in range(len(current_state)):
            unaval.add(current_state[i])
            swift = r-i

            if current_state[i]-swift >= 0:
                unaval.add(current_state[i]-swift)

            if current_state[i]+swift < n:
                unaval.add(current_state[i]+swift)

        for c in unaval:
            avail_columns.remove(c)
        results = []
        for nominee in avail_columns:
            current_state.append(nominee)
            result_array = solver(n, current_state.copy())
            for r in result_array:
                if r != None:
                    results.append(r)
            current_state.remove(current_state[-1])
        return results


    def QueensLasVegas(n, k):
        r = 0
        column = []
        chosens = []
        avail_columns = [x for x in range(n)]
        while len(avail_columns) != 0 and r < k:
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
                return None

            chosen = rand.choice(avail_columns)
            chosens.append(chosen)
            column.append(chosen)
            r += 1

        return column


    values = [6, 8, 10]
    for value in values:
        print(f"{'-'*15} {value} {'-'*15}")
        for k_value in range(value):
            print(f"k is {k_value}")
            count = 0
            for i in range(10000):
                current_state = None 
                while current_state == None: # try until finding 
                    current_state = QueensLasVegas(n=value, k=k_value)

                solution_array = solver(n=value, current_state=current_state)
                if len(solution_array) > 0:
                    count += 1
            print(f"Number of successful placements is {count}")
            print("Number of trials is 10000")
            print(f"Probabilty that it will come to a solution is {count / 10000}")
        print()

def main():
    part = argv[1]
    if part == 'part1':
        part1()
    else:
        part2()


if __name__ == "__main__":
    main()
