dict_items = {
    "name": ["milk", "sugar", "flour", "coffee"],
    "quanitity": ["120", "1000", "12000", "30"],
    "unit": ["l", "kg", "kg", "kg"],
    "unit_price": ['2.3', '3', '1.2', '40']
}

action_item = str()


def get_items():

    print("Name\tQuantity\tUnit\tUnit Price (PLN)")

    for n, q, u, up in dict_items.values():
        print(f"{n} \t {q} \t {u} \t  {up}")


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


if __name__ == "__main__":

    get_items()

    while action_item.lower() != exit:
        action_item = str(input("What would you like to do? "))
        if action_item == "exit":
            print("Exiting... Bye")
            exit()
        elif action_item == "show":
            get_items()
        elif action_item == "add":
            add_item()