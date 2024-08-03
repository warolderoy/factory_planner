class Block:
    def __init__(self, name, main_output, output_amount=0):
        self.name = name
        self.__rm_pairs = []
        self.__item_inputs = {}
        self.__item_outputs = {}
        self.main_output = main_output
        self.output_amount = output_amount

    def add_rm_pair(self, recipe, machine):
        # raise Exception("This recipe is already used")
        # call __calculate_inputs_outputs
        pass
    
    def remove_rm_pair(self, recipe):
        # call __calculate_inputs_outputs
        pass
                
    def __calculate_inputs_outputs(self):
        # Reset dicts
        self.__item_inputs = {}
        self.__item_outputs = {}    
        # Check if an item is both in inputs and outputs
        # TODO: Equilibrate scales of rm_pairs to not have items both in input and output
        # Search through rm_pairs to see which one is the "main rm_pair" (or have it be set at the start)
        # Once you have the main pair, scale it so that the main output is the same as output_amount
        # Now search through the other rm_pairs to see if one of their outputs is in the inputs of the main pair


    def get_recipe_machine_pairs(self):
        return self.__rm_pairs
    
    def get_item_inputs(self):
        return self.__item_inputs
    
    def get_item_outputs(self):
        return self.__item_outputs
