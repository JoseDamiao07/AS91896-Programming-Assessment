print("What type of order is this?\n")
print("\t1. Pick up (enter 1)")
print("\t2. Delivery (enter 2)")
while True:
  try:
    order_type = int(input("\n>>> "))
    if order_type != 1 and order_type != 2:
      print("Sorry, please type either 1 or 2.")
    else:
      break
  except ValueError:
    print("Sorry, please type either 1 or 2.")