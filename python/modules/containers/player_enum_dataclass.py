from dataclasses import dataclass
from enum import Enum, unique

# @unique to enforce no repititions
class PlayerType(Enum):
  BATSMAN = 0
  BOWLER = 1
  WICKET_KEEPER = 2
  BATTER = 0 # repeat definition allowed

  def __str__(self):
    return self.name # enum to string
  
  @staticmethod
  def allrounder_types():
    return [PlayerType.BATSMAN, PlayerType.BOWLER]


def check_enums():
  print("All PlayerType values")
  print(list(PlayerType)) # excludes BATTER
  print()

  pt = PlayerType.BATSMAN
  print("BATSMAN is {} with value {}".format(pt, pt.value)) # --> BATSMAN

  pt1 = PlayerType.BATTER
  print("BATTER is {} with value {}".format(pt1, pt1.value))
  # --> BATSMAN (repeat definition will still have original name)

  aliases_equal = PlayerType.BATSMAN == PlayerType.BATTER \
                      and PlayerType.BATSMAN is PlayerType.BATTER
  print("BATSMAN is BATTER: {}".format(aliases_equal))

  print()
  pt2 = PlayerType['BATSMAN'] # string to enum
  print("str BATSMAN is {} with value {}".format(pt2, pt2.value))

  pt3 = PlayerType(0) # value to enum
  print("val 0 is {} with value {}".format(pt3, pt3.value))


@dataclass
class Player:
  name: str
  age: int
  player_type: list[PlayerType]
  sword_dancing: bool = False

  def is_allrounder(self):
    return all([pt in self.player_type for pt in PlayerType.allrounder_types()])
  
  def has_cool_celebration(self):
    return self.sword_dancing


def check_dataclass():
  p1 = Player(name = "Virat Kohli", age = 35, player_type = [PlayerType.BATSMAN])
  print(p1)
  print("\tAllrounder: {}".format(p1.is_allrounder()))

  p2 = Player(name = "MS Dhoni", age = 45,
              player_type = [PlayerType.BATSMAN, PlayerType.WICKET_KEEPER])
  print(p2)
  print("\tAllrounder: {}".format(p2.is_allrounder()))

  p3 = Player(name = "Ravindra Jadeja", age = 35, sword_dancing = True,
              player_type = [PlayerType.BATTER, PlayerType.BOWLER])
  print(p3)

  # is_allrounder() is True even though defined as BATTER and checked for BATSMAN
  print("\tAllrounder: {}".format(p3.is_allrounder()))
  print("\tCool celebration: {}".format(p3.has_cool_celebration()))


if __name__ == "__main__":
  print()
  print("CHECK ENUM")
  check_enums()

  print()
  print("CHECK DATACLASS")
  check_dataclass()
