def simulate(steps, cars, streets, bonus):
    result = 0

    # creat the queue for each street
    queues = {}
    for street in streets:
        queues[street] = []

    # place the cars on each street
    for car in range(len(cars)):
        queues[cars[car][0]].append([car, 0])

    # start the simulation.
    for i in range(steps):
        for street in queues:
            pop = 0
            for car in queues[street]:
                if car[1] == 0:
                    pop += 1
                    # find next street
                    for j in range(len(cars[car[0]])):
                        if cars[car[0]][j] == street:
                            if j + 1 < len(cars[car[0]]):
                                queues[cars[car[0]][j+1]].append([car[0], streets[cars[car[0]][j+1]][2]])
                            else:
                                result += bonus
                                result += steps - i
                else:
                    car[1] -= 1
    return result
