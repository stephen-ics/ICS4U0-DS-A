from Classes.Pokemon.pokemon import Pokemon
import json

class Charmander(Pokemon):
  '''
  The Charmander object that inherits the properties of its parent class Pokemon and contains its species and if its seeds are blooming
  
  Attributes
  ----------
  species : str
    The species of the Charmander
  tailBurning : boolean
    Whether the fire on Charmanders tail is currently burning

  Methods
  -------
  attack() -> float
    Returns the amount of damage dealt as a float
  ember() -> list
    Returns a list that includes the amount of damage dealt as a float and the type of the attack as a str
  fireFang() -> list
    Returns a list that includes the amount of damage dealt as a float and the type of the attack as a str
  flamethrower() -> list
    Returns a list that includes the amount of damage dealt as a float and the type of the attack as a str
  writeCharmanderStatus() -> void
    Writes the status of the Charmander on myPokemon.json
  '''
  
  def __init__(self, name, level, totalHp, attack, defense, speed, type, tailBurning):
    '''
    Constructs a Charmander object

    Parameters
    ----------
    tailBurning : boolean
      Whether the fire on the Charmanders tail is currently burning
    '''
    super().__init__(name, level, totalHp, attack, defense, speed, type)
    self.species = "Charmander"
    self.tailBurning = tailBurning

  def __str__(self):
    '''
    Returns the string representation of the Charmander object

    Returns
    -------
    Returns the string representation of the Charmander object as a string
    '''
    return "Level " + str(self.level) + " " + self.species + ". Name: " + self.name

  def __repr__(self):
    '''
    Returns the object representation of the Charmander object
  
    Returns
    -------
    Returns the object representation of the Charmander object as a string
    '''
    return f'Stats("{self.species}", "{self.name}", "{self.level}", "{self.hp}", "{self.fainted}")'
    
  def attack(self):
    '''
    Returns the damage dealt after including the attack of the Charmander
    
    Returns
    -------
    The amount of damage dealt as a float
	  '''
    damage = self.attack * 10
    return damage
    
  def ember(self):
    '''
    Returns the damage dealt using ember after including the attack of the Charmander, and the type of the attack
    
    Returns
    -------
    A list that includes the amount of damage dealt as a float and the type of the attack as a str
	  '''
    damage = self.attack * 15
    return [damage, "fire"]

  def fireFang(self):
    '''
    Returns the damage dealt using fireFang after including the attack of the Charmander, and the type of the attack
    
    Returns
    -------
    A list that includes the amount of damage dealt as a float and the type of the attack as a str
	  '''
    damage = self.attack * 65
    return [damage, "fire"]

  def flamethrower(self):
    '''
    Returns the damage dealt using flamethrower after including the attack of the Charmander, and the type of the attack
    
    Returns
    -------
    A list that includes the amount of damage dealt as a float and the type of the attack as a str
	  '''
    damage = self.attack * 40
    return [damage, "fire"]
  
  def writeCharmanderStatus(self):
    '''
    Writes down the status of Charmander in the myPokemon.json file
    
    Returns
    -------
    None
	  '''
    if self.tailBurning:
      data = "Your level " + str(self.level) + " " + self.species + "'s tail is currently burning', this means he is happy"
    else:
      data = "Your level " + str(self.level) + " " + self.species + "'s tail is currently not burning, this means he is sad"
      
    json_object = json.dumps(data, indent=2)
    
    with open("Data/myPokemon.json", "a") as outfile:
      outfile.write(json_object + " ")
  