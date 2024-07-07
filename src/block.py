class Block:
    def __init__(self, name):
        self.name = name
        self.__recipe_machine_pairs = []
        self.__item_inputs = {}
        self.__item_outputs = {}

    def add_recipe_machine_pair(self, recipe, machine):
        for pair in self.__recipe_machine_pairs:
            if pair[0] == recipe:
                raise Exception("This recipe is already used")
        
        self.__recipe_machine_pairs.append((recipe, machine))
        self.__calculate_inputs_outputs()
    
    def remove_recipe_machine_pair(self, recipe):
        if len(self.__recipe_machine_pairs) > 0:
            for i in range(len(self.__recipe_machine_pairs)):
                if self.__recipe_machine_pairs[i][0] == recipe:
                    self.__recipe_machine_pairs.pop(i)
                    self.__calculate_inputs_outputs
                
    def __calculate_inputs_outputs(self):
        # Reset dicts
        self.__item_inputs = {}
        self.__item_outputs = {}

        for rm_pair in self.__recipe_machine_pairs:
            inputs = rm_pair[0].get_inputs_per_second()
            outputs = rm_pair[0].get_outputs_per_second()

            if len(inputs) > 0:
                for input in inputs:
                    input_per_second = inputs[input] * rm_pair[1].modded_speed
                    if input in self.__item_inputs:
                        self.__item_inputs[input] += input_per_second
                    else:
                        self.__item_inputs[input] = input_per_second
            
            if len(outputs) > 0:
                for output in outputs:
                    output_per_second = outputs[output] * rm_pair[1].modded_speed
                    if output in self.__item_outputs:
                        self.__item_outputs[output] += output_per_second
                    else:
                        self.__item_outputs[output] = output_per_second
            
            # TODO
            # Add fuel if applicable
            if not rm_pair[1].is_electric():
                fuel = rm_pair[1].get_burn_fuel()
                

        # Check if an item is both in inputs and outputs
        if len(self.__item_inputs) > 0:
            for item in self.__item_inputs:
                if item in self.__item_outputs:
                    # TODO: Redo this section (forgot machines)
                    # Item needs to be balanced so that it is only an input, an output or neither
                    # Amount of the item needs to be reduced accordingly

                    # Get an amount of item/s for input and output

                    # Compare item/s and balance accordingly
                    if self.__item_inputs[item] > self.__item_outputs[item]:
                        self.__item_inputs[item] -= self.__item_outputs[item]
                        self.__item_outputs.pop(item)
                    
                    elif self.__item_inputs[item] < self.__item_outputs[item]:
                        self.__item_outputs[item] -= self.__item_inputs[item]
                        self.__item_inputs.pop(item)
                    
                    else:
                        self.__item_inputs.pop(item)
                        self.__item_outputs.pop(item)

    def get_recipe_machine_pairs(self):
        return self.__recipe_machine_pairs
    
    def get_item_inputs(self):
        return self.__item_inputs
    
    def get_item_outputs(self):
        return self.__item_outputs
