from tkinter import *
tela = Tk()
lbllogin = Label(tela,text = 'login')
lbllogin.grid(row=1,column=1)

etrlogin = Entry(tela)
etrlogin.grid(row=1, column=2)

lblsenha = Label(tela,text = 'senha')
lblsenha.grid(row=2,column=1)

etrsenha = Entry(tela)
etrsenha.grid(row=2, column=2)

btnlogar = Button(tela,text = 'logar')
btnlogar.grid(row=3,column=1,columnspan=2)

tela.mainloop()