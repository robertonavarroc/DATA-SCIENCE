from tkinter import *
from tkinter import messagebox

def saludar():
    nombre = tbx_nombre.get()
    email = tbx_email.get()
    dni = tbx_dni.get()
    print(f"Hola, {nombre}!")
    print(f"Dni: {dni}")
    print(f"Email: {email}")
    messagebox.showinfo("Saludo",f"Hola, {nombre}!")

app = Tk()
app.title("Interfaz Alumno")
app.geometry("300x110")

frame = Frame(app)
frame.grid(row=0,column=0,padx=20,pady=10)

lbl_nombre = Label(frame,text="Ingrese su Nonbre: ")
lbl_nombre.grid(row=0, column=0)

tbx_nombre = Entry(frame)
tbx_nombre.grid(row=0,column=1)

lbl_email = Label(frame,text="Ingrese su Email: ")
lbl_email.grid(row=1, column=0)

tbx_email = Entry(frame)
tbx_email.grid(row=1,column=1)

lbl_dni = Label(frame,text="Ingrese su DNI: ")
lbl_dni.grid(row=2, column=0)

tbx_dni = Entry(frame)
tbx_dni.grid(row=2,column=1)

#crear un botón (button) dentro del frame
btn_saludar = Button(frame,text="Saludar",command=saludar, width=17)
btn_saludar.grid(row=4,column=1)

app.mainloop()