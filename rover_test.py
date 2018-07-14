import pytest
from rover import Rover, Position, Nord, Sud, Est, West


class Test_Rover:
    """
        Rummer Test Class
        has been wrote using TDD method,
        the tests are listed according to the time they was wrote,
        the older tests are, indeed, marked as obsolete.

        run tests with 'pytest' command.
    """
    @pytest.fixture
    def rover(self):
        return Rover()

    # obsolete
    @pytest.mark.parametrize("orientation, x, y, test",
                             [
                                 (Position, 1, 1, "1 1"),
                                 (Nord, 1, 1, "1 1 N"),
                                 (Sud,  1, 1, "1 1 S"),
                                 (Est,  1, 1, "1 1 E"),
                                 (West, 1, 1, "1 1 W"),
                             ])
    def test_initial_pos(self, rover, orientation, x, y, test):
        rover._set_initial_pos(orientation(x, y))
        assert str(rover.orientation) == test

    # obsolete
    @pytest.mark.parametrize("orientation, x, y, test",
                             [
                                 (Nord, 1, 1, "1 2 N"),
                                 (Sud,  1, 1, "1 0 S"),
                                 (Est,  1, 1, "2 1 E"),
                                 (West, 1, 1, "0 1 W"),
                             ])
    def test_go_forward(self, rover, orientation, x, y, test):
        rover._set_initial_pos(orientation(x, y))
        rover._go_forward()
        assert str(rover.orientation) == test

    # obsolete
    @pytest.mark.parametrize("orientation, x, y, test",
                             [
                                 (Nord, 1, 1, "1 1 E"),
                                 (Sud,  1, 1, "1 1 W"),
                                 (Est,  1, 1, "1 1 S"),
                                 (West, 1, 1, "1 1 N"),
                             ])
    def test_turn_right(self, rover, orientation, x, y, test):
        rover._set_initial_pos(orientation(x, y))
        rover._turn_right()
        assert str(rover.orientation) == test

    # obsolete
    @pytest.mark.parametrize("orientation, x, y, test",
                             [
                                 (Nord, 1, 1, "1 1 W"),
                                 (Sud,  1, 1, "1 1 E"),
                                 (Est,  1, 1, "1 1 N"),
                                 (West, 1, 1, "1 1 S"),
                             ])
    def test_turn_left(self, rover, orientation, x, y, test):
        rover._set_initial_pos(orientation(x, y))
        rover._turn_left()
        assert str(rover.orientation) == test

    @pytest.mark.parametrize("command, test",
                             [
                                 ("1 1 N", "1 1 N"),
                                 ("1 1 S", "1 1 S"),
                                 ("1 1 E", "1 1 E"),
                                 ("1 1 W", "1 1 W"),
                             ])
    def test_initial_position(self, rover, command, test):
        rover.command(command)
        assert str(rover.orientation) == test

    @pytest.mark.parametrize("initial_command, test",
                             [
                                 ("1 1 N", "1 2 N"),
                                 ("1 1 S", "1 0 S"),
                                 ("1 1 E", "2 1 E"),
                                 ("1 1 W", "0 1 W"),
                             ])
    def test_move(self, rover, initial_command, test):
        rover.command(initial_command)
        rover.command('M')
        assert str(rover.orientation) == test

    @pytest.mark.parametrize("initial_command, test",
                             [
                                 ("1 1 N", "1 1 E"),
                                 ("1 1 S", "1 1 W"),
                                 ("1 1 E", "1 1 S"),
                                 ("1 1 W", "1 1 N"),
                             ])
    def test_rotate_right(self, rover, initial_command, test):
        rover.command(initial_command)
        rover.command('R')
        assert str(rover.orientation) == test

    @pytest.mark.parametrize("initial_command, test",
                             [
                                 ("1 1 N", "1 1 W"),
                                 ("1 1 S", "1 1 E"),
                                 ("1 1 E", "1 1 N"),
                                 ("1 1 W", "1 1 S"),
                             ])
    def test_left_right(self, rover, initial_command, test):
        rover.command(initial_command)
        rover.command('L')
        assert str(rover.orientation) == test

    def test_command_sequence(self, rover):
        rover.command('1 2 N')
        rover.command('LMLMLMLMM')
        assert str(rover.orientation) == '1 3 N'
        rover.command('3 3 E')
        rover.command('MMRMMRMRRM')
        assert str(rover.orientation) == '5 1 E'

