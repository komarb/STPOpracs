from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import scrolledtext


def removeQuotes(string, qm):
    qmend = ""
    searchind = 0
    count = 0
    if qm == "(":
        qmend = ")"
    elif qm == "«":
        qmend = "»"
    while string.find(qm, searchind) != -1 and string.find(qmend, searchind) != -1:
        count += 1
        lind = string.find(qm, searchind)
        rind = string.find(qmend, searchind)
        if lind > rind:
            searchind = string.find(qmend, searchind) + 1
            continue
        len = rind - lind - 1
        string = string[:lind + 1] + str(len) + string[rind:]
        searchind = string.find(qmend, searchind) + 1
    if count == 0:
        return -1
    print(string)
    return string


def clicked():
    res = removeQuotes(inp.get(), combo.get())
    if res == -1:
        messagebox.showinfo('Внимание!', 'В введеной строке требуемого символа не обнаружено!')
    else:
        restxt.delete('1.0', END)
        restxt.insert('1.0', res)

window = Tk()
window.title("STPO1")
window.geometry('500x250')
window.resizable(False, False)
window.configure(background='#f9f9f9')
f_inp = LabelFrame(window, text="Ввод строки")
f_inp.pack()
inp = Entry(f_inp, width=50)
inp.pack()

f_mid = Frame(window, width=50)
f_mid.pack()
combo = Combobox(f_mid, width=10, state="readonly")
combo['values'] = ("(", "«")
combo.current(0)
combo.pack(side=LEFT)
btn = Button(f_mid, text="Преобразовать", command=clicked)
btn.pack(side=RIGHT)

f_text = Frame(window, width=50)
f_text.pack()
restxt = scrolledtext.ScrolledText(f_text, width=40, height=10)
restxt.insert('1.0', "Результат будет отображаться здесь")
restxt.pack()

window.mainloop()

'''while 1:
    qm = input("Круглая скобка - 1\nДвойная кавычка - 2\nВыберите символ:")
    if qm == "1":
        string = input("Введите строку: ")
        res = removeQuotes(string, "(")
        if res == -1:
            print("В введеной строке требуемого симовола не обнаружено!")
        else:
            print(res)
        break
    elif qm == "2":
        string = input("Введите строку: ")
        res = removeQuotes(string, "«")
        if res == -1:
            print("В введеной строке требуемого симовола не обнаружено!")
        else:
            print(res)
        break
    else:
        print("Некорректный вариант")
'''
