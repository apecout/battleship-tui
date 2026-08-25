from enum import Enum


class Orientation(Enum):
    VERTICAL = 0
    HORIZONTAL = 1


class Ship:
    def __init__(self, origin_x, origin_y, size, orientation):
        self.size = size
        self.orientation = orientation
        self.positions = calc_positions(origin_x, origin_y, size, orientation)
        self.status = [True for _ in range(size)]
        self.is_alive = True

    def collides_pos(self, pos) -> bool:
        for self_pos in self.positions:
            if self_pos == pos:
                return True
        return False

    def collides_ship(self, ship) -> bool:
        for ship_pos in ship.positions:
            for self_pos in self.positions:
                if self_pos == ship_pos:
                    return True
        return False

    def shoot_at(self, pos) -> bool:
        for idx, self_pos in enumerate(self.positions):
            if self_pos == pos:
                self.status[idx] = False
                return True
        return False

    def update_alive(self) -> bool:
        for segment_status in self.status:
            if segment_status:
                return True

        self.is_alive = False
        return False


def calc_positions(origin_x, origin_y, size, orientation) -> list[tuple]:
    if orientation == Orientation.VERTICAL:
        return [(origin_x, origin_y + i) for i in range(size)]
    else:
        return [(origin_x + i, origin_y) for i in range(size)]
