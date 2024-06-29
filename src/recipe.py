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
    
    def __repr__(self):
        return f"Recipe({self.name}, {self.time}, inputs: {self.inputs}, outputs: {self.outputs})"
        