from printer_manager import start_position, screen_z_value


class Gcode:
    gcode = []

    def __init__(self):
        self.screen_height = screen_z_value
        self.hop_up()
        self.goto(start_position)

    def hop_up(self):
        self.gcode.append(f"G1 Z{self.screen_height + 3} F10000")

    def hop_down(self):
        self.gcode.append(f"G1 Z{self.screen_height} F10000")

    def goto(self, position):
        self.gcode.append(f"G1 X{position[0]} Y{position[1]} F10000")

    def get_code(self):
        self.hop_up()
        self.goto(start_position)
        return "\n".join(self.gcode)
