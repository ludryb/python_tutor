def capitalize(world):
    world = [i for i in world]
    world[0] = chr(ord(world[0]) - 32)
    for i in range(len(world)):
        if world[i] == " ":
            world[i + 1] = chr(ord(world[i + 1]) - 32)

    return world

    # world = [i for i in world.split()]
    # for i in range(len(world)):
    #     letter = [i for i in world[i]]
    #     letter[0] = chr(ord(letter[0]) - 32)
    #     world[i] = "".join(letter)
    # world = " ".join(world)
    # return world


print(capitalize(input()))
