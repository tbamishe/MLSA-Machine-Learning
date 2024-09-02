
#Adding Inventory
def add_inventory():
  name = str(input("Enter Product Name: "))
  quantity = int(input("Enter Product Quantity: "))
  category = str(input("Enter Product Category: "))
  price = int(input("Enter Product Price: "))
  threshold = int(input("Enter Quantity Threshold: "))
  sales = str(input("Enter Product Sales: "))

  inventory[name] = {
    "quantity": quantity,
    "category": category,
    "price": price,
    "threshold": threshold,
    "sales": 0
  }
  Print("Product Added Successfully")

  #Remove Item
  def remove_item(inventory):
    name = str(input("Enter Product Name: "))
    if name in inventory:
      del inventory[name]
      print("Product Removed Successfully")
    else:
      print("Product Not Found")

  #Update Item
  def update_item(inventory):
    name = str(input("Enter Product Name: "))
    new_quantity = int(input("Enter New Quantity: "))
    if name in inventory:
      inventory[name]["quantity"] = new_quantity
      print("Product Updated Successfully")
    else:
      print("Product Update Failed")

    #Search Product 
    def search_product(inventory):
      name = str(input("Enter Product Name: "))
      if name in inventory:
        print("Product Found")
      else:
        print("Product Not Found")

    #Display Inventory
    def display_inventory(inventory):
      print(inventory)

    inventory = {}
    while True:
      print("1. Add Inventory")
      print("2. Remove Item")
      print("3. Update Item")
      print("4. Search Product")
      print("5. Display Inventory")

      choice = int(input("Enter Your Choice: "))
      if choice == 1:
        add_inventory()
      elif choice == 2:
        remove_item(inventory)
      elif choice == 3:
        update_item(inventory)
      elif choice == 4:
        search_product(inventory)
      elif choice == 5:
        display_inventory(inventory)
      else:
        print("Invalid Choice")
        break


      

