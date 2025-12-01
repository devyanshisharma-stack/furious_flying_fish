"""
Name: Devyanshi Sharma
PennKey: devys
Recitation: 205
Program Execution: N/A, this class is meant to be used by other classes
Description:
A class that represents a Target to be hit in
Furious Flying Fish. Can update its own position based
on velocity and time.
"""

import penndraw


class Target:

    def __init__(self, scale, x_pos, y_pos, radius, x_vel, y_vel, hit_points):
        """
        Given the scale, a position, a radius, a velocity, and a number of
        hit points, construct a Target.
        """



    def draw(self):
        """
        Draw a circle centered at the Target's position
        with a radius equal to the Target's radius.
        Only draw a Target if it has more than zero
        hit points.
        """
        
    def update(self, time_step):
        """
        Given the change in time, update the Target's
        position based on its x and y velocity. When
        a Target is completely offscreen horizontally,
        its position should wrap back around to the opposite
        horizontal side. For example, if the Target moves off the
        right side of the screen, its x_pos should be set to the
        left side of the screen minus the Target's radius.
        The same logic should apply to the Target's vertical
        position with respect to the vertical screen boundaries.
        """
     

    def decrease_hp(self):
        """Decrement the Target's hit points by 1."""
        