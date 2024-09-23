print("Build you house out of: \n 1 straw \n 2 sticks \n 3 bricks")
houseType = input("> ")
if (houseType == "1"):
  print("HUFF PUFF, THE WOLF BLEW YOUR STRAW HOUSE!")
elif (houseType == "2"):
  print("HUFFF PUFFF, The wolf blew down your house of sticks!")
elif (houseType == "3"):
  print("HUFFPHH PUFFPHH, the house wouldn't budge. Well done! \n")
  print("Will you let the wolf in? (y/n)")

  naivePig = input(">")
  if (naivePig == "y"):
    print("WHAT, the wolf is hungry 😈")
  elif (naivePig == "n"):
    print("The wolf ran away. You're alive for another day...")
  else:
    print("Invalid input")
else:
  print("Invalid input")
