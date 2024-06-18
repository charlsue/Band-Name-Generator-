print("Welcome to the Band Name Generator!")
print("\n")
while True:
  city_grew_up_in = input("What's the name of the city you grew up in? \n")
  print("\n")
  pet_name = input("What's your pet's name?\n")
  print("\n")
  print("Your band name could be " + city_grew_up_in + " " + pet_name)
  print("\n")
  print("Thank you for using the Band Name Generator!")
  print("\n")
  try_again = input("Would you like to try again? (y/n)\n")
  if try_again == "y" or try_again == "Y": 
    continue
  else:
    break
