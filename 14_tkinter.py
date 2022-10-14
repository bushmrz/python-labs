import tkinter
import random
#1
def first_app():

    def click():
        farin = 9 / 5 * float(entry.get()) + 32
        label.config(text=str(farin))

    window = tkinter.Tk()
    label_main = tkinter.Label(window, text="Перевод градусов \n из Цельсия в Фарингейт")
    label_main.pack()
    frame = tkinter.Frame(window)
    frame.pack()
    entry = tkinter.Entry(frame)
    entry.pack()
    label = tkinter.Label(frame)
    label.pack()


    # Привязываем обработчик нажатия на кнопку к функции click()
    button = tkinter.Button(frame, text='Конвертировать', command=click)
    exit_butt = tkinter.Button(frame, text='Выход', command=exit)
    button.pack()
    exit_butt.pack()

    window.mainloop()

#first_app()

#2
def inpWord():
    global k
    var = entry.get()
    if label.cget("text") != "":
        if var.isalpha():
            if k != 0:
                if var == dictionary[rus]:
                    label.config(text="Ответ правильный!")
                    k = 3
                else:
                    label_main.config(text="У тебя есть " + str(k) + " попытки:")
                    label.config(text="Ответ неправильный!")
                    k -= 1
            else:
                label_main.config(text="Попыток не осталось!")
                label.config(text="Ответ неправильный! Зарандомили новое слово")
                click_rand()
                k = 3
        else:
            label.config(text="Ошибка ввода! Введите заново!")
    else:
        label.config(text="Вы не зарандомили!")

def click_rand():
    global rus, eng
    rus, eng = random.choice(list(dictionary.items()))
    label.config(text=rus)

k = 3
dictionary = {"яблоко": "apple",
              "абрикос": "apricot",
              "апельсин": "orange",
              "груша": "pear",
              "лайм": "lime",
              "мандарин": "tangerine",
              "персик": "peach",
              "дыня": "melon",
              "лимон": "lemon",
              "папайя": "papaya",
              }

window = tkinter.Tk()
window.title("Угадай слово")
label_main = tkinter.Label(window, text="У тебя есть " + str(4) + " попытки: ")
label_main.pack()

frame = tkinter.Frame(window)
frame.pack()
entry = tkinter.Entry(frame)
entry.pack()
label = tkinter.Label(frame)
label.pack()


button_1 = tkinter.Button(frame, text="Зарандомить", width='30', command=click_rand)
button_1.pack()
button_2 = tkinter.Button(frame, text="Попытка", width='30', command=lambda: inpWord())
button_2.pack()

exit_butt = tkinter.Button(frame, text='Выход', width='30', command=exit)
exit_butt.pack()
window.mainloop()
