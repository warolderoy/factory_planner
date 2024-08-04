# Steps for project

## Get a basic window open
Get the window paramters and graphics from maze solver.
Done.

## Create Item class
Item mostly has attributes.
Done.

## Create recipe class
Takes items as ingredients and outputs
Done.

## Create machine class
A machine has a crafting speed (modifier) and energy consumption (electic/burnable)
Done.

## Create module class
A module can be added to a machine to modify it's crafting speed, energy consumption and production.
Done.

## Create rm_pair class
A class that pairs a recipe and a machine.
Should take care of recipe/machine interactions.

## Create block class
A block contains machine/recipe combinations. Allows to know how many machines there is in the block
for a given input / output.

Block starts with no machines or recipes.
Method to add recipe/machine pairs.
Method to remove(?) pairs.
1 main output, rest of outputs are byproducts.

Initial list of inputs and outputs created from recipes.
If no outputs then scale out of input (trash block).
If item both in input and output : intermediate item (goes from one recipe to another or is reused by recipe)
    Compare input and outpout of intermediate item
    Remove item from input, output or both based on result.
    If not removing both, lower input/outpout amount accordingly.

