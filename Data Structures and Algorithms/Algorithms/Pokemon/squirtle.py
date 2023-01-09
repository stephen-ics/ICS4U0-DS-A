from Classes.Pokemon.pokemon import Pokemon
import json

class Squirtle(Pokemon):
  '''
  The Squirtle object that inherits the properties of its parent class Pokemon and contains its species and if its currently wearing sunglasses
  
  Attributes
  ----------
  species : str
    The species of the Squirtle
  wearingSunglasses : boolean
    Whether the Squirtle is currently wearing sunglasses

  Methods
  -------
  attack() -> float
    Returns the amount of damage dealt as a float
  aquaTail() -> list
    Returns a list that includes the amount of damage dealt as a float and the type of the attack as a str
  bubble() -> list
    Returns a list that includes the amount of damage dealt as a float and the type of the attack as a str
  waterGun() -> list
    Returns a list that includes the amount of damage dealt as a float and the type of the attack as a str
  writeSquirtleStatus() -> void
    Writes the status of the Squirtle on myPokemon.json
  '''
  def __init__(self, name, level, totalHp, attack, defense, speed, type, id, wearingSunglasses):
    '''
    Constructs a Squirtle object

    Parameters
    ----------
    wearingSunglasses : boolean
      If the Squirtle is wearing sunglasses
    '''
    super().__init__(name, level, totalHp, attack, defense, speed, type)
    self.id = id
    self.species = "Squirtle"
    self.wearingSunglasses = wearingSunglasses

  def __str__(self):
    '''
    Returns the string representation of the Squirtle object

    Returns
    -------
    Returns the string representation of the Squirtle object as a string
    '''
    return str("Level " + str(self.level) + " Squirtle. Name: " + self.name)

  def __repr__(self):
    '''
    Returns the object representation of the Squirtle object
  
    Returns
    -------
    Returns the object representation of the Squirtle object as a string
    '''
    return f'Stats("{self.species}", "{self.name}", "{self.level}", "{self.hp}", "{self.fainted}")'
  def getId(self):
    return self.id
  def getName(self):
    return self.name
  def getSunglasses(self):
    return self.wearingSunglasses
  def attack(self):
    '''
    Returns the damage dealt after including the attack of the Squirtle
    
    Returns
    -------
    The amount of damage dealt as a float
	  '''
    damage = self.attack * 10
    return damage
    
  def aquaTail(self):
    '''
    Returns the damage dealt using aquaTail after including the attack of the Squirtle, and the type of the attack
    
    Returns
    -------
    A list that includes the amount of damage dealt as a float and the type of the attack as a str
	  '''
    damage = self.attack * 20
    return [damage, "water"]

  def bubble(self):
    '''
    Returns the damage dealt using bubble after including the attack of the Squirtle, and the type of the attack
    
    Returns
    -------
    A list that includes the amount of damage dealt as a float and the type of the attack as a str
	  '''
    damage = self.attack * 10
    return [damage, "water"]

  def waterGun(self):
    '''
    Returns the damage dealt using waterGun after including the attack of the Squirtle, and the type of the attack
    
    Returns
    -------
    A list that includes the amount of damage dealt as a float and the type of the attack as a str
	  '''
    damage = self.attack * 30
    return [damage, "water"]

  def writeSquirtleStatus(self):
    '''
    Writes down the status of Squirtle in the myPokemon.json file
    
    Returns
    -------
    None
	  '''
    if self.wearingSunglasses:
      data = "Your level " + str(self.level) + " " + self.species + " is currently wearing sunglasses, this means he is happy"
    else:
      data = "Your level " + str(self.level) + " " + self.species + " is currently not wearing sunglasses, this means he is sad"
      
    json_object = json.dumps(data, indent=2)
    
    with open("Data/myPokemon.json", "a") as outfile:
      outfile.write(json_object + " ")
      
  

  
