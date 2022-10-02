from collections import deque

boxes_with_materials = [int(x) for x in input().split()]

magic_levels = deque([int(x) for x in input().split()])

present = {
    150 : 'Doll',
    250 : 'Wooden train',
    300 : 'Teddy bear',
    400 : 'Bicycle'
}

crafted_present = {}

while boxes_with_materials and magic_levels:

    box_with_materials = boxes_with_materials.pop()

    magic_level = magic_levels.popleft()

    points = box_with_materials * magic_level

    if points in present:

        toy = present[points]

        if toy in crafted_present:

            crafted_present[toy] += 1

        else:
            crafted_present[toy] = 1

    elif points < 0:

        result = box_with_materials + magic_level
        boxes_with_materials.append(result)

    elif points > 0:

        result = box_with_materials + 15
        boxes_with_materials.append(result)

    else:

        if box_with_materials == 0 and magic_level == 0:

            continue

        if box_with_materials == 0:

                magic_levels.appendleft(magic_level)

        else:

                boxes_with_materials.append(box_with_materials)


if ('Doll' in crafted_present and 'Wooden train' in crafted_present) or ('Teddy bear' in crafted_present and 'Bicycle' in crafted_present) :

    print("The presents are crafted! Merry Christmas!")

else:

    print("No presents this Christmas!")

if boxes_with_materials:

    print(f"Materials left: {', '.join([str(x) for x in boxes_with_materials[::-1]])}")

if magic_levels:

    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")


for present, count in sorted(crafted_present.items()):

    print(f"{present}: {count}")