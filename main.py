pizzas = {
  "Cheese": 8.50,
  "Garlic Cheese": 8.50,
  "Pepperoni": 8.50,
  "Hawaiian": 8.50,
  "Veggie": 8.50,
  "Beef and Onion": 8.50,
  "Margherita": 8.50,
  "Meat Lovers": 13.50,
  "Veggie Supreme": 13.50,
  "Double Pepperoni": 13.50,
  "Four Cheese": 13.50,
  "The Works": 13.50,
}

orders = {}

def choice_verification(min, max):
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
  print("\nWhat would you like to do?\n")
  print("\t1. Begin an order (enter 1)")
  print("\t2. Management summary (enter 2)")
  print("\t3. View orders (enter 3)")
  print("\t4. End session (enter 4)")
  function_choice = choice_verification(1, 4)
  if function_choice == 1:
    print("\n\t1. Pickup (enter 1)")
    print("\t2. Delivery (enter 2)")
    print("\t3. Cancel (enter 3)")
    order_type = choice_verification(1, 3)
    if order_type == 1:
      customer_name = input("\nWhat is the customer's name?\n\n>>> ")
      print("\nHow many pizzas would the customer like?")
      pizza_amount = choice_verification(1, 5)
      print("\n1. Choose pizza to add (enter 1)")
      print("2. View current order (enter 2)")
      print("3. Finish order (enter 3)")
      print("4. Cancel order (enter 4)")
      function_choice = choice_verification(1, 4)
      if function_choice == 1:
        i = 1
        print()
        for pizza, price in pizzas.items():
          print("{}. {}, ${:.2f} (enter {})".format(i, pizza, price, i))
          i += 1
        print("{}. Cancel (enter {})".format(len(pizzas) + 1, len(pizzas) + 1))
        pizza_choice = choice_verification(1, len(pizzas) + 1)
        if pizza_choice < len(pizzas):
          print("\nHow many {} pizzas would the customer like?"
                .format(list(pizzas)[pizza_choice - 1]))
          chosen_pizza_amount = choice_verification(1, pizza_amount)
          orders[customer_name].append(
            [list(pizzas)[pizza_choice - 1], chosen_pizza_amount])
      elif function_choice == 2:
        print("fungus2")
      elif function_choice == 3:
        print("fungus3")
      elif function_choice == 4:
        print("fungus4")
    elif order_type == 2:
      customer_name = input("\nWhat is the customer's name?\n\n>>> ")
      customer_address = input("\nWhat is the customer's address?\n\n>>> ")
      customer_number = input("\nWhat is the customer's phone number?\n\n>>> ")
  elif function_choice == 2:
    print("fungus2")
  elif function_choice == 3:
    print("fungus3")
  elif function_choice == 4:
    break
