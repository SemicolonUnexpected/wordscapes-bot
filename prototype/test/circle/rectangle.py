from dataclasses import dataclass


@dataclass
class Rectangle:
    """For usage with graphics. Has a width, height and location"""

    x: int
    y: int
    width: int
    height: int
