from asciimatics.screen import ManagedScreen
from time import sleep
import re

AIR = 0
STONE = 1
SAND = 2

VISUALIZE = True

with ManagedScreen() as s:
    cam_dims = s.dimensions[1], s.dimensions[0]  # width, height
    cam_pos = 500 - cam_dims[0] // 2, 0

    def world_to_screen(pos):
        return pos[0] - cam_pos[0], pos[1] - cam_pos[1]

    def screen_to_world(pos):
        return pos[0] + cam_pos[0], pos[1] + cam_pos[1]

    world = {}

    def get_block(pos):
        return world.get(pos, AIR)

    lowest_y = 0

    # load world
    with open("14.txt", "r") as f:
        for line in f:
            last_node = None

            for i, m in enumerate(re.finditer(r"(\d+),(\d+)", line)):
                node = int(m.group(1)), int(m.group(2))

                if i > 0:
                    for x in range(min(last_node[0], node[0]), max(last_node[0], node[0]) + 1):
                        for y in range(min(last_node[1], node[1]), max(last_node[1], node[1]) + 1):
                            world[x, y] = STONE
                            lowest_y = max(lowest_y, y)
                    
                last_node = node

    # simulate

    current_sand = None
    last_dropped_sand = None
    total_sand = 0

    while last_dropped_sand != (500, 0):
        if not current_sand:
            current_sand = 500, 0
        
        # move sand
        if current_sand[1] == lowest_y + 1:  # lower infinite platform
            world[current_sand] = SAND
            total_sand += 1
            last_dropped_sand = current_sand
            current_sand = None
        elif get_block((current_sand[0], current_sand[1] + 1)) == AIR:
            current_sand = current_sand[0], current_sand[1] + 1
        elif get_block((current_sand[0] - 1, current_sand[1] + 1)) == AIR:
            current_sand = current_sand[0] - 1, current_sand[1] + 1
        elif get_block((current_sand[0] + 1, current_sand[1] + 1)) == AIR:
            current_sand = current_sand[0] + 1, current_sand[1] + 1
        else:
            world[current_sand] = SAND
            total_sand += 1
            last_dropped_sand = current_sand
            current_sand = None

        # move camera so that last_dropped sand is within view and leave a five block buffer
        if last_dropped_sand:
            if last_dropped_sand[0] < cam_pos[0] + 5:
                cam_pos = last_dropped_sand[0] - 5, cam_pos[1]
            if last_dropped_sand[0] > cam_pos[0] + cam_dims[0] - 5:
                cam_pos = last_dropped_sand[0] - cam_dims[0] + 5, cam_pos[1]
            if last_dropped_sand[1] < cam_pos[1] + 5:
                cam_pos = cam_pos[0], last_dropped_sand[1] - 5
            if last_dropped_sand[1] > cam_pos[1] + cam_dims[1] - 5:
                cam_pos = cam_pos[0], last_dropped_sand[1] - cam_dims[1] + 5

        # draw world only if some sand just fell down
        if not current_sand and VISUALIZE:
            s.clear_buffer(s.COLOUR_WHITE, s.A_NORMAL, s.COLOUR_BLACK)

            for x in range(0, cam_dims[0]):
                for y in range(0, cam_dims[1]):
                    block = get_block(screen_to_world((x, y)))

                    if block == STONE:
                        s.print_at("#", x, y, s.COLOUR_WHITE, s.A_NORMAL, s.COLOUR_BLACK)
                    elif block == SAND:
                        s.print_at("o", x, y, s.COLOUR_YELLOW, s.A_NORMAL, s.COLOUR_BLACK)

                s.print_at("#", x, lowest_y + 2 - cam_pos[1], s.COLOUR_WHITE, s.A_NORMAL, s.COLOUR_BLACK)
            
            if current_sand:
                s.print_at("o", *world_to_screen(current_sand), s.COLOUR_RED, s.A_NORMAL, s.COLOUR_BLACK)

            s.print_at(f"Sand: {total_sand}", 0, 0, s.COLOUR_WHITE, s.A_NORMAL, s.COLOUR_BLACK)

            s.refresh()

print(total_sand)