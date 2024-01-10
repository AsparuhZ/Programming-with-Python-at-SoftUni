floors = int(input())
rooms_per_floor = int(input())


for floor in reversed(range(1, floors + 1)):
    if floor == floors:
        room_type = "L"
    elif floor % 2 == 0:
        room_type = "O"
    else:
        room_type = "A"

    for room in range(rooms_per_floor):
        room_name = f"{room_type}{floor}{room}"
        print(room_name, end=" ")

    print()
