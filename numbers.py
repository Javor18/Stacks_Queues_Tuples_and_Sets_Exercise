first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

n = int(input())

for i in range(n):

    command = input().split()

    command_type = command[0]

    command_param = command[1]

    if command_type == "Add":

        if command_param == "First":

            [first_sequence.add(int(x) for x in command[2:])]

        else:
            [second_sequence.add(int(x) for x in command[2:])]


    elif command_type == "Remove":

        if command_param == "First":

            first_sequence = first_sequence.difference(int(x) for x in command[2:])

        else:

            second_sequence = second_sequence.difference(int(x) for x in command[2:])

    else:

        print(first_sequence.issubset(second_sequence)) or second_sequence.issubset(first_sequence)


print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")