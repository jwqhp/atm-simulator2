def main():
    balance = 0
    while True:
        print("\n1.Баланс\n2.Снять\n3.Внести\n4.История операций\n5.Выход")
        choice = int(input())
        if choice == 1:
            print("Текущий баланс: ", balance)
        elif choice == 2:
            
        elif choice == 3:
            
        elif choice == 4:
            
        elif choice == 5:
            break
        else:
            print("Такой функции не существует")