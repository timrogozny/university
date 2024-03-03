words =[]
while True:
    word = input("enter word")
    if word == "stop":
        break
    words.append(word)
e= " ".join(words)
print(e)
