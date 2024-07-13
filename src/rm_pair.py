class RM_Pair:
    def __init__(self, recipe, machine):
        self.recipe = recipe
        self.machine = machine.copy()
        self.inputs = {}
        self.outputs = {}
        self.scale = 1
        self.scaled_energy = self.machine.modded_energy * self.scale

        # Generate input / output per second for pair
        self.__generate_io_per_second()

    def __generate_io_per_second(self):
        # First get input/output per second from the recipe
        inputs = self.recipe.get_inputs_per_second()
        outputs = self.recipe.get_outputs_per_second()
        # Then modify the amount by the speed of the machine
        for input in inputs:
            inputs[input] = inputs[input] * self.machine.modded_speed * self.scale
        # For output also modify by productivity
        for output in outputs:
            outputs[output] = outputs[output] * self.machine.modded_speed * self.machine.modded_prod * self.scale
        # Check if machine needs burnable fuel
        if not self.machine.is_electric():
            # If yes, add to input (using machine method)
            burn_fuel = self.machine.get_burn_fuel()
            if burn_fuel in inputs:
                inputs[burn_fuel] += self.machine.get_fuel_items_per_second() * self.scale
            else:
                inputs[burn_fuel] = self.machine.get_fuel_items_per_second() * self.scale
        # Else the machine is electric
        # Finally set the inputs and outputs
        self.inputs = inputs
        self.outputs = outputs
    
    def add_module(self, module):
        self.machine.add_module(module)
        self.__generate_io_per_second()

    def remove_module(self, module_name):
        self.machine.remove_module(module_name)
        self.__generate_io_per_second()
    
    def set_scale(self, scale):
        self.scale = scale
        self.scaled_energy = self.machine.modded_energy * self.scale
        self.__generate_io_per_second()
        