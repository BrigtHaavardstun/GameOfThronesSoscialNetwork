from CSV_toMatrix import CSV_Reader

FILENAME = "AllNames.csv"
SAVEFILENAME = "SaveFile.csv"
MATRIX = CSV_Reader(FILENAME)


def  setConnectionValue(id1, id2, value):
    global MATRIX
    MATRIX.set_value(id1,id2,value)


def is_new_name(name):
    global MATRIX
    return name not in MATRIX.get_labels()


def validate_input(firstName,secondName):
    global MATRIX
    firstID = MATRIX.label_to_id(firstName)
    secondID = MATRIX.label_to_id(secondName)
    ans = input(f"Are you sure you want to connect {firstName} and {secondName}? Current connection score: {MATRIX.get_cell_value(firstID, secondID)}. 'Y' for yes")
    if ans.lower().startswith("y"):
        return True

    else:
        print(f"Read {ans} as 'No'")
        return False




def _confirm_new_name(name):
    print(f"\n{name} don't exist in the matrix")
    ans = input(f"Do you want to add {name} to your matrix? (Y for yes)")
    if ans.lower().startswith("y"):
        MATRIX.add_new_label(name)
        return True
    else:
        return False


def new_connection():
    nameOfFirstPerson = input("Give me name of first person: ")
    if is_new_name(nameOfFirstPerson):
        if _confirm_new_name(nameOfFirstPerson):
            pass
        else:
            print(f"Aborting connection persons, since you don't want to add {nameOfFirstPerson}...")
            return
    nameOfSecondPerson = input("Give me name of second person: ")
    if is_new_name(nameOfSecondPerson):
        if _confirm_new_name(nameOfSecondPerson):
            pass
        else:
            print(f"Aborting connection persons, since you don't want to add {nameOfSecondPerson}...")
            return

    if validate_input(nameOfFirstPerson, nameOfSecondPerson):
        id1 = MATRIX.label_to_id(nameOfFirstPerson)
        id2 = MATRIX.label_to_id(nameOfSecondPerson)
        print(f"\nIncrementing connection between {nameOfFirstPerson} and {nameOfSecondPerson}...")
        MATRIX.increment_edge(id1,id2)
        print(f"Current connection is now {MATRIX.get_cell_value(id1,id2)}\n")
    else:
        print("'No'. Aborting connection...")

def display():
    MATRIX.display_matrix()

def save():
    print(f"Saving data to {SAVEFILENAME}...")
    MATRIX.save_to_file(SAVEFILENAME)
    print(f"Completed saving data.")


if __name__ == '__main__':

    print("Starting Game Of Thrones registration app")
    print("\nDone with setup!")
    print("Current matrix:")
    MATRIX.display_matrix()

    stopSymbol = "end"
    finished = False
    while True:
        print("\n------------------------------\nReady to take new commands!")
        ans = input("What do you want to do? (nc-new connection, s-save, q-quit, d-display): ")
        if ans.lower() == "nc":
            new_connection()
            save()
        elif ans.lower() == "s":
            save()
        elif ans.lower() == "q":
            break
        elif ans.lower() == "d":
            display()




