def get_cash(balance):
    g_c = int(input("Введите сумму: "))
    
    if g_c <= 0:
        print("Сумма должна быть больше нуля")
        return balance
    elif balance - g_c >= 0:
        balance -= g_c
        print(f"Снято с баланса: {g_c}")
    else:
        print("Недостаточно средств")
        
    return balance


def deposit(balance):
    dep = int(input("Введите сумму: "))
    
    if dep <= 0:
        print("Сумма должна быть больше нуля")
        return balance   
    else:
        balance += dep
        print(f"Баланс пополнен на {dep}")    
    return balance


def main():
    balance = 0
    while True:
        print("\n1.Баланс\n2.Снять\n3.Внести\n4.История операций\n5.Выход")
        choice = int(input("Выберите действие: "))
        if choice == 1:
            print("Текущий баланс: ", balance)
        elif choice == 2:
            balance = get_cash(balance)
        elif choice == 3:
            balance = deposit(balance)
        elif choice == 4:
            print("в разработке")
        elif choice == 5:
            break
        else:
            print("Такой функции не существует")
    
if __name__ == "__main__":
    main()                  