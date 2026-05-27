import tkinter as tk
from tkinter import messagebox, simpledialog

balance = 666
history = []

def update_ui():
    """Обновляет отображение баланса и истории на главном экране"""
    label_balance.config(text=f"Текущий баланс: {balance} руб.")
    
    # Обновляем список истории операций
    listbox_history.delete(0, tk.END)
    for record in reversed(history):
        listbox_history.insert(tk.END, record)

def get_cash():
    """Функция снятия наличных"""
    global balance
    # Всплывающее окно для ввода суммы
    amount_str = simpledialog.askstring("Снять наличные", "Введите сумму:")
    
    if amount_str is None:
        return
        
    try:
        g_c = int(amount_str)
        if g_c <= 0:
            messagebox.showerror("Ошибка", "Сумма должна быть больше нуля")
        elif balance - g_c >= 0:
            balance -= g_c
            history.append(f"Снято: -{g_c} руб.")
            messagebox.showinfo("Успех", f"Снято с баланса: {g_c} руб.")
            update_ui()
        else:
            messagebox.showerror("Ошибка", "Недостаточно средств")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректную сумму")

def deposit():
    """Функция пополнения баланса"""
    global balance
    amount_str = simpledialog.askstring("Пополнить баланс", "Введите сумму:")
    
    if amount_str is None:
        return
        
    try:
        dep = int(amount_str)
        if dep <= 0:
            messagebox.showerror("Ошибка", "Сумма должна быть больше нуля")
        else:
            balance += dep
            history.append(f"Пополнение: +{dep} руб.")
            messagebox.showinfo("Успех", f"Баланс пополнен на {dep} руб.")
            update_ui()
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректную сумму")

#Главное окно
root = tk.Tk()
root.title("Umbrella Bank")
root.geometry("500x800")
root.configure(bg="#000000")

#Лого
img_logo = tk.PhotoImage(file="Logo_ATM.png")
img_logo = img_logo.subsample(3, 3)
label_logo = tk.Label(root, image=img_logo, bg="#000000", bd=0)
label_logo.pack(pady=10)

# Заголовок и баланс
label_title = tk.Label(root, text="Под нашим зонтом безопасно", font=("Consolas", 16, "italic"), bg="#000000", fg="#ffffff")
label_title.pack(pady=10)

label_balance = tk.Label(root, text=f"Текущий баланс: {balance} руб.", font=("Consolas", 14, "bold"), bg="#000000", fg="#ffffff")
label_balance.pack(pady=5)

#Контейнер
frame_buttons = tk.Frame(root, bg="#000000")
frame_buttons.pack(pady=15)

# Кнопки действий
btn_deposit = tk.Button(frame_buttons, text="Внести средства", font=("Arial", 11), width=18, bg="#4caf50", fg="white", command=deposit)
btn_deposit.grid(row=0, column=0, padx=5, pady=5)

btn_get_cash = tk.Button(frame_buttons, text="Снять наличные", font=("Arial", 11), width=18, bg="#f44336", fg="white", command=get_cash)
btn_get_cash.grid(row=0, column=1, padx=5, pady=5)

#Истории операций
label_hist_title = tk.Label(root, text="История операций:", font=("Consolas", 10), bg="#000000", fg="#FFFFFF")
label_hist_title.pack(pady=(0, 5))

listbox_history = tk.Listbox(root, font=("Arial", 10), width=45, height=8, bg="#1a1a1a", fg="#FFFFFF", bd=1, relief="solid", highlightbackground="#333333")
listbox_history.pack(pady=5)

# Кнопка выхода
btn_exit = tk.Button(root, text="Выход", font=("Arial", 11), width=15, bg="#f44336", fg="white", command=root.quit)
btn_exit.pack(pady=15)

update_ui()
root.mainloop()