import random
var = random.randint(0,6)

if var == 3:
  print("Fizz")
elif var == 5:
  print("Buzz")
elif var == 3 and 5:
  print("FizzBuzz")
else:
  print(var)
