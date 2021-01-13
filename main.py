items = {
    "name": ["milk", "sugar", "flour", "coffee"],
    "quanitity": ["120", "1000", "12000", "30"],
    "unit": ["l", "kg", "kg", "kg"],
    "unit_price": ['2.3', '3', '1.2', '40']
}

action_item = str()


def get_items():

    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    # q = items.get("quantity")
    # u = items.get("unit")
    # up = items.get("unit_price")
    # for i in items.values():
    #     obj = items.get("name")
    #     print(obj[i])
    #     print(q[i])

if __name__ == "__main__":

    get_items()

    while action_item.lower() != exit:
        action_item = str(input("What would you like to do? "))
        if action_item == "exit":
            print("Exiting... Bye")
            exit()
        elif action_item == "show":
            get_items()