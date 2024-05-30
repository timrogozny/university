import json

def first():
    with open("products.json", "r", encoding="utf8") as f:
        text = json.load(f)
    print(text)

    for product in text['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии!")
        else:
            print("Нет в наличии!")


def second():

    with open("products.json", "r", encoding="utf8") as f:
        text = json.load(f)

    newproduct = {}
    newproduct['name] = input("Введите название: ")
    newproduct['price'] = float(input("Введите цену: "))
    newproduct['weight'] = input("Введите вес: ")
    newproduct['available'] = input("Есть ли в наличии? ")

    text['products'].append(newproduct)

    with open('products.json', 'w', encoding="utf8") as f:
        json.dump(text, f)

    for product in text['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии!")
        else:
            print("Нет в наличии!")
    print(text)






def third():

    ru_en_dict = {}

    with open("en-ru.txt", 'r', encoding='utf-8') as file:

        for line in file:
            en, rutrans = line.strip().split(' - ', 1)
            rus = [t.strip() for t in rutrans.split(',')]
            for ru in rus:
                if ru not in ru_en_dict:
                    ru_en_dict[ru] = []
                ru_en_dict[ru].append(en)

    with open("ru-en.txt", 'w', encoding='utf-8') as file:
        for ru in sorted(ru_en_dict):
            entrans = ', '.join(sorted(ru_en_dict[ru]))
            file.write(f"{ru} - {entrans}\n")


third()