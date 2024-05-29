# Create a tuple which stores following details
# [('Titanic', 1997),
# ('Matrix', 1999),
# (),
# ('Skyfall', 2012), ('Joker', 2019),
# ('MissionImpossible', 1996), ('ShawshankRedemption', 1994),
# ()]
# And remove empty tuples from a list of tuples.


tuple1 = [('Titanic', 1997),
('Matrix', 1999),
(),
('Skyfall', 2012), ('Joker', 2019),
('MissionImpossible', 1996), ('ShawshankRedemption', 1994),
()]
print("Before: ", tuple1)
tuple1.remove(())
print("Before: ", tuple1)

# Remove empty tuples
tuple1=list(filter(None, tuple1))
print("After: ", tuple1)

