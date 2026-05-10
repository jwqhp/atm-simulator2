def get_cash(balance):
    g_c = int(input())
    if balance - g_c >= 0:
        balance -= g_c
        print("Снято с баланса ", g_c)
    else:
        print("Недостаточно средств")
    return balance

def main():
    balance = 0
    while True:
        print("\n1.Баланс\n2.Снять\n3.Внести\n4.История операций\n5.Выход")
        choice = int(input())
        if choice == 1:
            print("Текущий баланс: ", balance)
        elif choice == 2:
            get_cash(balance)
        elif choice == 3:
            
        elif choice == 4:
            
        elif choice == 5:
            break
        else:
            print("Такой функции не существует")