from tkinter import *

#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    FuncionX_T.delete("0", "end")
    ValA_T.delete("0","end")
    ValB_T.delete("0","end")
    partes_T.delete("0","end")
    Extremo_D.delete("0","end")
    Extremo_M.delete("0","end")
    Extremo_I.delete("0","end")

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

Extremo_D = Label(FrameV, text="Extremo Derecho")
Extremo_D.grid(row=5, column=0, padx=10, pady=10)
Extremo_D.config(bg="light grey")

Extremo_M = Label(FrameV, text="Extremo Medio")
Extremo_M.grid(row=6, column=0, padx=10, pady=10)
Extremo_M.config(bg="light grey")

Extremo_I = Label(FrameV, text="Extremo Izquierdo")
Extremo_I.grid(row=7, column=0, padx=10, pady=10)
Extremo_I.config(bg="light grey")

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

Extremo_D = Entry(FrameV)
Extremo_D.grid(row=5, column=1, padx=10, pady=10)
Extremo_D.config(justify="center")

Extremo_M = Entry(FrameV)
Extremo_M.grid(row=6, column=1, padx=10, pady=10)
Extremo_M.config(justify="center")

Extremo_I = Entry(FrameV)
Extremo_I.grid(row=7, column=1, padx=10, pady=10)
Extremo_I.config(justify="center")

#-------------------------------------------------------------------------------------------
#Botones
calcular = Button(FrameV, text="Calcular")
calcular.grid(row=8, column=1, padx=10, pady=10)

Salir = Button(FrameV, text="Salir", command=Ventana.destroy)
Salir.grid(row=9, column=1, padx=10, pady=10)

Graficar = Button(FrameV, text="Graficar")
Graficar.grid(row=8, column=0, padx=10, pady=10)

Borrar = Button(FrameV, text="Borrar", command=clearcomm)
Borrar.grid(row=8, column=2, padx=10, pady=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop()