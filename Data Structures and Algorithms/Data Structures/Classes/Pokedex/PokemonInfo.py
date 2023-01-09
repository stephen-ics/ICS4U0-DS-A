from Classes.Pokedex.stats import Stats

class PokemonInfo:
  '''
  Info of a Pokemon contained in the Pokedex which contains its id, data, language, base, name, description, type and stats

  Attributes
  ----------
  id : int
    The id of the pokemon being searched
  data : dictionary
    A dictionaries containing the info of each Pokemon
  language : str
    The language of the Pokedex
  base : dictionary
    A dictionary of the base stats of the pokemon
  name : str
    The name of the Pokemon species
  description : str
    The description of the Pokemon
  type : list
    A list of the types of the Pokemon
  stats : Stats
    An object containing the stats of each set Pokemon
    
  Methods
  -------
  setInfo(description : str) -> str
    Sets the description of the object and returns the new description as a string
  setType(type : list) -> list
    Sets the type of the object and returns the new type as a list
  setName(name : str) -> str
    Sets the name of the object and returns the new name as a string
  '''
  
  def __init__(self, id, data, language):
    '''
    Constructs a PokemonInfo object
    
    Parameters
    ----------
    id : int
      The id of the pokemon being searched
    data : dictionary
      A dictionaries containing the info of each Pokemon
    language : str
      The language of the Pokedex
    base : dictionary
      A dictionary of the base stats of the pokemon
    name : str
      The name of the Pokemon species
    description : str
      The description of the Pokemon
    type : list
      A list of the types of the Pokemon
    stats : Stats
      An object containing the stats of each Pokemon
    '''
    self.id = id - 1
    self.data = data
    self.language = language
    self.base = self.data["base"]
    self.name = self.data["name"][self.language]
    print(self.data)
    self.description = self.data["description"]
    self.type = self.data["type"]
    self.stats = None

  def __str__(self):
    '''
    Returns the string representation of the PokemonInfo object

    Returns
    -------
    Returns the string representation of the PokemonInfo object as a string
    '''
    return "This pokemon is called: '" + str(self.name) + "'. " + self.description 

  def __repr__(self):
    '''
    Returns the object representation of the PokemonInfo object

    Returns
    -------
    Returns the object representation of the Pokedex object as a string
    '''
    return f'PokemonInfo("{self.name}", "{self.description}", "{self.type}")'

  def getStats(self):
    '''
    Returns the stats of the Pokemon
    
    Returns
    -------
    Returns the stats of the Pokemon as a Stats object 
	  '''
    return Stats(self.base)
    
  def setInfo(self, description):
    '''
    Sets and returns the new description of the Pokemon

    Parameters
    ----------
    description : str
    
    Returns
    -------
    Returns the new description as a string
	  '''
    self.description = description

  def setType(self, type):
    '''
    Sets and returns the new type of the Pokemon

    Parameters
    ----------
    type : list
    
    Returns
    -------
    Returns the new type as a list
	  '''
    self.type = type
    
  def setName(self, name):
    '''
    Sets and returns the new name of the Pokemon

    Parameters
    ----------
    name : str
    
    Returns
    -------
    Returns the new name as a string
	  '''
    self.name = name
    
