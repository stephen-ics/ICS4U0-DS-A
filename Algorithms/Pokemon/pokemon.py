from abc import ABC, abstractmethod

class Pokemon(ABC):
  '''
  A Pokemon object that inherits the properties of its parent class LivingCreature and is categorized into name, level, totalHp, hp, attack, defense, speed, and fainted status 
  
  Attributes
  ----------
  __name : str
    The name of the Pokemon
  __level : int
    The level of the Pokemon
  __totalHp : float
    The total health of the Pokemon
  __hp : float
    The health of the Pokemon
  __attack : float
    The attack power of the Pokemon
  __defense : float
    The defense power of the Pokemon
  __speed : float
    The speed of the Pokemon
  __type : string
    The type of the Pokemon
  __exp : int
    The amount of experience of the Pokemon  
    The default value of the exp int is 0
  __fainted : boolean
    If the Pokemon is fainted
    The default value of the fainted boolean is False
  
  Methods
  -------
  takeDamage(damage : float) -> float
    Returns the damage dealt of the pokemon
  takeDamage(damage : float, type : str) -> float
    Returns the health of the pokemon after taking types into account
  attack(move : string) -> float
    Returns the damage the pokemon will inflict
  heal() -> int
    Heals the pokemon to its max hp and returns the new hp
  heal(healthAmount : int) -> int
    Heals the pokemon by healAmount
  levelUp() -> int
    Levels up the Pokemon by 1 and returns the new level
  levelUp(exp : int) -> int
    Levels up the Pokemon and returns the new level
  __recaliberateStats() -> void
    Recaliberates the stats of the Pokemon after levelling up
  '''

  def __init__(self, name, level, totalHp, attack, defense, speed, type):
    '''
    Constructs a Pokemon object

    Parameters
    ----------
    name : str
      The name of the Pokemon
    level : int
      The level of the Pokemon
    totalHp : float
      The total health of the Pokemon
    hp : float
      The health of the Pokemon
    attack : float
      The attack power of the Pokemon
    defense : float
      The defense power of the Pokemon
    speed : float
      The speed of the Pokemon
    type : string
      The type of the Pokemon
    '''
    self.name = name
    self.level = level
    self.totalHp = totalHp
    self.hp = totalHp
    self.attack = attack
    self.defense = defense
    self.speed = speed
    self.type = type
    self.exp = 0
    self.fainted = False

  def __str__(self):
    '''
    Returns the string representation of the Pokemon object

    Returns
    -------
    Returns the string representation of the Pokemon object as a string
    '''
    return "Level " + self.level + " " + self.species + ". Name: " + self.name

  def __repr__(self):
    '''
    Returns the object representation of the Pokemon object
  
    Returns
    -------
    Returns the object representation of the Pokemon object as a string
    '''
    return f'Stats("{self.species}", "{self.name}", "{self.level}", "{self.hp}", "{self.fainted}")'

  @abstractmethod
  def attack(self):
    return
    
  def takeDamage(self, damage):
    '''
    Returns the damage taken after including the defense of the pokemon

    Parameters
    ----------
    damage : int
    
    Returns
    -------
    The amount of damage taken as a float
	  '''
    
    damageTaken = round(damage / (1 + (self.__defense/100)), 2)
    hp = round(self.hp - damageTaken, 2)
    self.hp = hp
    
    if self.hp <= 0:
      self.fainted = True

    return damageTaken

  def takeDamage(self, damage, type):
    '''
    Returns the damage taken after including the defense and type of the pokemon

    Parameters
    ----------
    damage : int
    type : str
    
    Returns
    -------
    The amount of damage taken as a float
	  '''
    
    damageTaken = round(damage / (1 + (self.__defense/100)), 2)
    if type == "fire":
      if self.type == "water":
        damageTaken /= 2
      elif self.type == "grass":
        damageTaken *= 2
    if type == "water":
      if self.type == "grass":
        damageTaken /= 2
      elif self.type == "fire":
        damageTaken *= 2
    if type == "grass":
      if self.type == "fire":
        damageTaken /= 2
      elif self.type == water:
        damageTaken *= 2

  def heal(self):
    '''
    Returns the full health of the Pokemon after being healed
    
    Returns
    -------
    The amount full health of the Pokemon as an int
    '''
    self.hp = self.__totalHp
    return self.hp

  def heal(self, healAmount):
    '''
    Returns the health of the Pokemon after being healed by healAmount

    Parameters
    ----------
    healAmount : int
    
    Returns
    -------
    The new health of the Pokemon after being healed as an int
	  '''
    if self.hp + healAmount <= totalHp:
      self.hp += healAmount
    else:
      self.hp = totalHp
    return self.hp

  def levelUp(self):
    '''
    Returns the level of the Pokemon after the Pokemon levels up by 1 level
    
    Returns
    -------
    The new level of the Pokemon as an int
	  '''
    self.level += 1
    self.recaliberateStats()

  def levelUp(self, exp):
    '''
    Returns the level of the Pokemon after the exp is added

    Parameters
    ----------
    exp : int
    
    Returns
    -------
    The level of the Pokemon as an int
    '''
    self.level += exp//100
    self.exp += exp % 100
    
    self.__recaliberateStats()
    return self.level
  
  def __recaliberateStats(self):
    '''
    Sets the new stats to Pokemon after levelling up
    
    Returns
    -------
    None
    '''
    self.totalHp *= (1 + (self.level/100))
    self.hp = self.totalHp
    self.attack *= (1 + (self.level/100))
    self.defense *= (1 + (self.level/100))
    self.speed *= (1 + (self.level/100))
    
