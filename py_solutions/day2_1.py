x = 0
y = 0

with open('../inputs/day2.txt', 'r') as file:
    for line in file:
        commands = line.split(" ")
        if commands[0] == 'forward':
            x += int(commands[1])
        elif commands[0] == 'up':
            y -= int(commands[1])
        elif commands[0] == 'down':
            y += int(commands[1])
        else:
            print(f"what the heck is this {line}")

print(f"{x} {y}")
print(x*y)