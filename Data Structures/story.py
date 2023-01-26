import json 
from Classes.Pokedex.pokedex import Pokedex
from Classes.pokemon import Pokemon

# Pokemon info (JSON): https://github.com/fanzeyi/pokemon.json/blob/master/pokedex.json

# x = 5
# with open("json.txt", "w+") as outfile:
  # json.dump(x, outfile)

with open('Data/pokemon.json', 'r') as outfile:
  data = json.load(outfile)

print("Welcome to the Pokemon Center!")
print("Congratulations on reaching the age of 10! It's time for you to choose your first Pokemon")
print()
print("Here is a Pokedex for you to get started")
print("Pokedex obtained!")
print()
language = "english"
# language = input("What language would you like to set your Pokedex to: ").lower()
myPokedex = Pokedex(data, language)
print(myPokedex)
print()
print("Now it's time to choose your first Pokemon!")
print("We have 3 options: charmander, squirtle, and bulbasaur")
print()

  
      
  





      
  
  


