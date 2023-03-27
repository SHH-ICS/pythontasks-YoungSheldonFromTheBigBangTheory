# TASK: Update both functions to reverse the letters in the name and provide the square root of the users age.
import math

def reverseName(myName):
  # Write your function here
  result = myName[::-1]
  return result
  
def rootAge(myAge):
  # Wrie your function here
  result = math.sqrt(float(myAge))
  return result
  
me = input("What is your name? ")
im = input("What is your age? ")

print("Your name in reverse is: ",reverseName(me))
print("The square root of your age is: ",rootAge(im))
