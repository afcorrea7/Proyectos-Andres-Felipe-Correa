from tkinter import * #libreria de GUI.

#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    decimalT.delete("0", "end")
    Signo32.delete("0","end")
    Exponente32.delete("0","end")
    Mantisa32.delete("0","end")
    Signo64.delete("0","end")
    Exponente64.delete("0","end")
    Mantisa64.delete("0","end")
#-------------------------------------------------------------------------------------------
#creacion de ventana principal.
Ventana = Tk()
Ventana.title("Calculadora IEEE")
Ventana.resizable(0,0) #bloqueo de tamaño.
Ventana.iconbitmap('Interfaz\calculadora.ico') #icono.
#-------------------------------------------------------------------------------------------
#Creacion del frame.
FrameV=Frame()
FrameV.pack()
FrameV.config(bg="light grey") #color de fondo.
#-------------------------------------------------------------------------------------------
#Labels (Etiquetas).
DecimalL=Label(FrameV, text="Decimal:")
DecimalL.grid(row=0, column=0, padx=10, pady=10)
DecimalL.config(bg="light grey") #color de fondo.

#32 bits.
IeeL32=Label(FrameV, text="IEE 32 bits")
IeeL32.grid(row=1, column=1)
IeeL32.config(bg="light grey") #color de fondo.

Signo32_L=Label(FrameV, text="Signo:")
Signo32_L.grid(row=2, column=0, pady=5, padx=5)
Signo32_L.config(bg="light grey") #color de fondo.

Exponente32_L=Label(FrameV, text="Exponente:")
Exponente32_L.grid(row=3, column=0, pady=5, padx=5)
Exponente32_L.config(bg="light grey") #color de fondo.

Mantisa32_L=Label(FrameV, text="Mantisa:")
Mantisa32_L.grid(row=4, column=0, pady=5, padx=5)
Mantisa32_L.config(bg="light grey") #color de fondo.

#64 bits.
IeeL64=Label(FrameV, text="IEE 64 bits")
IeeL64.grid(row=5, column=1)
IeeL64.config(bg="light grey") #color de fondo.

Signo64_L=Label(FrameV, text="Signo:")
Signo64_L.grid(row=6, column=0, pady=5, padx=5)
Signo64_L.config(bg="light grey") #color de fondo.

Exponente64_L=Label(FrameV, text="Exponente:")
Exponente64_L.grid(row=7, column=0, pady=5, padx=5)
Exponente64_L.config(bg="light grey") #color de fondo.

Mantisa64_L=Label(FrameV, text="Mantisa:")
Mantisa64_L.grid(row=8, column=0, pady=5, padx=5)
Mantisa64_L.config(bg="light grey") #color de fondo.
#-------------------------------------------------------------------------------------------
#Cajas de texto.
decimalT=Entry(FrameV)
decimalT.grid(row=0, column=1, padx=10, pady=10)
decimalT.config(justify="center")

#32 bits.
Signo32=Entry(FrameV)
Signo32.grid(row=2, column=1, padx=10, pady=10)
Signo32.config(justify="center")

Exponente32=Entry(FrameV)
Exponente32.grid(row=3, column=1, padx=10, pady=10)
Exponente32.config(justify="center")

Mantisa32=Entry(FrameV)
Mantisa32.grid(row=4, column=1, padx=10, pady=10)
Mantisa32.config(justify="center")

#64 bits.
Signo64=Entry(FrameV)
Signo64.grid(row=6, column=1, padx=10, pady=10)
Signo64.config(justify="center")

Exponente64=Entry(FrameV)
Exponente64.grid(row=7, column=1, padx=10, pady=10)
Exponente64.config(justify="center")

Mantisa64=Entry(FrameV)
Mantisa64.grid(row=8, column=1, padx=10, pady=10)
Mantisa64.config(justify="center")
#-------------------------------------------------------------------------------------------
#Botones.
CalcularB=Button(FrameV, text="Calcular")
CalcularB.grid(row=9, column=1, pady=10)

BorrarB=Button(FrameV, text="Borrar", command=clearcomm)
BorrarB.grid(row=9, column=0, pady=10)

SalirB=Button(FrameV, text="Salir", command=Ventana.destroy)
SalirB.grid(row=9, column=2, pady=10, padx=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop() #es el ciclo para que la ventana "exista"