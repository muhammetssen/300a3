import random as rand


# [1,3,2,5,4]
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


values = [6,8,10]
for value in values:
    print(f"{'-'*15} {value} {'-'*15}")
    for k_value in range(value):
        print(f"k is {k_value}")
        count = 0
        for i in range(10000):
            current_state = QueensLasVegas(n=value, k=k_value)
            if (current_state == None): continue
            solution_array = solver(n=value,current_state=current_state)
            if len(solution_array)> 0:
                count +=1
        print(f"Number of successful placements is {count}")
        print("Number of trials is 10000")
        print(f"Probabilty that it will come to a solution is {count / 10000}")
    print()    
     
        
# print(f"{current_state=}")
