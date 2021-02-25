data = input()
data = data.split()

lines_count = int(data[0])
lines = []

for i in range(lines_count):
    data = input()
    lines.append(data)

print(lines)
