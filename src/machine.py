from module import Module

class Machine:
    def __init__(self, name, crafting_speed, energy_consumption, productivity = 1, burn_fuel=None, modules = []):
        self.name = name
        self.__crafting_speed = crafting_speed
        self.__energy_consumption = energy_consumption # in kw
        self.__productivity = productivity

        self.modded_speed = crafting_speed
        self.modded_energy = energy_consumption
        self.modded_prod = productivity

        self.__burn_fuel = burn_fuel
        if burn_fuel == None:
            self.__electric = True
        else:
            self.__electric = False
        
        self.__modules = modules
        self.__apply_modules()

    def __apply_modules(self):
        # Create compound module
        compound_mod = Module("")
        # Go through modules and add to compound
        for module in self.__modules:
            compound_mod = compound_mod + module
        # Check that values of compound module are above 20% of base value
        compound_mod.speed_modifier = max(compound_mod.speed_modifier, -0.8)
        compound_mod.energy_modifier = max(compound_mod.energy_modifier, -0.8)
        compound_mod.productivity_modifier = max(compound_mod.productivity_modifier, -0.8)
        # Apply to modded values
        self.modded_speed = self.__crafting_speed + (self.__crafting_speed * compound_mod.speed_modifier)
        self.modded_energy = self.__energy_consumption + (self.__energy_consumption * compound_mod.energy_modifier)
        self.modded_prod = self.__productivity + (self.__productivity * compound_mod.productivity_modifier)
    
    def add_module(self, module):
        self.__modules.append(module)
        # Reapply modules
        self.__apply_modules()

    def remove_module(self, module_name):
        # Remove one module with the name from the modules list
        for i in range(len(self.__modules)):
            if self.__modules[i].name == module_name:
                self.__modules.pop(i)
                self.__apply_modules()
                return
    
    def get_modules(self):
        return self.__modules
    
    # Fuel value of the item should be in MJ
    # Energy consumption is in kw
    def get_fuel_items_per_second(self):
        if not self.__electric:
            if self.__burn_fuel.burnable():
                return self.modded_energy / (self.__burn_fuel.fuel_value * 1000)
        else:
            raise Exception("The machine is electric")
    
    def get_burn_fuel(self):
        return self.__burn_fuel
    
    def is_electric(self):
        return self.__electric
    
    # doesn't include everything
    def __repr__(self):
        return f"Machine({self.name}, {self.__crafting_speed}, {self.__energy_consumption}, {self.__productivity}, {self.__burn_fuel}, {self.__electric}, modules: {self.__modules})"
