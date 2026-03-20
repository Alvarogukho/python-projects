import json
try:
    contacts = json.load(open("contacts.json", "r"))
except:
    contacts = []

def add():
    contacts.append({"names":name,"number":number})

def save():
    json.dump(contacts, open("contacts.json", "w"))

while True:
    name_found = False
    menu = str(input("add/remove/find/quit : "))
    if menu == "add":
        name = str(input("Insert Name : "))
        number = str(input("Insert Number : "))
        add()
        save()
    elif menu == "find":
        find_name = str(input("Find Name : "))
        for i in contacts:
            if i["names"] == find_name:
                print(i["number"])
                name_found = True
        if name_found == False:
            print("Name is not found")
    elif menu == "remove":
        remove_name = str(input("Remove Name : "))
        for i, v in enumerate(contacts):
            if v["names"] == remove_name:
                contacts.pop(i)
                name_found = True
        if name_found == False:
            print("Name is not found")
        save()
    elif menu == "quit":
        break
    else:
        print("...")



