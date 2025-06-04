# import a submodule from the same module with .
from . import creator as cr

# import a submodule from a sibling module with module name
from containers import shape as shp

class SquarePrinter:

  @staticmethod
  def print_squares(squares = []):
    assert all([isinstance(s, shp.Square) for s in squares])

    print()
    print("ALL CREATED SQUARES:")
    for s in squares:
      print(s)


def show_n_squares(num_squares, side_lengths = []):
  assert num_squares > 0

  if side_lengths:
    cr.validate_side_lengths(num_squares, side_lengths)
    squares = cr.create_squares(num_squares, side_lengths)
  else:
    squares = cr.create_squares(num_squares)

  SquarePrinter.print_squares(squares)

