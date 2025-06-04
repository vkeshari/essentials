
# Classes

class Rectangle:

  # By convention, class members have a preceding _
  #   This is only a convention. An object can change or override this, but not permanently.
  #     (see r1 and r2 below)
  _type = "RECTANGLE"

  def __init__(self, side1, side2):
    assert side1 > 0, side2 > 0
    self.side1 = side1
    self.side2 = side2
  
  def area(self):
    return self.side1 * self.side2
  
  def __str__(self):
    return "{}\n\tSide1:\t{}\tSide2:\t{}\tArea:\t{}" \
              .format(self._type, self.side1, self.side2, self.area())


def check_rectangle():
  r = Rectangle(1, 2)
  r.area() # --> 2
  print("r is a {}".format(r))
  # r.area() internally translates to Rectangle.area(r)

  r.__class__ # --> <class 'Rectangle'>
  isinstance(r, Rectangle) # --> True

  r1 = Rectangle(1, 2)
  r1._type = "MUTANT RECTANGLE" # Objects can modify a class member (but only for themselves, see r2)
  print("r1 is a {}".format(r1))

  r2 = Rectangle(1, 2)
  print("r2 is a {}".format(r2)) # still has _type "RECTANGLE"

  Rectangle._type = "SUPER MUTANT RECTANGLE" # Class members (including methods) are not private
  r3 = Rectangle(1, 2)
  print("r3 is a {}".format(r3))


# Inheritance
from math import sqrt

class Square(Rectangle):

  _type = "SQUARE"

  # Two ways to call superclass' __init__
  def __init__(self, side):
    super().__init__(side, side)

  def __init__(self, side):
    Rectangle.__init__(self, side, side)
  # Re-definition overwrites old definition.

  # Function overloading is not supported, constructor or otherwise
  # def __init__(self, side, area)

  # Use generators to implement multiple constructors
  @classmethod
  def from_side(cls, side):
    assert side > 0
    return Square(side)
    # return cls(side) -- can use cls instead of class name
  
  @staticmethod
  def from_area(area): # static methods do not need cls argument
    assert area > 0
    return Square(sqrt(area))
  
  def __str__(self):
    return "{}\n\tSide:\t{}\tArea:\t{}".format(self._type, self.side1, self.area())


def check_square():
  s = Square(3)
  s.area() # --> 9
  print("s is a {}".format(s))

  # t = Square(4, 5) -- Cannot call parent class' __init__ from child class

  isinstance(s, Rectangle) # --> True
  issubclass(Square, Rectangle) # --> True
  issubclass(s.__class__, Rectangle) # --> True (cannot check s directly)

  s1 = Square.from_side(5)
  s1.area() # --> 25
  print("s1 is a {}".format(s1))

  s2 = Square.from_area(16)
  s2.area() # --> 16.0
  print("s2 is a {}".format(s2))
  # s1.from_side(5) internally translates to Square.from_side(Square, 5)

  s3 = s.from_side(1) # can call a @classmethod with object name
  s3.area() # --> 1
  print("s3 is a {}".format(s3))

  s4 = s.from_area(1) # can call a @staticmethod with object name
  s4.area() # --> 1.0
  print("s4 is a {}".format(s4))


if __name__ == "__main__":
  print()
  print("RECTANGLE CHECKS")
  check_rectangle()

  print()
  print("SQUARE CHECKS")
  check_square()
