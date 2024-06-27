class Recipe:
    def __init__(self, time, inputs=None, outputs=None):
        if time <= 0:
            raise ValueError("Recipe time should be positive")
        self.time = time
        if inputs is None and outputs is None:
            raise Exception("Recipe must have at least an input or an output")
        self.inputs = inputs
        self.outputs = outputs
    
    def __repr__(self):
        return f"Recipe({self.time}, inputs: {self.inputs}, outputs: {self.outputs})"
        