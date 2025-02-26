from tkinter import * 
from tkinter import filedialog as FileDialog
from io import open

ruta = "" #La utilizaremos para almacenar la ruta de un fichero

def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor")


def abrir():
    global ruta
    mensaje.set("Abrir fichero") 
    ruta = FileDialog.askopenfilename(
        initialdir= '.',
        filetypes=(("ficheros de texto", "*.txt"),),
        title="Abrir un fichero de texto")
    
    if ruta != "":
        fichero = open(ruta,'r')
        continido = fichero.read()
        texto.delete(1.0, 'end')
        texto.insert('insert', continido)
        fichero.close()
        root.title(ruta + " - Mi editorfm")


def guardar():
    mensaje.set("Guardar fichero") 
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El fichero se a guardado correctamente")
    else:
        guardar_como()    

def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como:") 
    fichero = FileDialog.asksaveasfile(title="Guardar Fichero", mode='w', defaultextension=".txt")  
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El fichero se ha guardado correctamente")
    else:
        mensaje.set("Guardado Canselado") 
        ruta = "" 

#Configuracion de la Raiz
root = Tk()
root.title("Mi Editor")


#Menu Superir

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir_fjmv", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar Como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")


#Caja de Texto Central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("consolas",12))

#Monitor Inferior
mensaje=StringVar()
mensaje.set("Bienvendo a tu Editor")
monitor = Label(root,textvar=mensaje, justify="left")
monitor.pack(side="left")


root.config(menu=menubar)#Con este codigo se visualiza el menubar(Archivo)
#Finalmente bucle de la aplicacion
root.mainloop()

