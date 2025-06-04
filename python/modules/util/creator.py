# import a submodule from a sibling module with module name
from containers import shape as shp


def create_basic_square():
  return shp.Square(side = 1) # call to constructor


def validate_side_lengths(num_squares, side_lengths):
  assert len(side_lengths) == num_squares
  assert all([sl > 0 for sl in side_lengths])


def create_squares(num_squares, side_lengths = []):
  assert num_squares > 0
  if side_lengths:
    validate_side_lengths(num_squares, side_lengths)

  squares = []
  for i in range(num_squares):
    if side_lengths:
      new_square = shp.Square.from_side(side = side_lengths[i]) # call to generator
      squares.append(new_square)
    else:
      squares.append(create_basic_square())
  
  return squares
