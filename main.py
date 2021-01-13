action_item = str()


if __name__ == "__main__":

    while action_item != exit:
        action_item = str(input("What would you like to do?"))
        if action_item == "exit":
            print("Exiting... Bye")
            exit()
        