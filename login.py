from tkinter import *
tela = Tk()
#criando a label login e definindo a linha e coluna q  vai ficar localizado
lbllogin = Label(tela,text = 'login')
lbllogin.grid(row=1,column=1)

#Entrada de dados
etrlogin = Entry(tela)
etrlogin.grid(row=1, column=2)

lblsenha = Label(tela,text = 'senha')
lblsenha.grid(row=2,column=1)

etrsenha = Entry(tela)
etrsenha.grid(row=2, column=2)

#criando botão e columnspan é a ocupação do botão (colunas)
btnlogar = Button(tela,text = 'logar')
btnlogar.grid(row=3,column=1,columnspan=2)

#loop para que o programa só finalize a hora que fechar a TELA
tela.mainloop()