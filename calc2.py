def calc():
    print ("Введите первое число")
    a = int(input())
    print ("Введите второе число")
    b = int(input())

    print("Выберите дейсвие")
    print("1: +" \
    " 2: -" \
    " 3: /" \
    " 4: *")
    operation = input()
    
    if operation == "1":
                result = a + b
    elif operation == "2":
                result = a - b
    elif operation == "4":
                result = a * b
    elif operation == "3":
        if b != 0:
            result = a / b
        else:
            result = "на ноль делить нельзя"
    else:
        result = "Неизвестное действие"
    
    return result
print(calc())

