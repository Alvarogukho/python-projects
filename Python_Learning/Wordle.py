word = "llama"

while True:

    word_count = {}
    yellow_used = {}
    counter = 0
    result = []

    guess = str(input("Guess The Word : "))
    if guess == word:
        print("You got it right")
        break
    for char in guess: 
        word_count[char] = word.count(char)

    for char in guess: 
        if char in word:
            if char == word[counter]:
                result.append('[Green]')
                if char not in yellow_used:
                    yellow_used[char] = 0
                yellow_used[char] += 1
            else:
                if yellow_used.get(char, 0) < word_count[char]:
                    result.append('[Yellow]')
                    if char not in yellow_used:
                        yellow_used[char] = 0
                    yellow_used[char] += 1
                else:
                    result.append('[Grey]')
        else:
            result.append('[Grey]')
        counter = counter+1
        print(word_count)

    print(result)

