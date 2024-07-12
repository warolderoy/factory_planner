import unittest

from item import Item
from recipe import Recipe
from machine import Machine
from module import Module
from rm_pair import RM_Pair

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
        
    def test_recipe_io_per_second(self):
        input = Item("Copper ore")
        output = Item("Copper plate")
        recipe = Recipe("Copper plate", 3.2, {input: 1}, {output: 1})
        self.assertEqual(
            recipe.get_inputs_per_second(),
            {input: 1/3.2}
        )
        self.assertEqual(
            recipe.get_outputs_per_second(),
            {output: 1/3.2}
        )
    
    # Module tests
    def test_module(self):
        module = Module("Speed module", 0.2, 0.5)
        self.assertEqual(
            module.__repr__(),
            "Module(Speed module, 0.2, 0.5, 0)"
        )
        module = module + module
        self.assertEqual(
            module.__repr__(),
            "Module(Speed module, 0.4, 1.0, 0)"
        )
        
    # Machine tests
    def test_machine_electric(self):
        machine = Machine("Assembling machine 1", 0.5, 75, modules=[])
        self.assertEqual(machine.is_electric(), True)
        self.assertEqual(
            machine.__repr__(),
            "Machine(Assembling machine 1, 0.5, 75, 1, None, True, modules: [])")
    
    def test_machine_burner(self):
        burn_fuel = Item("Coal", 4)
        machine = Machine("Stone furnace", 1, 90, burn_fuel=burn_fuel, modules=[])
        self.assertEqual(machine.get_fuel_items_per_second(), 0.0225)
        self.assertEqual(machine.is_electric(), False)
        self.assertEqual(
            machine.__repr__(),
            "Machine(Stone furnace, 1, 90, 1, Item(Coal, 4), False, modules: [])")
    
    def test_machine_get_burn_fuel(self):
        burn_fuel = Item("Coal", 4)
        machine = Machine("Stone furnace", 1, 90, burn_fuel=burn_fuel, modules=[])
        self.assertEqual(
            machine.get_burn_fuel(),
            burn_fuel
        )

        machine2 = Machine("Assembling machine 1", 0.5, 75, modules=[])
        self.assertEqual(
            machine2.get_burn_fuel(),
            None
        )

    # Modded machines
    def test_machine_one_module(self):
        module = Module("Speed module", 0.2, 0.5)
        machine = Machine("Assembling machine 1", 0.5, 75, modules=[module])
        self.assertEqual(machine.modded_speed, 0.6)
        self.assertEqual(machine.modded_energy, 112.5)
    
    def test_machine_min_mod(self):
        module = Module("Efficiency module", 0, -1)
        burn_fuel = Item("Coal", 4)
        machine = Machine("Assembling machine 1", 1, 100, burn_fuel=burn_fuel, modules=[module])
        self.assertEqual(machine.modded_energy, 20)
        self.assertEqual(machine.get_fuel_items_per_second(), 0.005)
    
    def test_machine_add_module(self):
        module = Module("Speed module", 0.2, 0.5)
        machine = Machine("Assembling machine 1", 0.5, 75)
        machine.add_module(module) # Why does this add to other machines?
        self.assertEqual(machine.modded_speed, 0.6)
        self.assertEqual(machine.modded_energy, 112.5)
        
        machine.remove_module("Speed module")
        self.assertEqual(machine.modded_speed, 0.5)
        self.assertEqual(machine.modded_energy, 75)
    
    def test_machine_get_modules(self):
        machine = Machine("Assembling machine 1", 0.5, 75)
        self.assertEqual(machine.get_modules(), [])
    
    # rm_pair tests
    def test_rm_pair_base(self):
        burn_fuel = Item("Coal", 4)
        machine = Machine("Stone furnace", 1, 90, burn_fuel=burn_fuel, modules=[])
        input = Item("Copper ore")
        output = Item("Copper plate")
        recipe = Recipe("Copper plate", 3.2, {input: 1}, {output: 1})
        pair = RM_Pair(recipe, machine)

        self.assertEqual(
            pair.inputs[input],
            1 / 3.2
        )
        self.assertEqual(
            pair.outputs[output],
            1 / 3.2
        )
        self.assertEqual(
            pair.inputs[burn_fuel],
            0.0225
        )
    
    def test_rm_pair_module(self):
        module = Module("Speed module", 1)
        burn_fuel = Item("Coal", 4)
        machine = Machine("Stone furnace", 1, 90, burn_fuel=burn_fuel, modules=[])
        input = Item("Copper ore")
        output = Item("Copper plate")
        recipe = Recipe("Copper plate", 3.2, {input: 1}, {output: 1})
        pair = RM_Pair(recipe, machine)

        pair.add_module(module)
        self.assertEqual(
            pair.inputs[input],
            2 / 3.2
        )
        self.assertEqual(
            pair.outputs[output],
            2 / 3.2
        )

        pair.remove_module("Speed module")
        self.assertEqual(
            pair.inputs[input],
            1 / 3.2
        )
        self.assertEqual(
            pair.outputs[output],
            1 / 3.2
        )

if __name__ == "__main__":
    unittest.main()
