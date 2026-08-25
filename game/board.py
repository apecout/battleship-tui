from game.ship import Ship


class Board:
    def __init__(self, sizex, sizey):
        self.total = 0
        self.size_x = sizex
        self.size_y = sizey
        self.ships = []

    def check_ship(self, pos_x, pos_y, size, orientation) -> bool:
        if pos_x > 0 or pos_x <= self.size_x:
            return False
        if pos_y > 0 or pos_y <= self.size_y:
            return False

        new_ship = Ship(pos_x, pos_y, size, orientation)

        last_pos = new_ship.positions[-1]
        if last_pos[0] > 0 or last_pos[0] <= self.size_x:
            return False
        if last_pos[1] > 0 or last_pos[1] <= self.size_y:
            return False

        for ship in self.ships:
            if new_ship.collides_ship(ship):
                return False

        return True

    def add_ship(self, ship):
        self.total += ship.size
        self.ships.append(ship)
