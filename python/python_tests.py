import sys
sys.exit("Reference material. Do not execute")


### Assert ###

assert is_data_provided
assert age > 0, "Age must be positive"
assert 0 <= rating <= 100, "Rating must be between 0 and 100"

# Check dict contains expected keys
assert not {'key1', 'key2'} - d.keys() # Contains at least these keys
assert not {'key1', 'key2'} ^ d.keys() # Contains only these keys


### Exceptions ###

try:
  with open('not_a_file') as f:
    l = f.readlines()
except:
  print ("Cannot read file")
  l = []

# Exception types
# https://docs.python.org/3/library/exceptions.html#concrete-exceptions

# Handle specific exception
try:
  n = 100 / 0
except ZeroDivisionError as zde:
  print(zde)
  n = 0
except (RuntimeError, TypeError):
  pass

# Raise an exception
raise RuntimeError("I don't like you")

# Handle exception details
try:
  raise RuntimeError("Ea", "Eb")
except Exception as e:
  print(type(e)) # --> RuntimeError
  print(e.args)  # --> ("Ea", "Eb")
  print(e)       # Same as e.args, but can override with __str__
