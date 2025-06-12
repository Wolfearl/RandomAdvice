from tkinter import Tk, ttk, StringVar, Text
from tkinter.messagebox import showinfo
from random import randint
import csv


# -------------------------------Уничтожение frame
def back_to_start(frame):
    frame.destroy()

# -------------------------------Frame с рандомным советом (из файла advices.csv)
def get_advice():
    with open("./files/advices.csv", "r", encoding="utf-8") as file:
        reader = list(csv.reader(file))
        n = len(reader)
        first_random_row = reader[randint(0, n - 1)][0] # Выбираем рандомно совет из файла в виде 'совет;иконка'
        random_row = first_random_row.split(';') # Получение массива [Совет, иконка]
        advice.set(random_row[0])

        # Если иконка не задана, открываем стандартную
        if len(random_row) == 2:
           emoji.set(random_row[1])
        else:
            emoji.set('🏕')

        frame2 = ttk.Frame(style="My.TFrame")
        frame2.place(relx=0.5, relwidth=0.98, rely=0.5, relheight=0.98, anchor='center')

        frame2.rowconfigure(index=0, weight=1)
        frame2.rowconfigure(index=1, weight=2)
        frame2.rowconfigure(index=2, weight=1)
        frame2.columnconfigure(index=0, weight=1)

        label1 = ttk.Label(frame2, textvariable=advice, style='My.TLabel', wraplength=300, justify='center')
        label1.grid(row=0, column=0, sticky="s")

        label2 = ttk.Label(frame2, textvariable=emoji, style='Icon.TLabel')
        label2.grid(row=1, column=0, sticky="n")

        button = ttk.Button(frame2, text='Назад', style='My.TButton', command=lambda f=frame2: back_to_start(f))
        button.grid(row=2, column=0, sticky="nsew")


# Добавление совета в csv файл
def in_csv(w, f):
    w = w.get("1.0", "end-1c") # Читаем введеный текст
    if w:
        with open("./files/advices.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            if not new_emoji.get():
                writer.writerow([w, '🏕']) # Если не введена иконка, добавляем стандартную
            else:
                writer.writerow([w, new_emoji.get()])
            showinfo("Добавление", "Операция проведена успешно!")
            back_to_start(f)


# Окно "Добавление совета"
def add_advice():
    frame3 = ttk.Frame(style='My.TFrame')
    frame3.place(relx=0.5, relwidth=0.98, rely=0.5, relheight=0.98, anchor='center')

    frame3.rowconfigure(index=0, weight=3)
    frame3.rowconfigure(index=1, weight=2)
    frame3.rowconfigure(index=2, weight=1)
    frame3.rowconfigure(index=3, weight=1)
    for c in range(2): frame3.columnconfigure(index=c, weight=1)

    label_frame3_1 = ttk.Label(frame3, text="Совет", style='My.TLabel', anchor='center')
    label_frame3_1.grid(row=0, column=0, sticky="s")

    label_frame3_2 = ttk.Label(frame3, text="Иконка", style='My.TLabel', anchor='center')
    label_frame3_2.grid(row=0, column=1, sticky="s")

    # Поле для ввода текста совета
    text_widget = Text(frame3, width=22, height=3, background="#ffffff", foreground="#1e3a71", font=("Arial", 12, "bold"))
    text_widget.grid(row=1, column=0, sticky='nsew', padx=7, pady=20, ipady=50)

    #Поле для ввода иконки
    entry1 = ttk.Entry(frame3, textvariable=new_emoji, style='My.TEntry', font=("Arial", 12, "bold"), validate='key',
                       validatecommand=vcmd) # Ставим ограничение на ввод (1 символ)
    entry1.grid(row=1, column=1, sticky='nsew', padx=7, pady=20, ipady=50)

    button_frame3_1 = ttk.Button(frame3, text = "Добавить", style='My.TButton',
                                 command=lambda w=text_widget, f=frame3: in_csv(w, f))
    button_frame3_1.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=3, pady=1)

    button_frame3_2 = ttk.Button(frame3, text="Назад", style='My.TButton', command=lambda f=frame3: back_to_start(f))
    button_frame3_2.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=3, pady=1)

# Можно ввести не больше 1 символа
def validate(new_value):
    return len(new_value) <= 1


# -------------------------------Основное окно
root = Tk()
root.geometry("400x500+600+150")
root.title("Совет для тебя")
root.config(bg="#010828")
root.resizable(False, False)

# -------------------------------Стили
style = ttk.Style()
style.theme_use('clam')
style.configure('My.TFrame', background="#031742", relief='ridge')
style.configure('My.TButton', background='#f6593e', foreground="white",relief='solid', font=("Arial", 16, "bold"))
style.map("My.TButton", foreground=[('active', 'white')], background=[('active', '#e24a30')])
style.configure('My.TLabel', background='#031742', font=("Arial", 20, "bold"), foreground="white", anchor='center')
style.configure('Icon.TLabel', background='#031742', font=("Arial", 50), foreground="white",
                anchor='center', justify='center')
style.configure('My.TEntry', fieldbackground="#ffffff", foreground="#1e3a71")

# -------------------------------Переменные
advice = StringVar()
emoji =  StringVar()
new_emoji = StringVar()

# -------------------------------Первый frame
frame1 = ttk.Frame(style="My.TFrame")
frame1.place(relx=0.5, relwidth=0.98, rely=0.5, relheight=0.98, anchor='center')

frame1.rowconfigure(index=0, weight=10)
frame1.rowconfigure(index=1, weight=1)
frame1.rowconfigure(index=2, weight=1)
frame1.columnconfigure(index=0, weight=1)

label_frame1 = ttk.Label(frame1, text='🪂', style='Icon.TLabel', anchor='center', font=("Arial", 250))
label_frame1.grid(row=0, column=0, sticky="nsew")

button1 = ttk.Button(frame1, text="Получить совет", style="My.TButton", command=get_advice)
button1.grid(row=1, column=0, sticky="nsew", padx=3, pady=1)

button2 = ttk.Button(frame1, text="Добавить совет", style="My.TButton", command = add_advice)
button2.grid(row=2, column=0, sticky="nsew", padx=3, pady=1)

# Проверка количества введенных симолов
vcmd = (root.register(validate), '%P')


root.mainloop()