class Machine:
    def __init__(self, crafting_speed, energy_consumption, burn_fuel=None):
        self.crafting_speed = crafting_speed
        self.energy_consumption = energy_consumption # in kw
        self.burn_fuel = burn_fuel
        if burn_fuel == None:
            self.electric = True
        else:
            self.electric = False
    
    # Fuel value of the item should be in MJ
    # Energy consumption is in kw
    def get_fuel_items_per_second(self):
        if not self.electric:
            if self.burn_fuel.burnable():
                return (self.burn_fuel.fuel_value * 1000) / self.energy_consumption
        else:
            raise Exception("The machine is electric")
