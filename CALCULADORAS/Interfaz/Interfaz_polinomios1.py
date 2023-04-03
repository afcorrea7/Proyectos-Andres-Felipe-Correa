from tkinter import * #libreria de GUI

#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    Tcuadratico.delete("0", "end")
    Tlineal.delete("0","end")
    Tindependiente.delete("0","end")
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
Tcuadratico_L=Label(FrameV, text="Termino cuadratico:")
Tcuadratico_L.grid(row=2, column=0, padx=10, pady=10)
Tcuadratico_L.config(bg="light grey") #color de fondo.

Tlineal_L=Label(FrameV, text="Termino lineal:")
Tlineal_L.grid(row=3, column=0, padx=10, pady=10)
Tlineal_L.config(bg="light grey") #color de fondo.

Tindependiente_L=Label(FrameV, text="Termino independiente:")
Tindependiente_L.grid(row=4, column=0, padx=10, pady=10)
Tindependiente_L.config(bg="light grey") #color de fondo.

Resultado_L=Label(FrameV, text="Resultado:")
Resultado_L.grid(row=5, column=0, padx=10, pady=10)
Resultado_L.config(bg="light grey") #color de fondo.
#-------------------------------------------------------------------------------------------
#Cajas de texto.
Tcuadratico=Entry(FrameV)
Tcuadratico.grid(row=2, column=1, padx=10, pady=10)
Tcuadratico.config(justify="center")

Tlineal=Entry(FrameV)
Tlineal.grid(row=3, column=1, padx=10, pady=10)
Tlineal.config(justify="center")

Tindependiente=Entry(FrameV)
Tindependiente.grid(row=4, column=1, padx=10, pady=10)
Tindependiente.config(justify="center")

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