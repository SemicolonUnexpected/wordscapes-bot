import printer_manager


class Gcode:
    gcode = []

    def __init__(self):
        self.screen_height = printer_manager.screen_z_value
        self.hop_up()
        self.gcode.append("G1 X0 Y0")

    def hop_up(self):
        self.gcode.append(f"G1 Z{self.screen_height + 3} F10000")

    def hop_down(self):
        self.gcode.append(f"G1 Z{self.screen_height} F10000")

    def goto(self, position):
        self.gcode.append(f"G1 X{printer_manager.start_position[0] + position[0]} Y{printer_manager.start_position[1] + position[0]} F10000")

    def get_code(self):
        self.hop_up()
        self.gcode.append("G1 X0 Y0")
        return "\n".join(self.gcode)
