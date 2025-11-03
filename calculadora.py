# projeto 1 - calculadora 

from tkinter import * 
from tkinter import ttk              # importando a biblioteca, "*" usadao para importar tudo de dentro da biblioteca

# cores

cor1 = "#121213" #preto
cor2 = "#DFDFE9" #branco
cor3 = "#04048F" #azul escuro
cor4 = "#C4BBBB" #cinza
cor5 = "#E69626" #laranja



janela = Tk()
janela.title("Calculadora")
janela.geometry("226x259")           # tamanho, 1º valor = largura e 2º valor = altura
janela.config(bg=cor1)

# criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)



#variável todos os valores

todos_valores=''


# criando label

valor_texto = StringVar()


    # criando função

def entrar_valores(substituivel):

    global todos_valores

    todos_valores = todos_valores + str(substituivel)
    
    # passando o valor para tela
    valor_texto.set(todos_valores)


    # função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))


#função limpar tela

def limpa_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")




app_label = Label(frame_tela, textvariable= valor_texto, width=16, height=2, bg=cor3, fg=cor2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 16 bold'))   # "padx" significa margem
app_label.place(x=0, y=0)

# criando botoes

b1 = Button(frame_corpo, command=limpa_tela, text="C", width=14, height=2, bg= cor4, relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%", width=7, height=2, bg= cor4)
b2.place(x=108, y=0)
b3 = Button(frame_corpo, command= lambda: entrar_valores('/'), text="/", width=7, height=2, bg= cor5, fg= cor2 )
b3.place(x=167, y=0)

b4 = Button(frame_corpo, command= lambda: entrar_valores('7'), text="7", width=7, height=2, bg= cor4)
b4.place(x=0, y=42)
b5 = Button(frame_corpo, command= lambda: entrar_valores('8'), text="8", width=7, height=2, bg= cor4)
b5.place(x=55, y=42)
b6 = Button(frame_corpo, command= lambda: entrar_valores('9'), text="9", width=7, height=2, bg= cor4)
b6.place(x=108, y=42)
b7 = Button(frame_corpo, command= lambda: entrar_valores('*'), text="*", width=7, height=2, bg= cor5, fg= cor2)
b7.place(x=167, y=42)


b8 = Button(frame_corpo, command= lambda: entrar_valores('4'), text="4", width=7, height=2, bg= cor4)
b8.place(x=0, y=84)
b9 = Button(frame_corpo, command= lambda: entrar_valores('5'), text="5", width=7, height=2, bg= cor4)
b9.place(x=55, y=84)
b10 = Button(frame_corpo, command= lambda: entrar_valores('6'), text="6", width=7, height=2, bg= cor4)
b10.place(x=108, y=84)
b11 = Button(frame_corpo, command= lambda: entrar_valores('-'), text="-", width=7, height=2, bg= cor5, fg= cor2)
b11.place(x=167, y=84)

b12 = Button(frame_corpo, command= lambda: entrar_valores('1'), text="1", width=7, height=2, bg= cor4)
b12.place(x=0, y=126)
b13 = Button(frame_corpo, command= lambda: entrar_valores('2'), text="2", width=7, height=2, bg= cor4)
b13.place(x=55, y=126)
b14 = Button(frame_corpo, command= lambda: entrar_valores('3'), text="3", width=7, height=2, bg= cor4)
b14.place(x=108, y=126)
b15 = Button(frame_corpo, command= lambda: entrar_valores('+'), text="+", width=7, height=2, bg= cor5, fg= cor2)
b15.place(x=167, y=126)

b16 = Button(frame_corpo, command= lambda: entrar_valores('0'), text="0", width=14, height=2, bg= cor4, relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=168)
b17 = Button(frame_corpo, command= lambda: entrar_valores('.'), text=".", width=7, height=2, bg= cor4)
b17.place(x=108, y=168)
b18 = Button(frame_corpo, command= calcular, text="=", width=7, height=2, bg= cor5, fg= cor2)
b18.place(x=167, y=168)


janela.mainloop()