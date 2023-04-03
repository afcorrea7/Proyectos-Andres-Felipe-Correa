from tkinter import * #libreria de GUI

#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    FuncionX.delete("0", "end")
    PuntoX.delete("0","end")
    ErrorT.delete("0","end")
    ResultadoT.delete("0","end")
#-------------------------------------------------------------------------------------------
#creacion de ventana principal.
Ventana = Tk()
Ventana.title("Calculadora Newton")
Ventana.resizable(0,0) #bloqueo de tamaño.
Ventana.iconbitmap('Interfaz\calculadora.ico') #icono.
#-------------------------------------------------------------------------------------------
#Creacion del frame.
FrameV=Frame()
FrameV.pack()
FrameV.config(bg="light grey") #color de fondo.
#-------------------------------------------------------------------------------------------
#Labels (etiquetas, todo lo que tenga "_L").
FuncionX_L=Label(FrameV, text="Funcion en X:")
FuncionX_L.grid(row=2, column=0, padx=10, pady=10)
FuncionX_L.config(bg="light grey") #color de fondo.

PuntoX_L=Label(FrameV, text="Punto X:")
PuntoX_L.grid(row=3, column=0, padx=10, pady=10)
PuntoX_L.config(bg="light grey") #color de fondo.

ErrorT_L=Label(FrameV, text="Error de tolerancia:")
ErrorT_L.grid(row=4, column=0, padx=10, pady=10)
ErrorT_L.config(bg="light grey") #color de fondo.

Resultado_L=Label(FrameV, text="Resultado:")
Resultado_L.grid(row=5, column=0, padx=10, pady=10)
Resultado_L.config(bg="light grey") #color de fondo.
#-------------------------------------------------------------------------------------------
#Cajas de texto.
FuncionX=Entry(FrameV)
FuncionX.grid(row=2, column=1, padx=10, pady=10)
FuncionX.config(justify="center")

PuntoX=Entry(FrameV)
PuntoX.grid(row=3, column=1, padx=10, pady=10)
PuntoX.config(justify="center")

ErrorT=Entry(FrameV)
ErrorT.grid(row=4, column=1, padx=10, pady=10)
ErrorT.config(justify="center")

ResultadoT=Entry(FrameV)
ResultadoT.grid(row=5, column=1, padx=10, pady=10)
ResultadoT.config(justify="center")
ResultadoT.config(state=DISABLED)
#-------------------------------------------------------------------------------------------
#Botones.
BorrarB=Button(FrameV, text="Borrar", command=clearcomm)
BorrarB.grid(row=6, column=0, pady=10)

CalcularB=Button(FrameV, text="Calcular")
CalcularB.grid(row=6, column=1, pady=10, padx=10)

SalirB=Button(FrameV, text="Salir", command=Ventana.destroy)
SalirB.grid(row=6, column=2, pady=10, padx=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop() #es el ciclo para que la ventana "exista"