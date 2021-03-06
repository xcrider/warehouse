dict_items = {
    "name": ["milk", "sugar", "flour", "coffee", "salt", "mayoneise"],
    "quantity": ["120", "1000", "12000", "30", "1", "12"],
    "unit": ["l", "kg", "kg", "kg", "kg", "kg"],
    "unit_price": ['2.3', '3', '1.2', '40', '5.50', '11']
}

action_item = str()


def show():

    '''Listing all item available in warehouse with detail informations'''

    print("Name\tQuantity\tUnit\tUnit Price (PLN)")

    for i in range(0, len(dict_items["name"])):
        print(f"{dict_items['name'][i]} \t {dict_items['quantity'][i]} \t \t {dict_items['unit'][i]} \t {dict_items['unit_price'][i]} ")

    warehouse_action()


def add():

    '''Adding item to dict_items warehouse from user input. '''

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

    # new_product = []
    # new_product.append(input("Product name: "))
    # new_product.append(input("Product quantity: "))
    # new_product.append(input("Product unit: "))
    # new_product.append(float(input("Product unit price: ")))   

    # for i, value in enumerate(dict_items.items()):
    #     dict_items.values(append(new_product[i]))


def sell():

    '''This functions takes user input data and validates it. 
    If that are valid it calls warehouse_update function'''
    
    item_name = input("What product you'd like to buy? ")
    
    try:
        i = dict_items["name"].index(item_name)
    except ValueError:
        print("Sorry we don't have this product!")
        print("Here's a list of available product!")
        show()

    item_quantity = int(input("How much of it? "))
    
    if int(dict_items['quantity'][i]) >= item_quantity:
       warehouse_update(item_name, item_quantity,i)
    else:
        print(f"Opss… we do not have enought of this for you! Maximum available is {dict_items['quantity'][i]} {dict_items['unit'][i]} of {dict_items['name'][i]}.")
        warehouse_action()

    
def warehouse_update(item_name, item_quantity, index):

    '''This function updates warehouse stock accordingly to the sale'''

    if int(dict_items['quantity'][index]) >= item_quantity:
        dict_items['quantity'][index] = int(dict_items['quantity'][index]) - item_quantity
        print(f"Successfuly sold {item_quantity} {dict_items['unit'][index]} of {item_name}.")
        print(f"There is still {dict_items['quantity'][index]} {dict_items['unit'][index]} of {item_name} in warehouse.")    

    # for i, item in enumerate(dict_items["name"]):
    #     if item == item_name:
    #         if int(dict_items["quantity"][i]) >= item_quantity:
    #             dict_items["quantity"][i] = int(dict_items["quantity"][i]) - item_quantity
    #             print(f"Successfuly sold {item_quantity} {dict_items['unit'][i]} of {item_name}.")
    #             print(f"There is still {dict_items['quantity'][i]} {dict_items['unit'][i]} of {item_name} in warehouse.")


def close():

    '''Exit program'''

    print("Exiting... Bye")
    exit


def warehouse_action():

    '''This is main program function, where user selects operation'''
    
    action_dict = {
        1: show,
        2: add,
        3: sell,
        4: close
    }
    
    [print(key, value.__name__) for key, value in action_dict.items()]

    try:
        action_type = int(input("Select the operation by providing the corresponding number: "))

        action = action_dict.get(action_type)
        action()

    except TypeError:
        print("Opps, there is no such operation. Select operation from the list.\n")
        warehouse_action()

if __name__ == "__main__":

    warehouse_action()
