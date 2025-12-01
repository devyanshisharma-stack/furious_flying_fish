"""
Name: Devyanshi Sharma
PennKey: devys
Recitation: 205
Program Execution: N/A, this class is meant to be used by other classes
Description:
A class representing the Arena in which the Furious Flying Fish
game takes place. Keeps track of the game's Fish and
Targets and receives the player's input to control the Fish.
"""

import penndraw
from fish import Fish
from target import Target


class Arena:
    def __init__(self, filename):
        """
        Given a file that describes the contents of the
        Arena, parse the file and initialize all member
        variables of the Arena.
        The file will be in the following format:
        num_targets scale
        nemo.num_throws
        target0.x_pos target0.y_pos target0.radius
        target0.x_vel target0.y_vel target0.hit_points
        target1.x_pos... etc.

        Remember to set mouse_listening_mode to true to start.
        """

        a_file = open(filename, 'r')
        first_line = a_file.readline().strip().split()
        num_targets = int(first_line[0])
        scale = float(first_line[1])
        num_throws = int(a_file.readline().strip())

        self.scale = scale
        penndraw.set_scale(0, scale)
        self.targets = []
        for i in range(num_targets):
            x_pos, y_pos, radius, x_vel, y_vel, hit_points = (
                a_file.readline().strip().split()
            )
            t = Target(scale, float(x_pos),
                    float(y_pos), float(radius), float(x_vel),
                    float(y_vel), int(hit_points))
            self.targets.append(t)
        self.nemo = Fish(1, 1, 0.25, num_throws)
        self.mouse_listening_mode = True
        self.mouse_was_pressed_last_update = False
        a_file.close()

    def draw(self):
        """
        1. Clear the screen
        2. Draw each Target
        3. Draw the Fish
        4. If in mouse listening mode and
        the mouse was pressed last update,
        draw the Fish's velocity as a line.
        5. Advance penndraw.
        """
        # clear screen
        penndraw.clear()

        # draw targets
        for t in self.targets:
            t.draw()

        # draw fish
        self.nemo.draw()

        # draw velocity
        if self.mouse_listening_mode and self.mouse_was_pressed_last_update:
            self.nemo.draw_velocity()
        penndraw.advance()

    def did_player_win(self):
        """
        Returns true when all Targets' hit points are 0.
        Returns false in any other scenario.
        """
        for t in self.targets:
            if t.hit_points > 0:
                return False
        return True

    def did_player_lose(self):
        """
        Returns true when the Fish's remaining throw count is 0
        when the game is in mouse-listening mode.
        Returns false in any other scenario.
        """
        return not self.did_player_win() and self.nemo.num_throws == 0

    def game_over(self):
        """
        Returns true when either the win or lose
        condition is fulfilled.
        Win: All Targets' hit points are 0.
        Lose: The Fish's remaining throw count reaches 0.
        Additionally, the game must be in mouse listening
        mode for the player to have lost so that the Fish
        can finish its final flight and potentially hit
        the last Target(s).
        """
        return self.did_player_win() or self.did_player_lose()

    def update(self, time_step):
        """
        Update each of the entities within the Arena.
        1. Call each Target's update function
        2. Check the game state (mouse listening or Fish moving)
        and invoke the appropriate functions for the Fish.
        """
        for t in self.targets:
            t.update(time_step)
        if (self.mouse_listening_mode):

            if penndraw.mouse_pressed():
                self.mouse_was_pressed_last_update = True
                self.nemo.set_velocity_from_mouse_pos()
        elif self.mouse_was_pressed_last_update:
            self.mouse_listening_mode = False
            self.nemo.decrement_throws()
            self.mouse_was_pressed_last_update = False
        else:
            self.nemo.update(time_step)

        for t in self.targets:
            self.nemo.test_and_handle_collision(t)
        self.targets = [t for t in self.targets if t.hit_points > 0]
        if self.fish_is_off_screen():
            for t in self.targets:
                if t.hit_this_shot:
                    t.decrease_hp()
                    t.hit_this_shot = False
                self.nemo.reset()
                self.mouse_listening_mode = True

    def fish_is_off_screen(self):
        """
        A helper function for the Arena class that lets
        it know when to reset the Fish's position and velocity
        along with the game state.
        Returns true when the Fish is offscreen to the left, right,
        or bottom. However, the Fish is allowed to go above the top
        of the screen without resetting.
        """
        x, y = self.nemo.x_pos, self.nemo.y_pos
        r = self.nemo.radius
        s = self.scale
        return (x + r < 0) or (x - r > s) or (y + r < 0)

    def draw_game_complete_screen(self):
        """
        Draws either the victory or loss screen.
        If all Targets have 0 hit points, the player has won.
        Otherwise they have lost.
        """
        penndraw.clear()
        penndraw.set_pen_color(penndraw.BLACK)
        if self.did_player_win():
            penndraw.text(self.scale / 2, self.scale / 2, "You win!")
        else:
            penndraw.text(self.scale / 2, self.scale / 2, "You have lost...")
        penndraw.advance()
