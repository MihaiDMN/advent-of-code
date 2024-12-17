class Robot:
    def __init__(self, position: tuple, velocity: tuple):
        self.position = position
        self.velocity = velocity

    def __repr__(self):
        return f'Robot({self.position})'


def calculate_moves(robots, grid, moves):
    for robot in robots:
        new_x = (robot.position[0] + robot.velocity[0] * moves) % grid[0]
        new_y = (robot.position[1] + robot.velocity[1] * moves) % grid[1]
        robot.position = (new_x, new_y)
    return robots


def calculate_robots_quadrants(robots, grid):
    quadrant_1 = 0
    quadrant_2 = 0
    quadrant_3 = 0
    quadrant_4 = 0
    center_x = grid[0] // 2
    center_y = grid[1] // 2
    for robot in robots:
        if robot.position[0] == center_x and robot.position[1] == center_y:
            continue
        elif robot.position[0] < center_x and robot.position[1] < center_y:
            quadrant_1 += 1
        elif robot.position[0] > center_x and robot.position[1] < center_y:
            quadrant_2 += 1
        elif robot.position[0] < center_x and robot.position[1] > center_y:
            quadrant_3 += 1
        elif robot.position[0] > center_x and robot.position[1] > center_y:
            quadrant_4 += 1
    return quadrant_1 * quadrant_2 * quadrant_3 * quadrant_4


def parse_input():
    line = input()
    robots = []
    while line != '':
        sections = line.strip().split(' ')
        i = 1
        for section in sections:
            x, y = section.split(',')
            x = x.split('=')[1]
            if i == 1:
                robot = Robot((int(x), int(y)), (0, 0))
            else:
                robot.velocity = (int(x), int(y))
            i += 1
        robots.append(robot)
        line = input()
    return robots


def main():
    robots = parse_input()
    grid = (11, 7)
    robots = calculate_moves(robots, grid, 100)
    print(calculate_robots_quadrants(robots, grid))


if __name__ == '__main__':
    main()
