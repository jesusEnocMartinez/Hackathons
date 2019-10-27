try:
    # for Python2
    from tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

class interfaz:

def donothing():
   root = Toplevel(root)
   button = Button(root, text="Cuestionario")
   button.pack()
   
root = Tk()
menubar = Menu(root) 
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo Cuestionario", command=donothing)

filemenu.add_command(label="Cerrar", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Menu", menu=filemenu, witd=300)
editmenu = Menu(menubar, tearoff=0)

root.config(menu=menubar)

l = Button(root, text="Do nothing button")
l.pack
root.mainloop()