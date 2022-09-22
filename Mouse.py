from win32gui import *
from win32api import *
from win32com import *
from win32con import *
import time
import bezier
import numpy as np


class Mouse:

    def __init__(self):
        self.pos_x = GetCursorPos()[0]
        self.pos_y = GetCursorPos()[1]

    def moveTo(self, x, y):
        SetCursorPos((x, y))

    def left(self):
        mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(.1)
        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)

    def right(self):
        mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(.1)
        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0)

    def bezier(self, destinationPoint):
        # For this example we'll use four control points, including start and end coordinates
        start = GetCursorPos()
        end = destinationPoint
        # Two intermediate control points that may be adjusted to modify the curve.
        control1 = start[0] + 125, start[1] + 100
        control2 = start[0] + 375, start[1] + 50

        # Format points to use with bezier
        control_points = np.array([start, control1, control2, end])
        points = np.array([control_points[:, 0], control_points[:, 1]])  # Split x and y coordinates

        # You can set the degree of the curve here, should be less than # of control points
        degree = 3
        # Create the bezier curve
        curve = bezier.Curve(points, degree)
        # You can also create it with using Curve.from_nodes(), which sets degree to len(control_points)-1
        # curve = bezier.Curve.from_nodes(points)

        curve_steps = 120  # How many points the curve should be split into. Each is a separate pyautogui.moveTo() execution
        delay = 1 / curve_steps  # Time between movements. 1/curve_steps = 1 second for entire curve

        # Move the mouse
        for i in range(1, curve_steps + 1):
            # The evaluate method takes a float from [0.0, 1.0] and returns the coordinates at that point in the curve
            # Another way of thinking about it is that i/steps gets the coordinates at (100*i/steps) percent into the curve
            x, y = curve.evaluate(i / curve_steps)
            SetCursorPos((int(x), int(y))) # Move to point in curve
            time.sleep(delay)  # Wait delay