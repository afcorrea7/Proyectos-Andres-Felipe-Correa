from tkinter import *

#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    FuncionX_T.delete("0", "end")
    ValA_T.delete("0","end")
    ValB_T.delete("0","end")
    partes_T.delete("0","end")
    resultado_T.delete("0","end")
    Error_T.delete("0","end")

#-------------------------------------------------------------------------------------------
#creacion de ventana principal.
Ventana = Tk()
Ventana.title("Calculadora Simpson")
#Ventana.resizable(0,0)
#-------------------------------------------------------------------------------------------
#Creacion del frame.
FrameV=Frame()
FrameV.pack()
FrameV.config(bg="light grey")
#-------------------------------------------------------------------------------------------
#Etiquetas
FuncionX_L = Label(FrameV, text="Funcion en x")
FuncionX_L.grid(row=1, column=0, padx=10, pady=10)
FuncionX_L.config(bg="light grey") 

ValA_L = Label(FrameV, text="Valor A")
ValA_L.grid(row=2, column=0, padx=10, pady=10)
ValA_L.config(bg="light grey")

ValB_L = Label(FrameV, text="Valor B")
ValB_L.grid(row=3, column=0, padx=10, pady=10)
ValB_L.config(bg="light grey")

partes_L = Label(FrameV, text="Numero de particiones")
partes_L.grid(row=4, column=0, padx=10, pady=10)
partes_L.config(bg="light grey")

resultado_L = Label(FrameV, text="Resultado")
resultado_L.grid(row=5, column=0, padx=10, pady=10)
resultado_L.config(bg="light grey")

Error_L = Label(FrameV, text="Error")
Error_L.grid(row=6, column=0, padx=10, pady=10)
Error_L.config(bg="light grey")
#-------------------------------------------------------------------------------------------
#Cajas de texto
FuncionX_T = Entry(FrameV)
FuncionX_T.grid(row=1, column=1, padx=10, pady=10)
FuncionX_T.config(justify="center")

ValA_T = Entry(FrameV)
ValA_T.grid(row=2, column=1, padx=10, pady=10)
ValA_T.config(justify="center")

ValB_T = Entry(FrameV)
ValB_T.grid(row=3, column=1, padx=10, pady=10)
ValB_T.config(justify="center")

partes_T = Entry(FrameV)
partes_T.grid(row=4, column=1, padx=10, pady=10)
partes_T.config(justify="center")

resultado_T = Entry(FrameV)
resultado_T.grid(row=5, column=1, padx=10, pady=10)
resultado_T.config(justify="center")

Error_T = Entry(FrameV)
Error_T.grid(row=6, column=1, padx=10, pady=10)
Error_T.config(justify="center")

#-------------------------------------------------------------------------------------------
#Botones
calcular = Button(FrameV, text="Calcular")
calcular.grid(row=7, column=1, padx=10, pady=10)

Salir = Button(FrameV, text="Salir", command=Ventana.destroy)
Salir.grid(row=8, column=1, padx=10, pady=10)

Graficar = Button(FrameV, text="Graficar")
Graficar.grid(row=7, column=0, padx=10, pady=10)

Borrar = Button(FrameV, text="Borrar", command=clearcomm)
Borrar.grid(row=7, column=2, padx=10, pady=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop()