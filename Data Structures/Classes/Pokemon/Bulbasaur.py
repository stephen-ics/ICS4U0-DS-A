from Classes.Pokemon.pokemon import Pokemon
import json

class Bulbasaur(Pokemon):
  '''
  The Bulbasaur object that inherits the properties of its parent class Pokemon and contains its species and if its seeds are blooming
  
  Attributes
  ----------
  species : str
    The species of the Bulbasaur
  seedsBlooming : boolean
    Whether the seeds on the Bulbasaur are currently blooming

  Methods
  -------
  attack() -> float
    Returns the amount of damage dealt as a float
  vineWhip() -> list
    Returns a list that includes the amount of damage dealt as a float and the type of the attack as a str
  powerWhip() -> list
    Returns a list that includes the amount of damage dealt as a float and the type of the attack as a str
  sludgeBomb() -> list
    Returns a list that includes the amount of damage dealt as a float and the type of the attack as a str
  writeBulbasaurStatus() -> void
    Writes the status of the Bulbasaur on myPokemon.json
  '''
  
  def __init__(self, name, level, totalHp, attack, defense, speed, type, seedsBlooming):
    '''
    Constructs a Bulbasaur object

    Parameters
    ----------
    seedsBlooming : boolean
      Whether the seeds on the Bulbasaur are currently blooming
    '''
    super().__init__(name, level, totalHp, attack, defense, speed, type)
    self.species = "Bulbasaur"
    self.seedsBlooming = seedsBlooming

  def __str__(self):
    '''
    Returns the string representation of the Bulbasaur object

    Returns
    -------
    Returns the string representation of the Bulbasaur object as a string
    '''
    return "Level " + str(self.level) + " " + self.species + ". Name: " + self.name

  def __repr__(self):
    '''
    Returns the object representation of the Bulbasaur object
  
    Returns
    -------
    Returns the object representation of the Bulbasaur object as a string
    '''
    return f'Stats("{self.species}", "{self.name}", "{self.level}", "{self.hp}", "{self.fainted}")'

  def attack(self):
    '''
    Returns the damage dealt after including the attack of the Bulbasaur
    
    Returns
    -------
    The amount of damage dealt as a float
	  '''
    damage = self.attack * 10
    return damage

  def vineWhip(self):
    '''
    Returns the damage dealt using vineWhip after including the attack of the Bulbasaur and the type of the attack
    
    Returns
    -------
    A list that includes the amount of damage dealt as a float and the type of the attack as a str
	  '''
    damage = self.attack * 20
    return [damage, "grass"]

  def powerWhip(self):
    '''
    Returns the damage dealt using powerWhip after including the attack of the Bulbasaur and the type of the attack
    
    Returns
    -------
    A list that includes the amount of damage dealt as a float and the type of the attack as a str
	  '''
    damage = self.attack * 10
    return [damage, "grass"]

  def sludgeBomb(self):
    '''
    Returns the damage dealt using sludgeBomb after including the attack of the Bulbasaur and the type of the attack
    
    Returns
    -------
    A list that includes the amount of damage dealt as a float and the type of the attack as a str
	  '''
    damage = self.attack * 30
    return [damage, "poison"]
  
  def writeBulbasaurStatus(self):
    '''
    Writes down the status of Bulbasaur in the myPokemon.json file
    
    Returns
    -------
    None
	  '''
    if self.seedsBlooming:
      data = "Your level " + str(self.level) + " " + self.species + "'s seeds are currently blooming, this means he is happy"
    else:
      data = "Your level " + str(self.level) + " " + self.species + "'s seeds are currently not blooming, this means he is sad"
      
    json_object = json.dumps(data, indent=2)
    
    with open("Data/myPokemon.json", "a") as outfile:
      outfile.write(json_object + " ")
  
