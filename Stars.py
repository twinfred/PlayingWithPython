def draw_stars(my_list):
    for x in range(0, len(my_list)):
        if isinstance(my_list[x], int):
            print "*" * my_list[x]
        elif isinstance(my_list[x], str):
            print my_list[x][0] * len(my_list[x])

draw_stars(["tim", "magic", 1, 10, "applesauce"])