"""
    In this simple implementation rover has infinite land to go.
"""


class Rover:
    orientation = None

    def command(self, cmd: str):
        if cmd[0].upper() in 'MLR':
            for _cmd in cmd.upper():
                if _cmd == 'M':
                    self._go_forward()
                elif _cmd == 'R':
                    self._turn_right()
                elif _cmd == 'L':
                    self._turn_left()
                else:
                    raise NotImplementedError(f"Command {_cmd} not found")
            print(self.orientation)
        else:
            _x, _y, _o = cmd.split(' ')
            self._set_initial_pos(self._get_orientation_class(_o)(int(_x), int(_y)))

    def _get_orientation_class(self, orientation: str):
        if orientation == 'N':
            return Nord
        elif orientation == 'S':
            return Sud
        elif orientation == 'E':
            return Est
        elif orientation == 'W':
            return West
        else:
            raise NotImplementedError(f"Orientation {orientation} not found")

    def _set_initial_pos(self, orientation):
        self.orientation = orientation

    def _go_forward(self):
        self.orientation.go_forward()

    def _turn_right(self):
        self.orientation = self.orientation.turn_right()

    def _turn_left(self):
        self.orientation = self.orientation.turn_left()


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def go_forward(self):
        pass

    def __str__(self):
        return f"{self.x} {self.y}"


class OrientatedPosition(Position):
    orientation = ''

    def turn_right(self):
        pass

    def turn_left(self):
        pass

    def __str__(self):
        return f"{self.x} {self.y} {self.orientation}"


class Nord(OrientatedPosition):
    orientation = 'N'

    def go_forward(self):
        self.y += 1

    def turn_right(self):
        return Est(self.x, self.y)

    def turn_left(self):
        return West(self.x, self.y)


class Sud(OrientatedPosition):
    orientation = 'S'

    def go_forward(self):
        self.y -= 1

    def turn_right(self):
        return West(self.x, self.y)

    def turn_left(self):
        return Est(self.x, self.y)


class Est(OrientatedPosition):
    orientation = 'E'

    def go_forward(self):
        self.x += 1

    def turn_right(self):
        return Sud(self.x, self.y)

    def turn_left(self):
        return Nord(self.x, self.y)


class West(OrientatedPosition):
    orientation = 'W'

    def go_forward(self):
        self.x -= 1

    def turn_right(self):
        return Nord(self.x, self.y)

    def turn_left(self):
        return Sud(self.x, self.y)


if __name__ == "__main__":
    rover = Rover()
    print("Waiting for commands..")
    while True:
        cmd = input()
        if cmd == 'q':
            break
        else:
            rover.command(cmd)
    print("Bye")







