#-----------------------------------------------------------------------------
# Name:        ICS4UO Review 
# Purpose:     To review the ideas covered in ICS3UO along with some added concepts!
#
# Author:      Stephen Ni
# Created:     20-Sept-2022
# Updated:     23-Sept-2022
#-----------------------------------------------------------------------------

def checkPrime(num):
  """"
  Check if numer is a prime number
  
  Checks the number to see if it's a prime number by looping through each number and finding potential factors using the modulus function

  Parameters
  ----------
  num : int
    integer user is checking (any real number larger than 2)
  
  Returns
  -------
  Boolean
    if found to be prime number return true (more factors than 1 and itself), else return false
  """
  # Checking if number is under 2, if so return false
  if num < 2:
    print("The number must be larger than 2!")
    print()
    return False

  # Initializing list of factors 
  factors = [(1, num)]
  i = 2

  # Check all numbers for i^2 under num
  while i*i <= num:
    # If modulus is 0, add to factors, and increment i
    if num % i == 0:
      factors.append((i, num/i))
    i += 1

  # If there are more than 1 pair of factors (1 and itself), it is not a prime number
  if len(factors) > 1:
    print(str(num) + " is not a prime. It has the following factors: " + str(factors))
    print()
    return False

  return True

def simpleEncrypt(msg):
  """"
  Encrypt message with simple encryption
  
  Encrypt message by shifting each character three positions up the ASCII Table

  Parameters
  ----------
  msg : String
    message to be encoded (any string)
  
  Returns
  -------
  String
    the encrypted message after shifting all letters up three times in the ASCII Table
  """

  # Initializing encrypted message
  encryptedMsg = ""
  for char in msg:
    # convert to ASCII value
    value = ord(char)
    # encrypt by adding 2
    encryptedValue = value + 2
    # convert back to char
    encryptedChar = chr(encryptedValue)

    # Add encrypted char to message
    encryptedMsg += encryptedChar
  return encryptedMsg

def simpleDecrypt(msg):
  """"
  Decrypt message with simple decryption
  
  Decrypt message by shifting each character three positions down the ASCII Table

  Parameters
  ----------
  msg : String
    message to be decoded (any string)
  
  Returns
  -------
  String
    the decrypted message after shifting all letters down three times in the ASCII Table
  """

  # Initializing decrypted message
  decryptedMsg = ""

  # For characters in message
  for char in msg:
    # convert to ASCII value
    value = ord(char)
    # decrypt by subtracting 2
    decryptedValue = value - 2
    # convert back to char
    decryptedChar = chr(decryptedValue)

    # Add decrypted char to message
    decryptedMsg += decryptedChar
  return decryptedMsg
  

def caesarCipherEncrypt(msg, shift):
  """"
  Encrypt message with simple Caesar Cipher
  
  Encrypt message by shifting each character by 'shift' positions down the ASCII Table, when the shift value is over 26, use the modulus function to take the remainder and shift it by the remainder

  Parameters
  ----------
  msg : String
    message to be decoded (any string)
  shift : int
    amount to shift each character by (any positive natural number)
  
  Returns
  -------
  String
    the encrypted message after the Caeser Cipher
  """

  # Initializing encrypted message
  encryptedMsg = ""

  # For characters in message
  for char in msg:
    # convert to ASCII value
    value = ord(char)
    # encrypt by adding 'shift' value remainder of 26
    encryptedValue = value + (shift % 26)
    # convert back to char
    encryptedChar = chr(encryptedValue)

    # Add encrypted char to message
    encryptedMsg += encryptedChar

  return encryptedMsg 

# Initializing guesses
guesses = 0
incorrectGuesses = 0

# Print introduction
print("Hello, I am Cyberbot, here to educate you on ethical computer uses")
print("Today's topic will be, the importance of staying safe on the internet!")
print()
print("One of the best ways to stay safe on the internet is to have secure passwords")
print("A way to encrypt your password is through very long prime numbers, as used in the RSA encrpytion")
print()

# Introduction (Prime Numbers)
print("A prime number is a number that is only divisible by 1 and itself")
print("Let's try to find a prime number!")
print()

# Gather user input and add to total guesses
num = int(input("Input number: "))
guesses += 1
print()

# Loop if not prime number
while checkPrime(num) == False:
  # Add total + incorrect guesses and answer again
  num = int(input("Input number: "))
  print()
  guesses += 1
  incorrectGuesses += 1

# User has guessed correctly, print congrulations
print()
print("Yes! " + str(num) + " is a prime number!")
print()

# Lesson 2 (Simple Encryptions + Decryptions)

# Introduction to encryptions
print("Now that you have checked prime numbers, let's try a way to actually encrypt messages")
print()
print("Let's start off with a simple encryption by shifting every character 2 spots down the ASCII Table")
print("For example, act would become cev")
print()
print("What would 'hello' become?")
print()

# Gathering user answer for encryption
answer = input("Answer: ")
guesses += 1

# Loop if not correct encryption
while answer != "jgnnq":
  # Add total + incorrect guesses and answer again
  print("'" + answer + "' is not the correct answer!")
  print()
  answer = input("Answer: ")
  guesses += 1
  incorrectGuesses += 1

# User has guessed correctly, print congrulations
print()
print("Congratulations! '" + answer + "' is the correct answer!")
print()

# Trying out the encrypter
print("Now, try out the encrypter by yourself!")

# Gather input message
msg = input("What message would you like to encrypt: ")

# Insert message into encrypter function + print out message
encryptedMsg = simpleEncrypt(msg)
print()
print("Your encrypted message: " + encryptedMsg)
print()

# Introduction to decryptions
print("Of course, there is no point in encrypting a message if there is no way to decrypt it")
print("To decrypt a message, simply reverse the processing of encrypting the message")
print("In this case, all you have to do is shift every character 2 spots up the ASCII Table")
print()
print("For example, cev would become act")
print()
print("What would 'ecv' become?")
print()

# Gathering user answer for decryption and add to total guesses
answer = input("Answer: ")
guesses += 1

# Loop until user answers correctly
while answer != "cat":
  print("'" + answer + "' is not the correct answer!")
  print()

  # Adding to total + incorrect guesses and answer again
  answer = input("Answer: ")
  guesses += 1
  incorrectGuesses += 1

# User has guessed correctly, print congrulations
print()
print("Congratulations! '" + answer + "' is the correct answer!")
print()

# Trying out the decrypter
print("Now, try out the decrypter for yourself!")

# Gather input message
msg = input("What message would you like to decrypt: ")

# Insert message into encrypter function + print out message
decryptedMsg = simpleDecrypt(msg)
print()
print("Your decrypted message: " + decryptedMsg)
print()

# Lesson 3 (Caesar Cipher)
# Introduction to Caesar Cipher
print("Great work! Now, we will take a look at the Caesar Cipher, a slightly more complicated cipher")
print()
print("The Caesar Cipher is  a simple shift, where the shift amount is entered by the user")
print("You may or may not have noticed before, but when you try to decrypt the letters over a shift of 26, you will end up with characters far beyond the alphabet")
print()
print("We can use the modulus operator to make sure that when letter shifting, the index will wrap around the end of the alphabet when it is reached, this will allow us to encrypt the message as if it was a shift under 26")
print()
print("Let's try to use the Caesar Cipher!")
print()
print("What would your encrypted message be if you used the Caesar Cipher to shift 'hello' 29 spots down the ASCII Table")
print()

# Gather user answer + add to total guesses
answer = input("Answer: ")
guesses += 1

# Loop until user answers correctly
while answer != "khoor":
  print("'" + answer + "' is not the correct answer!")
  print()

  # Adding to total + incorrect guesses and answer again
  answer = input("Answer: ")
  guesses += 1
  incorrectGuesses += 1

# User has guessed correctly, print congrulations
print()
print("Congratulations! '" + answer + "' is the correct answer!")
print()
print("This is because 29 / 26 would result in a remainder of three, wrapping around the whole alphabet once and then adding by an additional 3 steps")
print()

# Trying out the Caesar Cipher!
print("Now, try out the Caesar Cipher by yourself!")

# Gather message + shift
msg = input("What message would you like to encrypt: ")
shift = int(input("How much would you like to shift them by: "))

# Encrypt message using Caesar Cipher Function
encryptedMsg = caesarCipherEncrypt(msg, shift)
print()
print("Your encrypted message: " + encryptedMsg)
print()

# Conclusion!
print("That's it for this little lesson!")
print("Hope you gained some insight on cybersecurity and encrypting/decrypting messages")
print()

# Print total guesses
print("Total guesses: " + str(guesses))
print("Total incorrect guesses: " + str(incorrectGuesses))

# Calclulate user accuracy
correctGuesses = guesses-incorrectGuesses
accuracy = int((correctGuesses/guesses)*100)
print("You had an answering accuracy of: " + str(accuracy) + "%")

# Farewells
print()
print("Have a great day! :)")


