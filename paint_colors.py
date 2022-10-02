from collections import deque

data = deque(input().split())
colors_found = []
all_colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']

while data:
    if len(data) > 1:
        first = data.popleft()
        second = data.pop()
        substring1 = first + second
        substring2 = second + first
        if substring1 in all_colors:
            colors_found.append(substring1)
        elif substring2 in all_colors:
            colors_found.append(substring2)
        else:
            first_el = first[:-1]
            second_el = second[:-1]
            if first_el:
                data.insert(len(data) // 2, first_el)
            if second_el:
                data.insert(len(data) // 2, second_el)

    elif len(data) <= 1:
        result = data.popleft()
        if result in all_colors:
            colors_found.append(result)

final_print = []
for color in colors_found:
    if color not in all_colors[3:]:
        final_print.append(color)
    else:
        if color == 'orange':
            if 'red' in colors_found and 'yellow' in colors_found:
                final_print.append(color)
        elif color == 'purple':
            if 'red' in colors_found and 'blue' in colors_found:
                final_print.append(color)
        elif color == 'green':
            if 'yellow' in colors_found and 'blue' in colors_found:
                final_print.append(color)

print(final_print)