from collections import deque

working_bees = deque(int(x) for x in input().split())

nectars = [int(x) for x in input().split()]

elements = deque(input().split())

collected_honey = 0

while working_bees and nectars:

    bee_value = working_bees[0]
    nectar_value = nectars.pop()

    if bee_value > nectar_value:

        continue

    working_bees.popleft()
    operator = elements.popleft()

    if operator == "+":

        honey = abs(bee_value + nectar_value)

        collected_honey += honey

    elif operator == "-":

       honey = abs(bee_value - nectar_value)

       collected_honey += honey

    elif operator == "*":

        honey = abs(bee_value * nectar_value)

        collected_honey += honey

    elif operator == "/" and nectar_value > 0:

        honey = abs(bee_value / nectar_value)

        collected_honey += honey


print(f"Total honey made: {collected_honey}")

if working_bees:

    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")

if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")