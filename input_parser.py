import sys


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

    for i in range(streetsCount):
        start, end, name, time = input[i+1].split(" ")

        start = int(start)
        end = int(end)
        time = int(time)

        matrix[start][end] = [time, 0, name]
        streets[name] = (start, end, time)

    for i in range(int(carsCount)):
        pathInput = input[int(streetsCount)+1+i].split(" ")[1:]
        
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
            signal.append((colSignal, col))    


    print(len(signal))       

    for sig in signal:
        print(sig[1])
        print(len(sig[0]))
        for s in sig[0]:
            print(f"{s[2]} 1") # Print name of the street and how many seconds

inputs = ["a", "b", "c", "d", "e", "f"]

for i in inputs:
    f = open(i+".out", "w")
    sys.stdout = f
    solve(i+".txt")
    f.close()

