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
    grid = (101, 103)
    positions = set()
    neighbors_counter = []
    for i in range(10000):
        neighbors = 0
        robots = calculate_moves(robots, grid, i+1)
        for robot in robots:
            positions.add(robot.position)
        for x, y in positions:
            for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if (x2, y2) in positions:
                    neighbors += 1
        neighbors_counter.append(neighbors)
    print(neighbors_counter.index(max(neighbors_counter)) + 1)


if __name__ == '__main__':
    main()
