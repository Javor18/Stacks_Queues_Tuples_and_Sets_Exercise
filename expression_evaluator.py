from collections import deque

string_expression = input().split()

numbers = deque()

for element in string_expression:

    if element in "*+-/":

        while len(numbers) > 1:

            first_num = numbers.popleft()
            second_num = numbers.popleft()

            result = 0

            if element == "*":

                result = first_num * second_num

            elif element == "+":

                result = first_num + second_num

            elif element == "-":

                result = first_num - second_num

            elif element == "/":

                result = first_num // second_num

            numbers.appendleft(result)

    else:

        numbers.append(int(element))

print(numbers.popleft())