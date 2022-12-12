import re
import sys

sys.set_int_max_str_digits(1000000)
monkeys = []

manage_worry = False
# iterations = 20
iterations = 10000

tests_modulo = 1


def parse_operation(operation):
    first, operand, second = operation.split(" ")
    if first == "old" and second == "old":
        if operand == "+":
            return lambda x: x + x
        elif operand == "-":
            return lambda x: 0
        elif operand == "*":
            return lambda x: x * x
        elif operand == "/":
            return lambda x: 1
    elif first == "old":
        if operand == "+":
            return lambda x: x + int(second)
        elif operand == "-":
            return lambda x: x - int(second)
        elif operand == "*":
            return lambda x: x * int(second)
        elif operand == "/":
            return lambda x: x / int(second)
    elif second == "old":
        if operand == "+":
            return lambda x: int(first) + x
        elif operand == "-":
            return lambda x: int(first) - x
        elif operand == "*":
            return lambda x: int(first) * x
        elif operand == "/":
            return lambda x: int(first) / x


def parse_input(lines):
    monkey = re.findall(r"(\d+)", lines[0])[0]
    _, items = lines[1].split(": ")
    starting_items = list(map(lambda x: int(x), items.split(", ")))
    operation = parse_operation(lines[2].split("Operation: new = ")[1])
    test = int(re.findall(r"(\d+)", lines[3])[0])
    if_true = int(re.findall(r"(\d+)", lines[4])[0])
    if_false = int(re.findall(r"(\d+)", lines[5])[0])
    return {"monkey": monkey, "starting_items": starting_items, "operations": operation, "test": test, "if_true": if_true, "if_false": if_false, "inspected": 0}


def monkey_turn(monkey):
    while len(monkey["starting_items"]) > 0:
        item = monkey["starting_items"].pop(0)
        item = monkey["operations"](item)
        if manage_worry:
            item = item // 3
        else:
            if item > tests_modulo:
                item = item % tests_modulo
        monkey["inspected"] += 1
        if item % monkey["test"] == 0:
            monkeys[monkey["if_true"]]["starting_items"].append(item)
        else:
            monkeys[monkey["if_false"]]["starting_items"].append(item)


def print_monkey(monkey):
    print(
        f"Monkey {monkey['monkey']} has {monkey['starting_items']} and inspected {monkey['inspected']} items.")


def print_monkeys():
    for monkey in monkeys:
        print_monkey(monkey)


if __name__ == "__main__":
    file = open("../input.txt", "r")
    tests_modulo = 1
    lines = file.readlines()
    lines = list(map(lambda x: x.strip(), lines))
    for i in range(0, len(lines), 7):
        result = parse_input(
            lines[i:i+7])
        monkeys.append(result)
        tests_modulo = tests_modulo * result["test"]
    print(tests_modulo)
    for i in range(0, iterations):
        print(i)
        for i in monkeys:
            monkey_turn(i)
    inspections = list(map(lambda x: x["inspected"], monkeys))
    inspections.sort(reverse=True)
    print(inspections)
    print(inspections[0] * inspections[1])
