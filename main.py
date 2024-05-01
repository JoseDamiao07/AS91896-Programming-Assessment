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

def show_pizzas(customer):
  index = 1
  print()
  for pizza_type in orders[customer]:
    what_pizza = pizza_type[0]
    how_many = pizza_type[1]
    price = pizzas[what_pizza]
    total_price = how_many * pizzas[what_pizza]
    print("{}. {}, ${:.2f} x {} - ${:.2f}"
          .format(index, what_pizza, price, how_many, total_price))
    index += 1

def view_current_order(customer):
  index = 1
  print()
  order_price = 0
  for pizza_type in orders[customer]:
    what_pizza = pizza_type[0]
    how_many = pizza_type[1]
    price = pizzas[what_pizza]
    total_price = how_many * pizzas[what_pizza]
    order_price += total_price
    print("{}. {}, ${:.2f} x {} - ${:.2f} (enter {} to remove)"
          .format(index, what_pizza, price, how_many, total_price, index))
    index += 1
  print("{}. Total - ${}".format(index, order_price))
  print("{}. Return (enter {})".format(index + 1, index + 1))

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
      orders[customer_name] = []
      while True:
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
            pizza_amount -= chosen_pizza_amount
        elif function_choice == 2:
          while True:
            view_current_order(customer_name)
            order_function_choice = choice_verification(
              1, len(orders[customer_name]) + 1)
            if order_function_choice == len(orders[customer_name]) + 2:
              break
            else:
              pizza_amount += orders[customer_name][order_function_choice - 1]
              orders[customer_name].pop(order_function_choice - 1)
        elif function_choice == 3:
          print("fungus3")
        elif function_choice == 4:
          break
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
