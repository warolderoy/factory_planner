class Block:
    def __init__(self, name):
        self.name = name
        self.__rm_pairs = []
        self.__item_inputs = {}
        self.__item_outputs = {}

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


    def get_recipe_machine_pairs(self):
        return self.__rm_pairs
    
    def get_item_inputs(self):
        return self.__item_inputs
    
    def get_item_outputs(self):
        return self.__item_outputs
