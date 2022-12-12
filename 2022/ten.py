cycle_counter = 0
x = 1
signal_strength = 0
line_idx = 0
screen = []
for i in range(0, 6):
    screen.append([])
    for j in range(0, 40):
        screen[i].append(".")


def print_screen():
    print("\033[2J")
    print("\033[H")
    for row in screen:
        print("".join(row))


def check_signal_strength():
    global signal_strength
    global cycle_counter
    global x
    if cycle_counter == 20:
        print(
            f"Current signal strength {x*cycle_counter} at cycle {cycle_counter} with x={x}")
        signal_strength += x * cycle_counter
    if cycle_counter > 20 and (cycle_counter - 19) % 40 == 0:
        print(
            f"Current signal strength {x*(cycle_counter + 1)} at cycle {cycle_counter+1} with x={x}")
        signal_strength += x * (cycle_counter + 1)


def increment_cycle_counter(type: str):
    global cycle_counter
    cycle_counter += 1
    print(f"Cycle {cycle_counter} {type}")
    if cycle_counter % 40 == 0:
        global line_idx
        line_idx += 1
    draw_pixel()
    check_signal_strength()


def draw_pixel():
    if x - 1 <= cycle_counter % 40 and cycle_counter % 40 <= x + 1:
        screen[line_idx][cycle_counter % 40] = "#"


file = open("../input.txt", "r")
for line in file:
    line = line.strip()
    if (line == "noop"):
        increment_cycle_counter("noop")
    elif line.startswith("addx "):
        _, amount = line.split(" ")
        increment_cycle_counter("addx start")
        print(f"{cycle_counter}: {x} += {amount} -> {x + int(amount)}")
        x += int(amount)
        increment_cycle_counter("addx end")

print_screen()
print(signal_strength)
