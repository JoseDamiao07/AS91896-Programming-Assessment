def option_choice(min, max):
  while True:
    try:
      choice = int(input("\n>>> "))
      if min <= choice <= max:
        return choice
      print("\nSorry, that isn't an option. Please try again.")
    except ValueError:
      print("\nSorry, that isn't an option. Please try again.")

print("Welcome to the Crusty Pizzas' Pizza Program!")
while True:
  print("What would you like to do?\n")
  print("\t1. Begin an order (enter 1)")
  print("\t2. Management summary (enter 2)")
  print("\t3. View orders (enter 3)")
  print("\t4. End session (enter 4)")
  function_choice = option_choice(1, 4)
  if function_choice == 1:
    print("fungus1")
  elif function_choice == 2:
    print("fungus2")
  elif function_choice == 3:
    print("fungus3")
  elif function_choice == 4:
    break