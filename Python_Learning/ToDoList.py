import json
try:
    to_do_list = json.load(open("tasks.json", "r"))
except:
    to_do_list = []

task_done = 0

def finish():
    task_done = int(input("insert number of task that is done : "))
    to_do_list.pop(task_done - 1)

def view():
    for i, v in enumerate(to_do_list):    
        print(i+1,".",v)

def save():
    json.dump(to_do_list, open("tasks.json", "w"))

while True:
    menu = str(input("add/view/finish/quit"))
    if menu == "add":
        user_to_do = str(input("Make a prompt to do : "))
        to_do_list.insert(0, user_to_do)
        view()
        save()
    elif menu == "view":
        view()
    elif menu == "finish":
        view()
        finish()
        view()
        save()
    elif menu == "quit":
        break
    else:
        print(".....")