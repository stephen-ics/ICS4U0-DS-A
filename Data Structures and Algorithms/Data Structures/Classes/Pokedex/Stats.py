class Stats:
  '''
  The stats of the Pokemon that is categorized into its base, data, hp, attack, defense, spAttack, spDefense, and speed
  
  Attributes
  ----------
  base : dictionary
    The base stats of the Pokemon
  hp : int
    The hp of the Pokemon
  attack : int
    The attack power of the Pokemon
  defense : int
    The defense power of the Pokemon
  spAttack : int
    The spAttack power of the Pokemon
  spDefense : int
    The spDefense power of the Pokemon
  speed : int
    The speed of the Pokemon

  Methods
  -------
  setHp(hp : int) -> int
    Updates the hp and returns the new hp as an int
  setAttack(attack : int) -> int
    Updates the attack and returns the new attack as an int
  setDefense(defense : int) -> int
    Updates the defense and returns the new defense as an int
  setSpAttack(spAttack : int) -> int
    Updates the spAttack and returns the new spAttack as an int
  setSpDefense(spDefense : int) -> int
    Updates the spDefense and returns the new spDefense as an int
  setSpeed(speed : int) -> int
    Updates the speed and returns the new speed as an int
  '''
  
  def __init__(self, base):
    '''
    Constructs a Stats object
  
    Parameters
    ----------
    base : dictionary
      The base stats of the Pokemon
    hp : int
      The hp of the Pokemon
    attack : int
      The attack power of the Pokemon
    defense : int
      The defense power of the Pokemon
    spAttack : int
      The spAttack power of the Pokemon
    spDefense : int
      The spDefense power of the Pokemon
    speed : int
      The speed of the Pokemon
    '''
    
    self.base = base
    self.hp = base["HP"]
    self.attack = base["Attack"]
    self.defense = base["Defense"]
    self.spAttack = base["Sp. Attack"]
    self.spDefense = base["Sp. Defense"]
    self.speed = base["Speed"]
    
  def __str__(self):
    '''
    Returns the string representation of the Stats object

    Returns
    -------
    Returns the string representation of the Stats object as a string
    '''
    return "Stats of the Pokemon. Hp: " + str(self.hp) + ", Attack: " + self.description + ", Defense: " + str(self.defense) + ", spAttack: " + str(self.spAttack) + ", spDefense: " + str(self.spDefense) + ", speed" + str(self.speed)
    
  def __repr__(self):
    '''
    Returns the object representation of the Stats object

    Returns
    -------
    Returns the object representation of the Stats object as a string
    '''
    return f'Stats("{self.hp}", "{self.attack}", "{self.defense}", "{self.spAttack}", "{self.spDefense}", "{self.speed}")'
    
  def setHp(self, hp):
    '''
    Sets and returns the new hp in the Stats object

    Parameters
    ----------
    hp : int
    
    Returns
    -------
    Returns the new hp as an int
	  '''
    self.hp = hp
    return self.hp

  def setAttack(self, attack):
    '''
    Sets and returns the new attack in the Stats object

    Parameters
    ----------
    attack : int
    
    Returns
    -------
    Returns the new attack as an int
	  '''
    self.attack = attack
    return self.attack

  def setDefense(self, defense):
    '''
    Sets and returns the new defense in the Stats object

    Parameters
    ----------
    defense : int
    
    Returns
    -------
    Returns the new defense as an int
	  '''
    self.defense = defense
    return self.defense

  def setSpAttack(self, SpAttack):
    '''
    Sets the value of the spAttack parameter in the object and returns the new spAttack

    Parameters
    ----------
    spAttack : int
    
    Returns
    -------
    Returns the new spAttack as an int
	  '''
    self.spAttack = SpAttack
    return self.spAttack

  def setSpDefense(self, SpDefense):
    '''
    Sets the value of the spDefense parameter in the object and returns the new spDefense

    Parameters
    ----------
    spDefense : int
    
    Returns
    -------
    Returns the new spDefense as an int
	  '''
    self.spDefense = SpDefense
    return self.spDefense

  def setSpeed(self, speed):
    '''
    Sets the value of the speed parameter in the object and returns the new speed

    Parameters
    ----------
    speed : int
    
    Returns
    -------
    Returns the new speed as a int
	  '''
    self.speed = speed
    return self.speed
    
  def setAllStats(self, base):
    '''
    Sets a new base value and updates every stat, then returns the new base

    Parameters
    ----------
    base : dictionary
    
    Returns
    -------
    Returns the new base stats as a dictionary
	  '''
    self.base = base
    self.hp = base["HP"]
    self.attack = base["Attack"]
    self.defense = base["Defense"]
    self.spAttack = base["Sp. Attack"]
    self.spDefense = base["Sp. Defense"]
    self.speed = base["Speed"]
    
    return self.base