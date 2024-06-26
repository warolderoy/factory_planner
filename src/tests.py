import unittest

from item import Item

class Tests(unittest.TestCase):
    # Item tests
    def test_item_no_fuel(self):
        item = Item("Copper plate")
        self.assertEqual(item.__repr__(), "Item(Copper plate, None)")
    
    def test_item_burnable(self):
        item = Item("Coal", 4)
        self.assertEqual(item.burnable(), True)

if __name__ == "__main__":
    unittest.main()
