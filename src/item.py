class Item:
    # fuel value is in MJ
    def __init__(self, name, fuel_value=None):
        self.name = name
        self.fuel_value = fuel_value
    
    def burnable(self):
        if self.fuel_value:
            if self.fuel_value > 0:
                return True
            raise ValueError("fuel value must be positive")
        return False

    def __repr__(self):
        return f"Item({self.name}, {self.fuel_value})"