class Machine:
    def __init__(self, name, crafting_speed, energy_consumption, burn_fuel=None):
        self.name = name
        self.crafting_speed = crafting_speed
        self.energy_consumption = energy_consumption # in kw
        self.__burn_fuel = burn_fuel
        if burn_fuel == None:
            self.__electric = True
        else:
            self.__electric = False
    
    # Fuel value of the item should be in MJ
    # Energy consumption is in kw
    def get_fuel_items_per_second(self):
        if not self.__electric:
            if self.__burn_fuel.burnable():
                return self.energy_consumption / (self.__burn_fuel.fuel_value * 1000)
        else:
            raise Exception("The machine is electric")
    
    def is_electric(self):
        return self.__electric
    
    def __repr__(self):
        return f"Machine({self.name}, {self.crafting_speed}, {self.energy_consumption}, {self.__burn_fuel}, {self.__electric})"
