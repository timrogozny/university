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
    letter_scores = {
        "АВЕИНОРСТ": 1,
        "ДКЛМПУ": 2,
        "БГЁЬЯ": 3,
        "ЙЫ": 4,
        "ЖЗХЦЧ": 5,
        "ШЭЮ": 8,
        "ФЩЪ": 10
    }

    for letter in word.upper():
        for key in letter_scores:
            if letter in key:
                score += letter_scores[key]

    return score


word = input("Введите слово: ")
print(f"Стоймость слова '{word}' равна {word_score(word)} очков.")


