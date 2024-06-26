from graphics import Window
from item import Item

def main():
    #screen_x = 800
    #screen_y = 600

    #win = Window(screen_x, screen_y)

    #win.wait_for_close()
    test_item = Item("Copper plate")
    print(test_item)
    test_fuel = Item("Coal", 4)
    print(test_fuel)


main()