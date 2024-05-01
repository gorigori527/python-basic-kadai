class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def check_adult(self):
    if self.age>=20:
      print(self.name, "is 大人")
    else:
      print(self.name, "is not 大人")

p1 = Human("James", 30)
p2 = Human("Rob", 17)
p3 = Human("Sam", 20)
p4 = Human("Nick", 45)
people = [p1, p2, p3, p4]

for i in people:
  i.check_adult()

