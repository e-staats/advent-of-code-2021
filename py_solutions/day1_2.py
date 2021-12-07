with open("../inputs/day1.txt", "r") as file:
    lines = file.readlines()

count = 0
for i in range((len(lines) - 3)):
    window1 = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
    window2 = int(lines[i + 1]) + int(lines[i + 2]) + int(lines[i + 3])
    if window2 > window1:
        count += 1

print(window2)
print(count)
