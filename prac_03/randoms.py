import random

# Line 1: Generate a random integer between 5 and 20
print(random.randint(5, 20))

# Line 2: Generate a random odd integer between 3 and 9
print(random.randrange(3, 10, 2))

# Line 3: Generate a random float between 2.5 and 5.5
print(random.uniform(2.5, 5.5))

# Answering the questions in comments:
# 1. The smallest number on line 1 could be 5, the largest 20.
# 2. The smallest number on line 2 could be 3, the largest 9, and no, line 2 could not have produced a 4.
# 3. The smallest number on line 3 could be 2.5, the largest 5.5.

# Producing a random number between 1 and 100 inclusive:
print(random.randint(1, 100))
