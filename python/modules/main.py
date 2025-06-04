# Each folder with __init__.py is a module, each file in it is a submodule
from containers import shape as shp

s = shp.Square(5)
print ("s is a {}".format(s))
