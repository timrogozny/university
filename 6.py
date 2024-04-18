def first():

    d = {
        "Russia": "Moscow",
        "UK": "London",
        "France": "Paris",
        "Sweden": "Stockholm",
    }


    for country, capital in d.items():
        print (country , ":" , capital)

    country = input("Enter country:")
    print ("the capital of", country, "is", d.get(country))

    sort = sorted(d.items())
    print(sort)


def word_score(word):
    score = 0
    a = {
        "АВЕИНОРСТ": 1,
        "ДКЛМПУ": 2,
        "БГЁЬЯ": 3,
        "ЙЫ": 4,
        "ЖЗХЦЧ": 5,
        "ШЭЮ": 8,
        "ФЩЪ": 10
    }

    for letter in word.upper():
        for let in a:
            if letter in let:
                score += a[let]

    return score


word = input("Enter word: ")
print("Word value", word, "is", word_score(word) )


