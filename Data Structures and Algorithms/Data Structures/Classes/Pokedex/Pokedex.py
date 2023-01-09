from Classes.Pokedex.pokemonInfo import PokemonInfo
import json
    
class Pokedex:
  '''
  A Pokedex that is categorized into data and language
  
  Attributes
  ----------
  data : list
    A list of dictionaries containing the info of each Pokemon
  language : str
    The language of the Pokedex
    
  Methods
  -------
  getPokemon(id : int) -> none
    Returns an object of the class PokemonInfo
  definePokemon(base : dictionary) -> none
    Writes a new pokemon to pokemon.json
  updatePokemon(base) -> none
    Updates a pre-existing pokemon to pokemon.json
  '''
  
  def __init__(self, data, language):
    '''
    Constructs a Pokedex object

    Parameters
    ----------
    data : list
      A list of dictionaries containing the info of each Pokemon
    language : str
      The language of the Pokedex
    '''
    
    self.data = data
    self.language = language

  def __str__(self):
    '''
    Returns the string representation of the Pokedex object

    Returns
    -------
    Returns the string representation of the Pokedex object as a string
    '''
    
    return "This is your pokedex. Language: " + self.language

  def __repr__(self):
    '''
    Returns the object representation of the Pokedex object

    Returns
    -------
    Returns the object representation of the Pokedex object as a string
    '''
    return f'Pokedex("{self.data}", "{self.language}")'

  def getPokemon(self, id):
    '''
    Returns the info of the requested pokemon 

    Parameters
    ----------
    id : int
    
    Returns
    -------
    The info of the pokemon as a PokemonInfo object 
	  '''
    data = self.data[id]
    return PokemonInfo(id, data, self.language)

  def getMultiple(self, ids):
    '''
    Returns a list of info of the requested Pokemon

    Parameters
    ----------
    ids : list
    
    Returns
    -------
    A list of type list containing the info of the requested Pokemon of type Pokemon as a PokemonInfo object
	  '''
    pokemonList = []
    for id in ids:
      data = self.data[id]
      pokemonList.append(PokemonInfo(id, data, self.language))
      
    return pokemonList      
      
  def definePokemon(self, base):
    '''
    Appends the new base stats to pokemon.json

    Parameters
    ----------
    base : dictionary
    
    Returns  
    -------
    None
	  '''
    with open('Data/pokemon.json', 'r') as outfile:
      data = json.load(outfile)
      
    data.append(base)
    json_object = json.dumps(data, indent=2)
    
    with open("Data/pokemon.json", "w+") as outfile:
      outfile.write(json_object)

  def updatePokemon(self, base, index):
    '''
    Updates the base of the current pokemon to the base of the new Pokemon and writes it in the pokemon.json file

    Parameters
    ----------
    base : dictionary
    index : int
    
    Returns
    -------
    None
	  '''
    with open('Data/pokemon.json', 'r') as outfile:
      data = json.load(outfile)
      
    data[index-1] = base
    json_object = json.dumps(data, indent=2)
    
    with open("Data/pokemon.json", "w+") as outfile:
      outfile.write(json_object)
    

