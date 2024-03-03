n = int(input("Enter the number of words"))
words = [input("Enter word") for i in range(n)]
result = " ".join(words)
print(result)