# Dictionary of pizzas and their prices. 
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

# Order dictionary to store the customer orders. 
# It is structured like so: 
# Dave: [[Cheese, 2], [Pepperoni, 3]].
orders = {}

# Details dictionary to store the customer's details.
# It is structured like so: 
# Dave: [type_of_order(1 (pickup) or 2 (delivery)), address(delivery), number(delivery)]
details = {}

# Pizzas sold dictionary to store the amount of specific pizzas sold.
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

# User choice function to verify input and only allow numbers.
def user_choice(min, max, error_text):
  """This function gets user input with a number and verifies it within some boundaries.
  Arguments: minimum choice, maximum choice, and text to print in error case."""
  # Infinite loop until they choose an option.
  while True:
    # Try to turn their input choice into a string.
    try:
      choice = int(input("\n>>> "))
      # If their choice is within the boundaries, return their choice and end function.
      if min <= choice <= max:
        return choice
      # If it isn't, print the error text.
      print(error_text)
    # If it can't convert, print the error text and make them choose again. 
    except ValueError:
      print(error_text)

# Main menu function to display the main menu, and get the user's choice.
def main_menu():
  """This function displays the main menu and gets the user's choice."""
  # \n and \t for formatting and to make it look nice.
  print("\nWhat would you like to do?\n")
  print("\t1. Begin an order (enter 1)")
  print("\t2. Management summary (enter 2)")
  print("\t3. View orders (enter 3)")
  print("\t4. End session (enter 4)")
  # Uses the user_choice function to get the user's choice.
  return user_choice(1, 4, "\nSorry, that isn't an option, please try again.")

# Function to create a customer's order. 
def create_order(order_type):
  """This function creates creates an order in the orders dictionary.
  Gets the customers name, how many pizzas they want and details if necessary. 
  Argument is whether the order is for delivery or for pickup."""
  # Gets the customers name and removes trailing spaces. 
  customer_name = input("\nWhat is the customer's name?\n\n>>> ").strip()
  # If their order is for pickup.
  if order_type == 1:
    # Creates the customer's order in the orders dictionary with their name.
    orders[customer_name] = {}
    # Adds the customer's details to the details dictionary, but as it is for pickup
    # it only adds the type of order. 
    details[customer_name] = [1]
  # If their order is for delivery.
  elif order_type == 2:
    # Gets the customer's address and removes trailing spaces. 
    customer_address = input("\nWhat is the customer's address?\n\n>>> ").strip()
    # Gets the customer's phone number and removes trailing spaces. 
    customer_number = input("\nWhat is the customer's phone number?\n\n>>> ").strip()
    # Creates the customer's order in the order dictionary with their name. 
    orders[customer_name] = {}
    # Adds the customer's details to the details dictionary.
    details[customer_name] = [2, customer_address, customer_number]
  # Gets how many pizzas the customer would like
  print("\nHow many pizzas would the customer like?")
  pizza_amount = user_choice(1, 5, 
  "\nSorry, there's a max of 5 pizzas per customer, please try again.")
  # Returns the customer's name and the amount of pizzas they want.
  return customer_name, pizza_amount

# Function to build the customer's order.
def order_menu(pizza_amount, customer_name):
  """This function lets the user add pizzas to an order and finish the order.
  Arguments are the amount of pizzas the customer wants and their name."""
  # Infinite loop until the order is finished or cancelled.
  while True:
    print("\n\t1. Choose pizza to add (enter 1)")
    print("\t2. View current order (enter 2)")
    print("\t3. Finish order (enter 3)")
    print("\t4. Cancel order (enter 4)")
    # Gets the user's choice of what to do
    order_menu_choice = user_choice(1, 4, 
    "\nSorry, that isn't an option, please try again.")
    # If they choose to add a pizza to the order.
    if order_menu_choice == 1:
      # If the amount of pizzas the customer has left is greater than 0.
      if pizza_amount > 0:
        # Index variable.
        i = 1
        # Line for formatting.
        print()
        # For each pizza in the pizzas dictionary (displays avaliable pizzas).
        for pizza, price in pizzas.items():
          # Prints them like so:
          #   1. Cheese, $8.50 (enter 1)
          # The .format is (index, pizza name, pizza price, index).
          print("\t{}. {}, ${:.2f} (enter {})".format(i, pizza, price, i))
          # Increments index.
          i += 1
        # Prints the option to cancel adding a pizza.
        print("\t{}. Cancel (enter {})".format(i, i))
        # Gets the customer's choice of pizza to add. 
        pizza_choice = user_choice(1, i, 
        "\nSorry, that isn't an option, please try again.\n")
        # If their choice isn't to cancel adding a pizza.
        if pizza_choice < i:
          # Gets how many of the specified pizza the customer would like.
          # Converts the pizzas dictionary to a list and grabs the name of the specified
          # pizza. - 1 is because lists start at 0 but the user input starts at 1.
          print("\nHow many {} pizzas would the customer like?"
                .format(list(pizzas)[pizza_choice - 1]))
          chosen_pizza_amount = user_choice(1, pizza_amount, 
          "\nSorry, the customer can only add {} more pizzas.".format(pizza_amount))
          # If their order already contains the chosen pizza.
          if list(pizzas)[pizza_choice - 1] in orders[customer_name]:
            # Adds their chosen pizza amount to the already existing pizza in the order.
            orders[customer_name][list(pizzas)[pizza_choice - 1]] += chosen_pizza_amount
          # If their order doesn't already contain the chosen pizza. 
          else:
            # Adds their chosen pizza to the their dictionary.
            # Again, converts the pizzas dictionary to a list, - 1
            # to grab the pizza name.
            orders[customer_name][list(pizzas)[pizza_choice - 1]] = chosen_pizza_amount
          # Subtracts the chosen pizza amount from the customers total amount of pizzas.
          pizza_amount -= chosen_pizza_amount
        # If they choose to cancel the order, it doesn't need an else, just loops back. 
      # If the customer reached their max pizzas. 
      else:
        print("\nSorry, the customer can't add any more pizzas.")
    # If they choose to view the current order. 
    elif order_menu_choice == 2:
      # Infinite loop until they return to the previous menu.
      while True:
        # Index variable.
        i = 1
        # Total order price variable.
        order_price = 0 
        # Line for formatting.
        print()
        # For each pizza and amount in the customer's order.
        for pizza, amount in orders[customer_name].items():
          # Prints the pizza, the quantity and the price, like so:
          #   1. Cheese, $8.50 x 5 - $42.50 (enter 1 to remove)
          # (index, pizza_name, pizza_price, pizza_amount, pizza_amount * price, index).
          print("\t{}. {}, ${:.2f} x {} - ${:.2f} (enter {} to remove)"
          .format(i, pizza, pizzas[pizza], amount, pizzas[pizza] * amount, i))
          # Adds the pizza amount x the pizza price to the total order price.
          order_price += pizzas[pizza] * amount
          # Increments index. 
          i += 1
        # If the order is for delivery.
        if details[customer_name] == 2:
          # Prints the delivery charge.
          print("\t{}. Delivery charge - $2.50".format(i))
          # Adds delivery charge to the total order price. 
          order_price += 2.5
          i += 1
        # Prints the total price of the order. 
        print("\t{}. Total - ${:.2f}".format(i, order_price))
        # Prints the return option.
        print("\t{}. Return (enter {})".format(i + 1, i + 1))
        # Gets the users choice
        current_order_choice = user_choice(1, len(orders[customer_name]) + 2, 
                     "\nSorry, that isn't an option, please try again.")
        # If the user's choice was to return to the previous menu.
        # len(orders[customer_name] + 2) is the second option after all the pizzas.
        if current_order_choice == len(orders[customer_name]) + 2:
          break
        # If the user chose the total price or delivery charge (not an option).
        elif (current_order_choice == len(orders[customer_name]) + 1 or 
              current_order_choice == len(orders[customer_name]) + 2):
          print("\nSorry, that isn't an option, please try again.")
        # If the user chose to remove a pizza from the list.
        else:
          # Adds back pizzas to their amount left.
          # the_customers_order[amount_of_specified pizza]
          pizza_amount += orders[customer_name][list(pizzas)[current_order_choice - 1]]
          # Removes the pizza from the order.
          # - 1 because lists start at 0 while the choices don't.
          orders[customer_name].pop(list(pizzas)[current_order_choice - 1])
    # If they choose to finish the order. 
    elif order_menu_choice == 3:
      # Confirm to finish order variable.
      finish = 1
      # Total order price variable.
      order_price = 0
      # If the customer still has pizzas left to order.
      if pizza_amount > 0:
        print("\nThe customer has not ordered all his pizzas.")
        print("Are you sure you want to finish the order?")
        print("\n\t1. Yes (enter 1)\n\t2. No (enter 2)")
        # Sets the finish order variable to 1 (finish) or 2 (cancel).
        finish = user_choice(1, 2, "\nSorry, that isn't an option, please try again.")
      # If finish order variable is 1 (finish).
      if finish == 1:
        # If the type of order is pickup.
        if details[customer_name][0] == 1:
          # Prints the customer's name.
          print("\n{}, pickup".format(customer_name.capitalize()))
        # If the type of order is delivery.
        else:
          # Prints the customer's name, address and phone number. 
          print("\n{}, delivery".format(customer_name.capitalize()))
          print("{}, {}".format(details[customer_name][1], details[customer_name][2]))
        # Index variable.
        i = 1
        # For each pizza and amount in the customer's order. 
        for pizza, amount in orders[customer_name].items():
          # Prints the pizza, price and quantity like so:
          # 1. Cheese, $8.50 x 2 - $17.00
          # (index, pizza_name, pizza_price, pizza_amount, pizza_price x amount).
          print("\t{}. {}, ${:.2f} x {} - ${:.2f}"
          .format(i, pizza, pizzas[pizza], amount, pizzas[pizza] * amount))
          # Increments index variable.
          i += 1
          # Adds pizza_price x amount to the total order price.
          order_price += pizzas[pizza] * amount
        # If the order is for delivery.
        if details[customer_name] == 2:
          # Prints the delivery charge.
          print("\t{}. Delivery charge - $2.50".format(i))
          # Adds delivery charge to the total order price. 
          order_price += 2.5
          i += 1
        # Prints the total price of the order.
        print("\t{}. Total - ${:.2f}".format(i, order_price))
        print("\t{}. Finish and add order (enter {})".format(i + 1, i + 1))
        print("\t{}. Return (enter {})".format(i + 2, i + 2))
        # Gets user's choice of cancel or finish.
        current_order_decision = user_choice(i, i + 2, 
                                "\nSorry, that isn't an option, please try again.")
        # If their choice is to finish order, break the loop. 
        if current_order_decision == i + 1:
          for pizza, amount in orders[customer_name].items():
            # Adds the amount of specified pizza in the order to the total pizzas sold.
            pizzas_sold[pizza] += amount
          break
        # Don't need to handle return option, just loops back.
    # If the user chooses to cancel the order.
    else:
      print("\nAre you sure you want to cancel the order?")
      print("\n\t1. Yes (enter 1)\n\t2. No (enter 2)")
      # Gets confirmation.
      cancel = user_choice(1, 2, "\nSorry, that isn't an option, please try again.")
      # If they confirm to cancel.
      if cancel == 1:
        # Remove the customer's order from the orders dictionary.
        orders.pop(customer_name)
        break

# Function to view every order.
def view_orders():
  """This function displays every order in the orders dictionary."""
  # For every customer and their order in the orders dictionary.
  for name, order in orders.items():
    # Index variable.
    i = 1
    # Set the total order price to 0.
    order_price = 0
    # If the order is for pickup.
    # Prints name like so: 
    # Dave - Pickup
    if details[name][0] == 1:
      print()
      print("{} - Pickup".format(name.capitalize()))
    # If the order is for delivery.
    # Prints name and details like so:
    # Dave - Delivery
    # 1 Fungus Avenue, 123456789
    else:
      print()
      print("{} - Delivery".format(name.capitalize()))
      # Grabs the customer's details.
      print("{}, {}".format(details[name][1], details[name][2]))
    # For every pizza and amount in their order.
    for pizza, amount in order.items():
      # Print the pizza, amount, and total price like so:
      # 1. Cheese x 5 - $42.50
      # (index, pizza_name, pizza_price, pizza_amount, pizza_price x pizza_amount).
      print("\t{}. {}, ${:.2f} x {} - ${:.2f}"
      .format(i, pizza, pizzas[pizza], amount, pizzas[pizza] * amount))
      # Adds pizza_price x pizza_amount to the total order price.
      order_price += pizzas[pizza] * amount
      # Increments index.
      i += 1
    # Prints total order price.
    print("\t{}. Total - ${:.2f}".format(i, order_price))

# Function to provide the amount of pizzas sold and profit made.
def management_summary():
  """This function displays a management summary. 
  This includes the total pizzas sold, and profit made."""
  # Formatting print statement.
  print()
  # Index variable.
  i = 1
  # Regular pizzas sold.
  regular_sold = 0
  # Gourmet pizzas sold.
  gourmet_sold = 0
  # For every pizza and their amount in the total pizzas sold dictionary.
  for pizza, quantity in pizzas_sold.items():
    # Prints the pizza, price and amount like so:
    # 1. Cheese, $8.50 x 5 - $42.50
    # (index, pizza_name, pizza_price, pizza_amount, price x amount).
    print("\t{}. {}, ${:.2f} x {} - ${:.2f}"
          .format(i, pizza, pizzas[pizza], quantity, pizzas[pizza] * quantity))
    # Increment index.
    i += 1
    # If the price of the specified pizza is $8.50.
    if pizzas[pizza] == 8.50:
      # It is a regular pizza so add the amount of them to the regular sold variable.
      regular_sold += quantity
    # If the price isn't $8.50.
    else:
      # It is a gourmet pizza so add the amount of them to the gourmet sold variable.
      gourmet_sold += quantity
  # Prints the total amount of regular pizzas sold and the total price.
  print("\t{}. Total regular x {} - ${:.2f}"
        .format(i, regular_sold, 8.50 * regular_sold))
  # Prints the total amount of gourmet pizzas sold and the total price. 
  print("\t{}. Total gourmet x {} - ${:.2f}"
        .format(i + 1, gourmet_sold, 13.50 * gourmet_sold))
  # Prints the total amount of pizzas sold and the total price. 
  print("\t{}. Total {} pizzas sold - ${:.2f}"
        .format(i + 2, regular_sold + gourmet_sold, 
                (8.50 * regular_sold) + (13.50 * gourmet_sold)))

print("Welcome to the Crusty Pizzas' Pizza Program!")

# Main loop.
while True:
  # Runs the main menu function and stores the result.
  main_choice = main_menu()
  # If the result was 1 (begin an order).
  if main_choice == 1:
    # Asks the user to enter the type of the customer's order.
    print("\n\t1. Pickup (enter 1)")
    print("\t2. Delivery (enter 2)")
    print("\t3. Cancel (enter 3)")
    order_type = user_choice(1, 3, "\nSorry, that isn't an option, please try again.")
    # If they don't choose to cancel. 
    if order_type != 3:
      # Runs the create order function with the order type and stores the results.
      current_order_name, current_order_amount = create_order(order_type)
      # Runs the order menu function with the current orders pizza amount and name. 
      order_menu(current_order_amount, current_order_name)
  # If the result was 2 (management summary).
  elif main_choice == 2:
    # Runs the management summary function. 
    management_summary()
  # If the result was 3 (view orders).
  elif main_choice == 3:
    # Runs the view orders function.
    view_orders()
  # If the result was 4 (end session).
  else:
    print("\nThanks for using the Crusty Pizzas' Pizza Program!")
    break