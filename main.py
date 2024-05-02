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

details = {}

pizzas_sold = {
  "Cheese": 0,
  "Garlic Cheese": 0,
  "Pepperoni": 0,
  "Hawaiian": 0,
  "Veggie": 0,
  "Beef and Onion": 0,
  "Margherita": 0,
  "Meat Lovers": 0,
  "Veggie Supreme": 0,
  "Double Pepperoni": 0,
  "Four Cheese": 0,
  "The Works": 0,
}

def user_choice(min, max, error_text):
  while True:
    try:
      choice = int(input("\n>>> "))
      if min <= choice <= max:
        return choice
      print(error_text)
    except ValueError:
      print(error_text)

def main_menu():
  print("\nWhat would you like to do?\n")
  print("\t1. Begin an order (enter 1)")
  print("\t2. Management summary (enter 2)")
  print("\t3. View orders (enter 3)")
  print("\t4. End session (enter 4)")
  return user_choice(1, 4, "\nSorry, that isn't an option, please try again.")

def create_order(order_type):
  customer_name = input("\nWhat is the customer's name?\n\n>>> ").strip()
  if order_type == 1:
    orders[customer_name] = []
    details[customer_name] = [1]
  elif order_type == 2:
    customer_address = input("\nWhat is the customer's address?\n\n>>> "
    ).strip().lower()
    customer_number = input("\nWhat is the customer's phone number?\n\n>>> ").strip()
    orders[customer_name] = []
    details[customer_name] = [2, customer_address, customer_number]
  print("\nHow many pizzas would the customer like?")
  pizza_amount = user_choice(1, 5, 
  "\nSorry, there's a max of 5 pizzas per customer, please try again.")
  return customer_name, pizza_amount

def order_menu(pizza_amount, customer_name):
  while True:
    print("\n\t1. Choose pizza to add (enter 1)")
    print("\t2. View current order (enter 2)")
    print("\t3. Finish order (enter 3)")
    print("\t4. Cancel order (enter 4)")
    order_menu_choice = user_choice(1, 4, 
    "\nSorry, that isn't an option, please try again.")
    if order_menu_choice == 1:
      if pizza_amount > 0:
        i = 1
        print()
        for pizza, price in pizzas.items():
          print("\t{}. {}, ${:.2f} (enter {})".format(i, pizza, price, i))
          i += 1
        print("\t{}. Cancel (enter {})".format(i, i))
        pizza_choice = user_choice(1, i, 
        "\nSorry, that isn't an option, please try again.\n")
        if pizza_choice < i:
          print("\nHow many {} pizzas would the customer like?"
                .format(list(pizzas)[pizza_choice - 1]))
          chosen_pizza_amount = user_choice(1, pizza_amount, 
          "\nSorry, the customer can only add {} more pizzas.".format(pizza_amount))
          orders[customer_name].append(
          [list(pizzas)[pizza_choice - 1], chosen_pizza_amount])
          pizza_amount -= chosen_pizza_amount
        else:
          print("\nSorry, the customer can't add any more pizzas.")
    elif order_menu_choice == 2:
      while True:
        i = 1
        order_price = 0 
        print()
        for item in orders[customer_name]:
          print("\t{}. {}, ${:.2f} x {} - ${:.2f} (enter {} to remove)"
          .format(i, item[0], pizzas[item[0]], item[1], pizzas[item[0]] * item[1], i))
          order_price += pizzas[item[0]] * item[1]
          i += 1
        print("\t{}. Total - ${:.2f}".format(i, order_price))
        print("\t{}. Return (enter {})".format(i + 1, i + 1))
        current_order_choice = user_choice(1, len(orders[customer_name]) + 2, 
                     "\nSorry, that isn't an option, please try again.")
        if current_order_choice == len(orders[customer_name]) + 2:
          break
        elif current_order_choice == len(orders[customer_name]) + 1:
          print("\nSorry, that isn't an option, please try again.")
        else:
          pizza_amount += orders[customer_name][current_order_choice - 1][1]
          orders[customer_name].pop(current_order_choice - 1)
    elif order_menu_choice == 3:
      finish = 1
      order_price = 0
      if pizza_amount > 0:
        print("\nThe customer has not ordered all his pizzas.")
        print("Are you sure you want to finish the order?")
        print("\n\t1. Yes (enter 1)\n\t2. No (enter 2)")
        finish = user_choice(1, 2, "\nSorry, that isn't an option, please try again.")
      if finish == 1:
        if details[customer_name][0] == 1:
          print("\n{}, pickup".format(customer_name.capitalize()))
        else:
          print("\n{}, delivery".format(customer_name.capitalize()))
          print("{}, {}".format(details[customer_name][1], details[customer_name][2]))
        i = 1
        for item in orders[customer_name]:
          print("\t{}. {}, ${:.2f} x {} - ${:.2f}"
          .format(i, item[0], pizzas[item[0]], item[1], pizzas[item[0]] * item[1]))
          i += 1
          order_price += pizzas[item[0]] * item[1]
          pizzas_sold[item[0]] += item[1]
        print("\t{}. Total - ${:.2f}".format(i, order_price))
        print("\t{}. Finish and add order (enter {})".format(i + 1, i + 1))
        print("\t{}. Return (enter {})".format(i + 2, i + 2))
        current_order_decision = user_choice(i, i + 2, 
                                "\nSorry, that isn't an option, please try again.")
        if current_order_decision == i + 1:
          break
    else:
      print("\nAre you sure you want to cancel the order?")
      print("\n\t1. Yes (enter 1)\n\t2. No (enter 2)")
      cancel = user_choice(1, 2, "\nSorry, that isn't an option, please try again.")
      if cancel == 1:
        orders.pop(customer_name)
        break

def view_orders():
  for name, order in orders.items():
    order_price = 0
    if details[name][0] == 1:
      print()
      print("{} - Pickup".format(name))
    else:
      print()
      print("{} - Delivery".format(name))
      print("{}, {}".format(details[name][1], details[name][2]))
    for pizza in order:
      print("  -  {} x {} - ${:.2f}".format(pizza[0], pizza[1], pizzas[pizza[0]]))
      order_price += pizzas[pizza[0]]
    print("  -  Total - ${:.2f}".format(order_price))

def management_summary():
  print()
  i = 1
  regular_sold = 0
  gourmet_sold = 0
  for pizza, quantity in pizzas_sold.items():
    print("\t{}. {}, ${:.2f} x {} - ${:.2f}"
          .format(i, pizza, pizzas[pizza], quantity, pizzas[pizza] * quantity))
    i += 1
    if pizzas[pizza] == 8.50:
      regular_sold += quantity
    else:
      gourmet_sold += quantity
  print("\t{}. Total regular x {} - ${:.2f}"
        .format(i, regular_sold, 8.50 * regular_sold))
  print("\t{}. Total gourmet x {} - ${:.2f}"
        .format(i + 1, gourmet_sold, 13.50 * gourmet_sold))
  print("\t{}. Total {} pizzas sold - ${:.2f}"
        .format(i + 2, regular_sold + gourmet_sold, 
                (8.50 * regular_sold) + (13.50 * gourmet_sold)))

while True:
  print("Welcome to the Crusty Pizzas' Pizza Program!")
  main_choice = main_menu()
  if main_choice == 1:
    print("\n\t1. Pickup (enter 1)")
    print("\t2. Delivery (enter 2)")
    print("\t3. Cancel (enter 3)")
    order_type = user_choice(1, 3, "\nSorry, that isn't an option, please try again.")
    if order_type != 3:
      current_order_name, current_order_amount = create_order(order_type)
      order_menu(current_order_amount, current_order_name)
  elif main_choice == 2:
    management_summary()
  elif main_choice == 3:
    view_orders()
  else:
    print("\nThanks for using the Crusty Pizzas' Pizza Program!")
    break