#-----------------------------------------------------------------------------
# Name:        Recursion Assignment
# Purpose:     To Create a small recursive program that demonstrates your understanding of the recursion
#
# Author:      Stephen Ni
# Created:     26-Oct-2022
# Updated:     1-Nov-2022
#-----------------------------------------------------------------------------

# Initialize cache as a dictionary
def solveMinimumDays(numOranges):
  orangesCache = {0:0, 1:1}
  def searchDays(numOranges):
    # Check if numOranges has already been calculated (already in cache) 
    if numOranges in orangesCache:
      # If value already calculated, return calculated value
      return orangesCache[numOranges]
  
    # Calculate minimum num days to get to where numOranges is divisble by 2 and 3, then call recursive function to find minimum num days of the quotient
    halfOranges = 1 + (numOranges % 2) + searchDays(numOranges // 2)
    oneThirdOranges = 1 + (numOranges % 3) + searchDays(numOranges // 3)
  
    # Find minimum day by comparing minimum days of both cases
    if halfOranges > oneThirdOranges:
      # If less days to eat 2/3rds of oranges, minimum days = days to eat 2/3rds of oranges
      minimumDays = oneThirdOranges
    elif halfOranges < oneThirdOranges:
      # If less days to eat half of oranges, minimum days = days to half oranges
      minimumDays = halfOranges
    else:
      # Else if number of days is equal, pick one of the options
      minimumDays = halfOranges
  
    # Add the minimum number of days to the cache to be referenced in the future
    orangesCache[numOranges] = minimumDays
  
    # Return the minimum number of days it takes to eat all the oranges
    return minimumDays
  
  # Minimum num days to eat 10 oranges
  print(searchDays(numOranges))

solveMinimumDays(100)

