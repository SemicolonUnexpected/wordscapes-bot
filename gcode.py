class Gcode:
    gcode = []

    def __init__(self, screen_height):
        self.screen_height = screen_height

    def hop_up(self):
        self.gcode.append(f"G1 Z{self.screen_height + 3} F10000")

    def hop_down(self):
        self.gcode.append(f"G1 Z{self.screen_height} F10000")

    def goto(self, x, y):
        self.gcode.append(f"G1 X{x} Y{y} F10000")

    def get_code(self):
        return "\n".join(self.gcode)
