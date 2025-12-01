"""
Name: Devyanshi Sharma
PennKey: devys
Recitation: 205
Program Execution: N/A, this class is meant to be used by other classes
Description:
A class that represents the fish projectile in
Furious Flying Fish. Can update its own position based
on velocity and time, and can compute whether
it overlaps a given Target.
"""

import penndraw


class Fish:

    def __init__(self, x_pos, y_pos, radius, num_throws):
        """
        Initialize the fish's member variables
        with the same names as the inputs to those values.
        Initializes the fish's velocity components to 0.
        """
        self.x_pos: x_pos
        self.y_pos: y_pos
        self.radius: radius
        self.num_throws: num_throws
        self.y_vel = 0
        self.x_vel = 0


    def draw(self):
        """
        Draws a Circle centered at the fish's position
        with a radius equal to the fish's radius.
        Additionally, draws a triangular fin and a
        circular eye somewhere on the circle to make
        the fish look more like a fish. Additional details
        are up to your discretion.
        Also draws the fish's remaining throws 0.1 units
        above its circular body.
        """
        penndraw.filled_circle(self.x_pos, self.y_pos, self.radius)

    def draw_velocity(self):
        """
        Draw the line representing the fish's initial velocity
        when the player is clicking and dragging the mouse.
        """
        
    def reset(self):
        """
        Set x_pos and y_pos to 1.0,
        set x_vel and y_vel to 0.0.
        """
 

    def set_velocity_from_mouse_pos(self):
        """
        Compute the fish's initial velocity as the
        vector from the mouse's current position to
        the fish's current position. This will be used
        in mouse listening mode to update the launch
        velocity.
        """
    
    def update(self, time_step):
        """
        Given the change in time, compute the fish's
        new position and new velocity.
        """
  

    def distance(x1, y1, x2, y2):
        """
        A helper function used to find the distance
        between two 2D points. Remember to use the
        Pythagorean Theorem.
        """

    def test_and_handle_collision(self, target):
        """
        Given a target, determine if the fish should
        test for collision against it. If the fish
        *should* see if it collides with the target,
        then perform that test. If the fish collides,
        then decrease the target's HP by 1 set its
        hit_this_shot field to be true.
        """
        

    def decrement_throws(self):
        """
        reduce the num_throws for this fish by 1.
        """
