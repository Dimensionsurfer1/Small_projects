# Write code below 💖

# Write code below 💖
class Pokemon:
  def __init__(self,entry,name,types,description,is_caught,level,next_evolution):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught
    self.level = level
    self.next_evolution = next_evolution
  def speak(self):
    print(self.name,self.name)

  def display_details(self):
    if self.is_caught == True:
      print(f'''
      Entry Number: {self.entry}
      Name: {self.name}
      Type: {self.types}
      Level: {self.level}
      Next evolution: {self.next_evolution}
      Description: {self.description}''')
Pikachu = Pokemon(4,'Pikachu','Electric','''It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.
Pikachu has already been caught!''',True,50,'Raichu')
Pikachu.speak()
Pikachu.display_details()