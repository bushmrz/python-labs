import tkinter


def click():
    farin = 9/5 * float(entry.get()) + 32
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