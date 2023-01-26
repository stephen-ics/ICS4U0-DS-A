#-----------------------------------------------------------------------------
# Name:        Data Structures Assignment
# Purpose:     To Create a small program that demonstrates your understanding of the materials researched.
#
# Author:      Stephen Ni
# Created:     4-Oct-2022
# Updated:     22-Nov-2022
#-----------------------------------------------------------------------------

import json 
from Classes.Pokedex.pokedex import Pokedex
from Classes.Pokemon.pokemon import Pokemon
from Classes.Pokemon.PokemonList.squirtle import Squirtle
from Classes.Pokemon.PokemonList.charmander import Charmander
from Classes.Pokemon.PokemonList.bulbasaur import Bulbasaur

with open('Data/pokemon.json', 'r') as outfile:
  data = json.load(outfile)

language = "english"

myPokedex = Pokedex(data, language)
print(myPokedex)
print()
print("Now it's time to choose your first Pokemon!")
print("We have 3 options: charmander, squirtle, and bulbasaur")
print()

myList = []

for i in range(3):
  myList.append(i)

pokeList = myPokedex.getMultiple(myList)

for pokemon in pokeList:
  print(pokemon.name)
  print(pokemon.description)
  print()

pokeList[0].setInfo('Updated info!')
print(pokeList[0].description)
print(pokeList[0].__repr__())
print(pokeList[0].getStats().__repr__())

squirtle =  {
    "id": 7,
    "name": {
      "english": "Squirtle",
      "french": "Carapuce"
    },
    "description": "When it retracts its long neck into its shell, it squirts out water with vigorous force.",
    "type": [
      "Water"
    ],
    "base": {
      "HP": 44,
      "Attack": 48,
      "Defense": 65,
      "Sp. Attack": 50,
      "Sp. Defense": 64,
      "Speed": 43
    }
}

squirtle2 =  {
    "base": {
      "HP": 44,
      "Attack": 48,
      "Defense": 65,
      "Speed": 43
    }
}

HP = squirtle2["base"]["HP"]
attack = squirtle2["base"]["Attack"]
defense = squirtle2["base"]["Defense"]
speed = squirtle2["base"]["Speed"]


mySquirtle = Squirtle("Joe", 7, HP, attack, defense, speed, "water", True)
myCharmander = Charmander("Joe", 7, HP, attack, defense, speed, "fire", True)
myBulbasaur = Bulbasaur("Joe", 7, HP, attack, defense, speed, "grass", True)

mySquirtle.writeSquirtleStatus()
myCharmander.writeCharmanderStatus()
myBulbasaur.writeBulbasaurStatus()

with open('Data/squirtle.json', 'r') as outfile:
  squirtleData = json.load(outfile)

squirtleList = []
for i in range(len(squirtleData)):
  currentSquirtle = squirtleData[i]
  currentSquirtleObject = Squirtle(currentSquirtle["name"], currentSquirtle["level"], currentSquirtle["hp"], currentSquirtle["attack"], currentSquirtle["defense"], currentSquirtle["speed"], currentSquirtle["type"], currentSquirtle["wearingSunglasses"])
  squirtleList.append(currentSquirtleObject)

for squirtle in squirtleList:
  print(squirtle)




  
  


