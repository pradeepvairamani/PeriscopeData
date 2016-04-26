class Grid(object):

    def __init__(self, x, y):
        """ Create a x * y grid """
        self.grid = {}
        self.rows = x
        self.cols = y
        self.visited = set()
        self.dirt_collected = 0
        self.hoover = None

        for item_x in range(self.rows):
            for item_y in range(self.cols):
                self.grid[(item_x, item_y)] = 1

    def _check_placement_validity(self, x, y):
        if(x >= 0 and y >= 0 and x < self.rows and y < self.cols):
            return True
        # print("No change in position")
        return False

    def place_dirt(self, x, y):
        if self._check_placement_validity(x, y):
            self.grid[(x, y)] = 0

    def set_hoover_pos(self, x, y):
        """Move hoover and collect dirt for the first time"""
        if self._check_placement_validity(x, y):
            self.hoover = [x, y]
            hoover_tuple = tuple(self.hoover)
            if hoover_tuple not in self.visited:
                if self.grid[hoover_tuple] == 0:
                    self.dirt_collected += 1
                self.visited.add(hoover_tuple)
            self.grid[hoover_tuple] = 'x'
            # print('new hoover pos ' + str(x) + " " + str(y))

    def get_hoover_pos(self):
        if not self.hoover:
            return None
        return str(self.hoover[0]) + " " + str(self.hoover[1])

    def get_dirt_collected(self):
        return self.dirt_collected

    def move_north(self):
        x, y = self.hoover
        y += 1
        self.set_hoover_pos(x, y)

    def move_south(self):
        x, y = self.hoover
        y -= 1
        self.set_hoover_pos(x, y)

    def move_east(self):
        x, y = self.hoover
        x += 1
        self.set_hoover_pos(x, y)

    def move_west(self):
        x, y = self.hoover
        x -= 1
        self.set_hoover_pos(x, y)

    def __str__(self):
        final_ans = []
        for item_x in range(self.rows):
            ans = []
            for item_y in range(self.cols):
                ans = [self.grid[(item_x, item_y)]] + ans
            final_ans.append(ans)
        final_ans = zip(*final_ans)
        s = '\n'.join([' '.join([str(item) for item in row])
                       for row in final_ans])
        return s


if __name__ == "__main__":
    grid = None
    count = 0
    directions = []
    initital_pos = None
    with open("input.txt", "r", encoding="utf-8") as grid_file:
        for grid_file_line in grid_file:
            count += 1
            """Create the grid"""
            if count == 1:
                x, y = map(int, grid_file_line.split())
                grid = Grid(x, y)
                continue

            """Initialize the hoover pos"""
            if count == 2:
                x, y = map(int, grid_file_line.split())
                initital_pos = (x, y)
                continue

            line = (grid_file_line.split())
            if len(line) == 2:
                grid.place_dirt(int(line[0]), int(line[1]))
            elif len(line) == 1:
                directions = list(line[0])

    grid.set_hoover_pos(initital_pos[0], initital_pos[1])
    for d in directions:
        if d == 'N':
            grid.move_north()
        elif d == 'S':
            grid.move_south()
        elif d == 'E':
            grid.move_east()
        elif d == 'W':
            grid.move_west()

    print(grid.get_hoover_pos())
    print(grid.dirt_collected)
