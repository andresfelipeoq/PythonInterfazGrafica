from tkinter import *

raiz=Tk()

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")


edicionMenu=Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")

herramientaMenu=Menu(barraMenu,tearoff=0)
herramientaMenu.add_command(label="Reemplazar")

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")



barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=edicionMenu)
barraMenu.add_cascade(label="Herramienta", menu=herramientaMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

raiz.mainloop()
