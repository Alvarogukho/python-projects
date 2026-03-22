word = "llama"

while True:
    word_count = {}
    yellow_used = {}
    result = []

    guess = str(input("Guess The Word : "))
    if guess == word:
        print("You got it right")
        break

    for char in guess:
        word_count[char] = word.count(char)

    # Pass 1: greens only
    for i in range(len(guess)):
        if guess[i] == word[i]:
            result.append('[Green]')
            yellow_used[guess[i]] = yellow_used.get(guess[i], 0) + 1
        else:
            result.append(None)

    # Pass 2: yellows and greys
    for i in range(len(guess)):
        if result[i] is not None:
            continue
        char = guess[i]
        if char in word and yellow_used.get(char, 0) < word_count[char]:
            result[i] = '[Yellow]'
            yellow_used[char] = yellow_used.get(char, 0) + 1
        else:
            result[i] = '[Grey]'

    print(result)