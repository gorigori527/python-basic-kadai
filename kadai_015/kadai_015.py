class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_name(self):
    print(self.name)
  def show_age(self):
    print(self.age)

human = Human("James", 25)
human.show_name()
human.show_age()
