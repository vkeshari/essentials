# Each folder with __init__.py is a module, each file in it is a submodule
from containers import shape_inheritance as shp
from util import creator, printer

s = shp.Square(5)
print ("s is a {}".format(s))

ss = creator.create_squares(5, side_lengths = [1, 2, 3, 4, 5]) # call submodule method
printer.SquarePrinter.print_squares(ss) # call submodule class method

printer.show_n_squares(5, side_lengths = [1, 2, 2, 3, 3])
