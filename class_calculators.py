class Calculators:
    def calculator_basic(self):
        
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
                            print("на ноль делить нельзя")
                            return not_end(result)
                else:
                        print("Неизвестное действие")
                        return not_end(result)
            else:
                    return result
                
                

        result = 0
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
              
                return  "на ноль делить нельзя"
        else:
            result = "Неизвестное действие"
        
        return result




    def calculator_bench_press(self):
        print ("Введите сколько кг вы смогли пожать и на сколько повторений")
        
        weight, repetitions = int(input()), int(input())
        weight += 20    
        print ("Считая вес штанги базово 20 кг ваш результат")
        print("По какой формуле посчитать ваш максимально перспективно возможный вес жим лёжа?", "1:Формула Эпли", "2:Формула Бржицки", "3: Формула Лендера", sep = " \n " )
        form =  input()
        if form == "1":
               return weight * (1 + repetitions / 30)
               
        elif form == "2":
                return  weight * 36 / (37 - repetitions)
        elif form == "3":
                return 100 * weight / (101.3 - 2.67123 * repetitions)
        else:
            return "Такой формулы нет"
    

calc = Calculators()
answer = calc.calculator_basic()
print(answer)