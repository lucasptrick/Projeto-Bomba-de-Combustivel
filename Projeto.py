from tkinter import *
from tkinter import ttk


valoresCombustiveis = [6,4,7]
combustiveis = ["Gasolina","Etanol","Diesel"]
boasVindas = "Bem vindo(a) ao Posto JML²"
textoInicio = "Escolha uma opção de combustivel:"
separador = "|---------------------------------|"
assinatura='team JML².exe'
root = Tk()
rBValue = IntVar()
rBValue.set(True)

root.title('Posto de Combustível JML²')
root.geometry('400x500')
root.resizable(False, False)
logo = PhotoImage(file='logoPostoJML.png') 
logo = logo.subsample(2,2)

def inicio():
    inicioFrame = ttk.Frame(root,padding=5)
    inicioFrame.grid(column=0 ,row=2 , sticky=(N, W, E, S)) # type: ignore

    label_logo = Label(inicioFrame, image=logo)
    label_logo.grid(column=0, row=0, pady=3)

    ttk.Label(inicioFrame, text=boasVindas, font=('Georgia',12,'bold'), foreground='#ff6f00').grid(column=0, row=2, pady=0)
    ttk.Label(inicioFrame,text=separador,font=('Georgia',12),foreground='#ff6f00').grid(column=0, row=3, pady=10)
    ttk.Label(inicioFrame, text=textoInicio, font=('Georgia',11), foreground='#000000').grid(column=0, row=4, pady=0)
    
    ttk.Button(inicioFrame,text='Gasolina',command=lambda:intermediaria(0,inicio)).grid(column=0, row=5, padx=150)
    ttk.Button(inicioFrame,text='Etanol',command=lambda:intermediaria(1,inicio)).grid(column=0, row=6, padx=150)
    ttk.Button(inicioFrame,text='Diesel',command=lambda:intermediaria(2,inicio)).grid(column=0, row=7, padx=150)
    ttk.Button(inicioFrame,text='Sair',command=root.quit).grid(column=0, row=8, padx=150)
   
    ttk.Label(inicioFrame,text=separador,font=('Georgia',12),foreground='#ff6f00').grid(column=0, row=9, pady=0)
    ttk.Label(inicioFrame,text=assinatura,font=('Consolas',9,'bold'),foreground='#000000').grid(column=0, row=10, pady=1)


formaPedido = ["Digite abaixo a quantidade em litros","Digite abaixo a quantidade em reais"]  

def intermediaria(comb,voltar):
    resultado = StringVar()
    textoPreEntry= StringVar()
    textoPreEntry.set(formaPedido[rBValue.get()-1])

    def troca():
        textoPreEntry.set(formaPedido[rBValue.get()-1])

    def calcular(qtd,f,comb,mdp):
        if f == 1:
            if mdp == 0:
                x=qtd*valoresCombustiveis[comb]
                resultado.set(f'R$ {x:,.2f} de {combustiveis[comb]}')
            elif mdp ==1:
                x=qtd*valoresCombustiveis[comb]
                x=x*1.08
                resultado.set(f'R$ {x:,.2f} de {combustiveis[comb]}')
        else:
            if mdp == 0:
                resultado.set(f'{str(qtd/valoresCombustiveis[comb])} L de {combustiveis[comb]}')
            elif mdp == 1:
                x=qtd/valoresCombustiveis[comb]
                x=x*0.92
                resultado.set(f'{str(x)} L de {combustiveis[comb]}')

    intermediariaFrame = ttk.Frame(root,padding=5)
    intermediariaFrame.grid(column = 0,row=2,sticky=(N,W,E,S)) # type: ignore

    label_logo = Label(intermediariaFrame, image=logo)
    label_logo.grid(column=0, row=0, pady=3)
    

    ttk.Label(intermediariaFrame,text="Método de Abastecimento",font=('Georgia',12,'bold'),foreground='#ff6f00').grid(column=0,row=3)
    
    rBL = Radiobutton(intermediariaFrame,text='Litros',var=rBValue,value=1, command=troca).grid(column=0,row=4,padx=150) # type: ignore
    rBR= Radiobutton(intermediariaFrame,text='Reais',var=rBValue,value=2,command=troca).grid(column=0,row=5,padx=150) # type: ignore
    
    labelResultado = ttk.Label(intermediariaFrame)
    
    ttk.Label(intermediariaFrame,textvariable=textoPreEntry).grid(column=0,row=6)
    qtd = ttk.Entry(intermediariaFrame)
    qtd.grid(column=0,row=7,padx=100,pady=5)

    ttk.Button(intermediariaFrame,text=' Calcular a vista ',command=lambda:calcular(int(qtd.get()),rBValue.get(),comb,0)).grid(column=0,row=8)
    ttk.Button(intermediariaFrame,text='Calcular no cartão',command=lambda:calcular(int(qtd.get()),rBValue.get(),comb,1)).grid(column=0,row=9)

    ttk.Label(intermediariaFrame,textvariable=resultado,font=('Courier',10),foreground='#ff6f00').grid(column=0,row=10) #
    ttk.Button(intermediariaFrame,text='Voltar',command=voltar).grid(column=0,row=11,padx=150)
inicio()

root.mainloop()

#'   _/﹋\_       _/﹋\_       _/﹋\_       _/﹋\_      ')
#'   (҂`_´)       (҂`_´)       (҂`_´)       (҂`_´)     ')
#'   <,︻╦╤─      <,︻╦╤─      <,︻╦╤─      <,︻╦╤─     ')
#'  _/﹋\_        _/﹋\_       _/﹋\_       _/﹋\_      ')
#' SR.JAIR.V    SR.MATHEUS.K SR.LUCAS.P    SR.LUCAS.M  ')
#'     limited development team JML.exe ᕦ(ò_óˇ)ᕤ      ')