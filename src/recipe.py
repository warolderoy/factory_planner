class Recipe:
    def __init__(self, name, time, inputs=None, outputs=None):
        self.name = name
        if time <= 0:
            raise ValueError("Recipe time should be positive")
        self.time = time
        if inputs is None and outputs is None:
            raise Exception("Recipe must have at least an input or an output")
        self.inputs = inputs
        self.outputs = outputs
    
    def get_inputs_per_second(self):
        inputs_per_s = {}
        for input in self.inputs:
            inputs_per_s[input] = self.inputs[input] / self.time
        
        return inputs_per_s
    
    def get_outputs_per_second(self):
        outputs_per_s = {}
        for output in self.outputs:
            outputs_per_s[output] = self.outputs[output] / self.time
        
        return outputs_per_s
    
    def __repr__(self):
        return f"Recipe({self.name}, {self.time}, inputs: {self.inputs}, outputs: {self.outputs})"
        