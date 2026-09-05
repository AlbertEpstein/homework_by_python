
result = 0 
def not_end(result):
    
    print("Выберите дейсвие")
    print("1: +" \
        " 2: -" \
         " 3: /" \
        " 4: *" \
        " 5 : =")
    operation = input()
    if operation != "5":
        print("Введите новое число")
    else:
        return result
    c = int(input())
    if operation != "5":
        if operation == "1":
                        result += c
                        return not_end(result)
        elif operation == "2":
                        result -= c
                        return not_end(result)
        elif operation == "4":
                        result *= c
                        return not_end(result)
        elif operation == "3":
            if c != 0:
                    result /= c
                    return not_end(result)
            else:
                    result = "на ноль делить нельзя"
        else:
                result = "Неизвестное действие"
    else:
            return result, "айдар лох"
           
           

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
                return not_end(result)
    elif operation == "2":
                result = a - b
                return not_end(result)
    elif operation == "4":
                result = a * b
                return not_end(result)
    elif operation == "3":
        if b != 0:
            result = a / b
            return not_end(result)
        else:
            result = "на ноль делить нельзя"
    else:
        result = "Неизвестное действие"
    
    return result


print(calc())