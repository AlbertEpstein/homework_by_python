import tkinter as tk
from tkinter import messagebox

def send():
    name = entry_name.get()
    age = entry_age.get()
    gender = choice.get()

    if name == "" or not age.isdigit():
        messagebox.showerror("Ошибка")
    else:
        result.config(text=f"{name}, {age} лет, {gender}")
        messagebox.showinfo("Готово")

window = tk.Tk()
window.title("Анкета")
window.geometry("567x765")

tk.Label(window, text="Ваше имя:").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Ваш возраст:").pack()
entry_age = tk.Entry(window)
entry_age.pack()

tk.Label(window, text="Ваш пол:").pack()

choice = tk.StringVar(value="Мужской")

tk.Radiobutton(window, text="Мужской",
               variable=choice, value="Мужской").pack()

tk.Radiobutton(window, text="Женский",
               variable=choice, value="Женский").pack()

tk.Button(window, text="Отправить", command=send).pack(pady=10)

result = tk.Label(window, text="Результат:")
result.pack()

window.mainloop()