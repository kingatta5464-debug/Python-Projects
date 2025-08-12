with open("story.txt", "r") as file:
    story = file.read()

start_of_word = -1

words = set()

for i, char in enumerate(story):
    if char == "<":
        start_of_word = i
    if char == ">":
        word = story[start_of_word : i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input(f"Enter a word for {word} : ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)
