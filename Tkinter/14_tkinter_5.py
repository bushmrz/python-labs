import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox

res = 0.0
def click():
    # Получаем строковое содержимое поля ввода с помощью метода get()
    # C помощью config() можем изменить отображаемый текст
    global res
    if entry.get().isdigit():
        inp = float(entry.get())
        try:
            res = (4 * 3.14 * inp ** 3) / 3
            answ_label.config(text=res)
        except:
            answ_label.config(text="Ошибка, введите число!")
    else:
        answ_label.config(text="Ошибка, введите число!")

def save_click_txt():
    text = entry.get()
    with open('../sphere.txt', 'w', encoding="utf8") as file:
        file.write('Объем для сферы радиуса '+ text + ' равен ' + str(res))


def save_click_html():
    text = entry.get()
    with open('sphere.html', 'w') as myFile:
        myFile.write('<html> \n<body> \n')
        myFile.write('<b> Радиус сферы равен: </b>')
        myFile.write('<br>' + text + '</br>')
        myFile.write('<b> Объем сферы равен: </b>')
        myFile.write('<br>' + str(res) + '</br>')
        myFile.write('\n</body> \n</html>')

def check_choose():
    if comboBox.get() == 'HTML':
        save_click_html()
    else:
        save_click_txt()

app = Tk()

app.geometry('400x250')
label_main = Label(app, text="Программа для вычисления объема сферы")
label_main.pack()



frame_radius = Frame(app)
frame_radius.pack()
label_r = Label(frame_radius, text='Введите радиус: ')
label_r.pack(side=LEFT)
entry = Entry(frame_radius, font=('Helvetica', 20))
entry.pack(side=RIGHT)


frame_val = Frame(app)
frame_val.pack()
label_v = Label(frame_val, text='Объем равен: ')
label_v.pack(side=LEFT)
answ_label = Label(frame_val, font=('Helvetica', 20), text='                                       ')
answ_label.pack(side=RIGHT)

exit_butt = Button(app, text='Посчитать', command=click)
exit_butt.pack()

frame_2 = Frame(app)
frame_2.pack()

save_butt = Button(frame_2, text='Сохранить', command=check_choose)
save_butt.pack(side=LEFT)


# menubar = Menu(app)
# menu = Menu(menubar, tearoff=0 )
# menubar.add_cascade(label = 'Save as...', menu = menu)
# menu.add_command(label = 'TXT', command=save_click_txt)
# menu.add_command(label = 'HTML', command=save_click_html)
#
# app.config(menu=menubar)


comboBox = Combobox(frame_2, width= 40, values=[
    'TXT',
    'HTML'
])
comboBox.set('Save as...')

comboBox.pack(side=RIGHT)
app.mainloop()