print("выберите уровень : 1, 2 , 3 , 4 , 5 ")
lvl = int(input())
if lvl == 1:
    test_1 = "пРиВет МИР"
    print("этот уровень выполняет следующие действия , он преобразует строку пРиВет МИР d в зависимости от метода")
    print(f"1 : перевод в нижний регистр : {test_1.lower()}")
    print(f"2 : перевод в верхний регистр : {test_1.upper()}")
    print(f"3 : делает первую букву заглавной другие строчными : {test_1.capitalize()}")

    print(" выберите метод : 1, 2, 3")
    n = int(input())
    print ("введите строку")
    string  = input()
    if n == 1:
        string = string.lower()
        print(string)
    elif n == 2:
        string = string.upper()
        print(string)
    elif n == 3:
        string = string.capitalize()
        print(string)
elif lvl == 2:
    test_2 = "Ботать круто"
    print("тестовая строка Ботать круто")
    print(f"1:найти позицию первого вхождения слова, например слова круто в строке : Ботать круто :  {test_2.lower().count("круто") + 1}")
    print(f"заменяет слово на выбранное , допустим слово круто на плохо {test_2.replace("круто", "плохо")}")
    print(f"подсчет всех выбраных букв , например буквы о в ботать круто {test_2.count("о")}")
    print(f"4 :ищет индекс элемента, например слова круто {test_2.lower().index("круто")}")
    print(" выберите метод : 1, 2, 3, 4")
    n = int(input())
    print ("введите строку")
    string  = input()
    if n == 1:
        k = input("Выберите слово")

        string.find(k)
    elif n ==2:
        k = input("Выберите слово")
        slovo = input("Выберите на какое замерить")
        print(string.replace(k, slovo))
    elif n == 3:
        char = input("Выберите букву")
        print(string.count(char))
    else:
        slovo = input("введите слово")
        print(string.lower().index(slovo))

elif lvl == 3:
    test_3 = "Ботать очень круто"
    print("тестовая строка: Ботать очень круто")
    print(f"1: разделить строку на слова: {test_3.split()}")
    print(f"2: соединить слова через дефис: {'-'.join(test_3.split())}")

    print("выберите метод: 1, 2")
    n = int(input())
    string = input("введите строку: ")

    if n == 1:
        separator = input("введите разделитель: ")
        if separator == "":
            print(string.split())
        else:
            print(string.split(separator))

    elif n == 2:
        separator = input("чем соединить слова: ")
        print(separator.join(string.split()))
elif lvl == 4:
    
    print(f"1: только буквы: {'Привет'.isalpha()}")
    print(f"2: только цифры: {'12345'.isdigit()}")
    print(f"3: убрать пробелы по краям: |{'  Привет  '.strip()}|")
    print("4: подставить строку в шаблон: {}".format("Привет"))
    print(f"5: Cделать r строкой {'he//lo'}")
    print(f"6: Сделать l строкой, то есть на неё выделится больше бит в памяти")

    print("выберите метод: 1, 2, 3, 4, 5, 6")
    n = int(input())
    string = input("введите строку: ")

    if n == 1:
        print(string.isalpha())

    elif n == 2:
        print(string.isdigit())

    elif n == 3:
        print(string.strip())

    elif n == 4:
        temp = input("введите шаблон с {}, например Привет, {}!: ")
        print(temp.format(string))
    elif n == 5:
        print(r'string')
    elif n == 6:
        pass
