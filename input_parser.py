import sys
import math


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


def readLines(file):
   with open(file, "r") as f:
       return f.read().split("\n")

def solve(file):
    input = readLines(file)


    seconds, inters, streetsCount, carsCount, score = input[0].split(" ")

    inters = int(inters)
    streetsCount = int(streetsCount)

    # streets = {}

    # for i in range(int(streetsCount)):
    #     start, end, name, time = input[i+1].split(" ")
    #     streets[name] = {
    #         "time": time,
    #         "start": start,
    #         "end": end,
    #     }


    matrix = [[None for _ in range(inters)] for _ in range(inters)] # row major
    streets = {}
    cars = []

    for i in range(streetsCount):
        start, end, name, time = input[i+1].split(" ")

        start = int(start)
        end = int(end)
        time = int(time)

        matrix[start][end] = [time, 0, name]
        streets[name] = (start, end, time)

    for i in range(int(carsCount)):
        pathInput = input[int(streetsCount)+1+i].split(" ")[1:]
        cars.append(pathInput)
        for p in pathInput[:-1]:
            start, end, time = streets[p]
            matrix[start][end][1] += 1


    signal = []
    for col in range(inters):
        totalPassedCars = 0
        colSignal = []
        for row in range(inters):
            if matrix[row][col] is None or matrix[row][col][1] == 0:
                continue

            colSignal.append(matrix[row][col])
            totalPassedCars += matrix[row][col][1]

        if len(colSignal) > 0:
            signal.append((col, colSignal))    


    print(len(signal))       

    for sig in signal:
        print(sig[0]) # Print index of intersection
        print(len(sig[1]))
        xam = max([a[1] for a in sig[1]])

        abc = sorted(sig[1], key=lambda student: student[0])
        for s in abc:
            print(f"{s[2]} { min(int(seconds), max(1, math.floor( 4 * (s[1] / xam))))   }") # Print name of the street and how many seconds



inputs = ["a", "b", "c", "d", "e", "f"]

for i in inputs:
    f = open(i+".out", "w")
    sys.stdout = f
    solve(i+".txt")



    f.close()

 