import random

question_list = [
    {"question":"2+2?", "answer": "4"},
    {"question":"3+2?", "answer": "5"},
    {"question":"4+2?", "answer": "6"},
    {"question":"5+2?", "answer": "7"},
    {"question":"6+2?", "answer": "8"}
]

points = 0

while True:
    random.shuffle(question_list)
    for i in question_list :
        print(i["question"])
        ans = i["answer"]
        ask = str(input("Answer : "))
        if ask == ans:
            print("You got that right")
            points = points+1
        else:
            print("You got that wrong")
    print("Points : ", points)
    end = str(input("Type end to end session"))
    if end == "end":
        break
    else:
        points = 0
        continue