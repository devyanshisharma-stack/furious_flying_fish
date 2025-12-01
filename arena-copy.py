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


    def did_player_win(self):
        """
        Returns true when all Targets' hit points are 0.
        Returns false in any other scenario.
        """
     

    def did_player_lose(self):
        """
        Returns true when the Fish's remaining throw count is 0
        when the game is in mouse-listening mode.
        Returns false in any other scenario.
        """

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

    def update(self, time_step):
        """
        Update each of the entities within the Arena.
        1. Call each Target's update function
        2. Check the game state (mouse listening or Fish moving)
        and invoke the appropriate functions for the Fish.
        """


    def fish_is_off_screen(self):
        """
        A helper function for the Arena class that lets
        it know when to reset the Fish's position and velocity
        along with the game state.
        Returns true when the Fish is offscreen to the left, right,
        or bottom. However, the Fish is allowed to go above the top
        of the screen without resetting.
        """
    

    def draw_game_complete_screen(self):
        """
        Draws either the victory or loss screen.
        If all Targets have 0 hit points, the player has won.
        Otherwise they have lost.
        """
