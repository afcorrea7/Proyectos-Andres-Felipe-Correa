from tkinter import * #libreria de GUI.

#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    decimalT.delete("0", "end")
    binarioT.delete("0","end")
    OctadecimalT.delete("0","end")
    HexadecimalT.delete("0","end")
#-------------------------------------------------------------------------------------------
#creacion de ventana principal.
Ventana = Tk()
Ventana.title("Calculadora Conversora")
#Ventana.geometry("550x550") #tamaño.
Ventana.resizable(0,0) #bloqueo de tamaño.
Ventana.iconbitmap('Interfaz\calculadora.ico') #icono.
#-------------------------------------------------------------------------------------------
#Creacion del frame.
FrameV=Frame()
FrameV.pack()
FrameV.config(bg="light grey") #color de fondo.
#-------------------------------------------------------------------------------------------
#Labels (etiquetas).
binarioL=Label(FrameV, text="Binario:")
binarioL.grid(row=0, column=0, sticky="w", padx=10, pady=10)
binarioL.config(bg="light grey") #color de fondo.

decimalL=Label(FrameV, text="Decimal:")
decimalL.grid(row=1, column=0, sticky="w", padx=10, pady=10)
decimalL.config(bg="light grey") #color de fondo.

OctadecimalL=Label(FrameV,text="Octadecimal:")
OctadecimalL.grid(row=2, column=0, sticky="w", padx=10, pady=10)
OctadecimalL.config(bg="light grey") #color de fondo.

HexadecimalL=Label(FrameV, text="Hexadecimal:")
HexadecimalL.grid(row=3, column=0, sticky="w", padx=10, pady=10)
HexadecimalL.config(bg="light grey") #color de fondo.
#-------------------------------------------------------------------------------------------
#Cajas de texto.
binarioT=Entry(FrameV)
binarioT.grid(row=0, column=1, padx=10, pady=10)
binarioT.config(justify="center")

decimalT=Entry(FrameV)
decimalT.grid(row=1, column=1, padx=10, pady=10)
decimalT.config(justify="center")

OctadecimalT=Entry(FrameV)
OctadecimalT.grid(row=2, column=1, padx=10, pady=10)
OctadecimalT.config(justify="center")

HexadecimalT=Entry(FrameV)
HexadecimalT.grid(row=3, column=1, padx=10, pady=10)
HexadecimalT.config(justify="center")
#-------------------------------------------------------------------------------------------
#Botones.
CalcularB=Button(FrameV, text="Calcular")
CalcularB.grid(row=4, column=1, pady=10)

BorrarB=Button(FrameV, text="Borrar", command=clearcomm)
BorrarB.grid(row=4, column=0, pady=10)

SalirB=Button(FrameV, text="Salir", command=Ventana.destroy)
SalirB.grid(row=4, column=2, pady=10, padx=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop() #es el ciclo para que la ventana "exista".