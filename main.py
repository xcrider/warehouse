dict_items = {
    "name": ["milk", "sugar", "flour", "coffee", "salt", "mayoneise"],
    "quantity": ["120", "1000", "12000", "30", "1", "12"],
    "unit": ["l", "kg", "kg", "kg", "kg", "kg"],
    "unit_price": ['2.3', '3', '1.2', '40', '5.50', '11']
}

action_item = str()


def get_items():

    print("Name\tQuantity\tUnit\tUnit Price (PLN)")

    for i in range(0,len(dict_items["name"])):
        print(f"{dict_items['name'][i]} \t {dict_items['quantity'][i]} \t \t {dict_items['unit'][i]} \t {dict_items['unit_price'][i]} ")

    # for i, n, q, u, up in enumerate(dict_items.values, 0()):
    #      print(f"{n[i]} \t {q[i]} \t {u[i]} \t {up[i]}")


def add_item():
    print("Adding to warehouse…")

    product_name = input("Item name: ")
    product_quantity = input("Item quantity: ")
    product_unit = input("Product unit: ")
    product_unit_price = input("Product unit price: ")

    dict_items["name"].append(product_name)
    dict_items["quanitity"].append(product_quantity)
    dict_items["unit"].append(product_unit)
    dict_items["unit_price"].append(product_unit_price)

    print("Item added!")

    # dict_items["name"].append(input("Item name: "))
    # dict_items["quantity"].append(input("Item quantity: "))
    # dict_items["unit"].append(input("Product unit: "))
    # dict_items["unit_price"].append(input("Product unit price:  "))


def sell_item(item_name, quantity):
    item_index = int()
    for i, item in enumerate(dict_items["name"]):
        if item == item_name:
            item_index = i

            if int(dict_items["quantity"][item_index]) >= item_quantity:
                dict_items["quantity"][item_index] = int(dict_items["quantity"][item_index]) - item_quantity
                print(f"Successfuly sold {item_quantity} {dict_items['unit'][item_index]} of {item_name}")
            else:
                print("Opss… we do not have enought of this for you!")
                break
        else:
            print("Opss… we do not have that product.")


if __name__ == "__main__":

    while action_item.lower() != exit:
        action_item = str(input("What would you like to do? "))
        if action_item == "exit":
            print("Exiting... Bye")
            exit()
        elif action_item == "show":
            get_items()
        elif action_item == "add":
            add_item()
        elif action_item == "sell":
            item_name = input("What product you'd like to buy? ")
            item_quantity = int(input("How much of it? "))
            sell_item(item_name, item_quantity)