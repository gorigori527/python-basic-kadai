class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def printinfo(self):
    print("name :", self.name)
    print("age :", self.age)

human = Human("James", "25")
human.printinfo()