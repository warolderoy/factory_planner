import unittest

from item import Item
from recipe import Recipe
from machine import Machine

class Tests(unittest.TestCase):
    # Item tests
    def test_item_no_fuel(self):
        item = Item("Copper plate")
        self.assertEqual(item.__repr__(), "Item(Copper plate, None)")
        self.assertEqual(item.burnable(), False)
    
    def test_item_burnable(self):
        item = Item("Coal", 4)
        self.assertEqual(item.burnable(), True)

    def test_item_not_burnable(self):
        item = Item("coal", 0)
        self.assertEqual(item.burnable(), False)

    # Recipe tests
    def test_recipe(self):
        input = Item("Copper ore")
        output = Item("Copper plate")
        recipe = Recipe("Copper plate", 3.2, {input: 1}, {output: 1})
        self.assertEqual(
            recipe.__repr__(), 
            "Recipe(Copper plate, 3.2, inputs: {Item(Copper ore, None): 1}, outputs: {Item(Copper plate, None): 1})")
    
    def test_recipe_no_input(self):
        output = Item("Copper plate")
        recipe = Recipe("Copper plate", 3.2, outputs={output: 1})
        self.assertEqual(
            recipe.__repr__(), 
            "Recipe(Copper plate, 3.2, inputs: None, outputs: {Item(Copper plate, None): 1})")
    
    def test_recipe_no_output(self):
        input = Item("Copper ore")
        recipe = Recipe("Copper plate", 3.2, {input: 1})
        self.assertEqual(
            recipe.__repr__(), 
            "Recipe(Copper plate, 3.2, inputs: {Item(Copper ore, None): 1}, outputs: None)")
        
    # Machine tests
    def test_machine_electric(self):
        machine = Machine("Assembling machine 1", 0.5, 75)
        self.assertEqual(machine.is_electric(), True)
        self.assertEqual(
            machine.__repr__(),
            "Machine(Assembling machine 1, 0.5, 75, None, True)")
    
    def test_machine_burner(self):
        pass


if __name__ == "__main__":
    unittest.main()
