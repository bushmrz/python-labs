import tkinter as tk
from tkinter import *


def save_click_txt():
    text = entry.get()
    with open('myfile.txt', 'w') as file:
        file.write(text)


def save_click_html():
    text = entry.get()
    with open('mypage.html', 'w') as myFile:
        myFile.write('<html> \n<body> \n')
        myFile.write('<br>' + text + '</br>')
        myFile.write('\n</body> \n</html>')


app = Tk()

app.geometry('400x150')
label_main = Label(app, text="Введите текст")
label_main.pack()

frame = Frame(app)
frame.pack()
entry = Entry(frame, font=('Helvetica', 25))
entry.pack()
label = Label(frame)
label.pack()

exit_butt = Button(frame, text='Выход', command=exit)
exit_butt.pack()


menubar = Menu(app)
menu = Menu(menubar, tearoff=0 )
menubar.add_cascade(label = 'Save as...', menu = menu)
menu.add_command(label = 'TXT', command=save_click_txt)
menu.add_command(label = 'HTML', command=save_click_html)

app.config(menu=menubar)

app.mainloop()