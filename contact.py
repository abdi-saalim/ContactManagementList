#Contact Management List: Collect User's Name, Age, & Email and store it 
#for loop: for i in range(1,11,2)-> starts at 1, ends at 10, goes in increments of 2
#lists = numbers.append() -> adds number to end of list; numbers.pop(2) removes element from list

import  json

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    
    #dictionary
    person = { "name": name, "age": age, "email": email}
    return person


def delete_person(people):
    display_people(people)
    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range.")
            else: 
                break
        except:
            print("Invalid number")
    people.pop(number -1)
    print("Person deleted!")

def search(people):
    search_name = input("Search for a name: ")
    result = []
    
    for person in people:
        name = person["name"]
        if search_name in name.lower():
            result.append(person)
    display_people(result)

def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])


print("Hi, welcome to the Contact Management System.")
print()

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print()
    print ("Contact list size:", len(people))
    command = input("You can 'Add', 'Delete' or 'Search' or 'Q' for quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added!")
    elif command == "delete":
        delete_person(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else: 
        print("Invalid command.")

with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)

print(people)