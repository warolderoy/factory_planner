class Module:
    def __init__(self, name, speed_modifier = 0, energy_modifier = 0, productivity_modifier = 0):
        self.name = name
        self.speed_modifier = speed_modifier
        self.energy_modifier = energy_modifier
        self.productivity_modifier = productivity_modifier

    def __add__(self, other):
        return Module(
            self.name,
            self.speed_modifier + other.speed_modifier,
            self.energy_modifier + other.energy_modifier,
            self.productivity_modifier + other.productivity_modifier
        )

    def __repr__(self):
        return f"Module({self.name}, {self.speed_modifier}, {self.energy_modifier}, {self.productivity_modifier})"