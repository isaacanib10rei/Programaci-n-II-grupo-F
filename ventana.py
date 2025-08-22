import tkinter as tk
from tkinter import messagebox
#Pacientes
def NuevoPaciente():
    ventanaRegistro=tk.Toplevel(ventanaPrincipal)
    ventanaRegistro.title("Registro de Paciente")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="#FF0000")
    #Nombre
    nombreLabel=tk.Label(ventanaRegistro, text= "Nombre:")
    nombreLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w")# n=norte, s=sur, e=este, w=oeste,we,ns,
    entryNombre=tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
    #Direccion
    direccionLabe=tk.Label(ventanaRegistro, text= "Direcion:")
    direccionLabe.grid(row=1, column=0, padx=10, pady=5, sticky="w")# n=norte, s=sur, e=este, w=oeste,we,ns,
    entryDireccion=tk.Entry(ventanaRegistro)
    entryDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")
    #Telefono
    telefonoLabel=tk.Label(ventanaRegistro, text= "Telefono:")
    telefonoLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w")# n=norte, s=sur, e=este, w=oeste,we,ns,
    entryTelefono=tk.Entry(ventanaRegistro)
    entryTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")
    #Radiobutton
    sexoLabel=tk.Label(ventanaRegistro, text="Sexo:")
    sexoLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    sexo=tk.StringVar(value="Masculino")
    sexoLabel=tk.StringVar(value="Masculino")
    rbMasculino=tk.Radiobutton(ventanaRegistro, text="Masculino", variable=sexo,value="Masculino")
    rbMasculino.grid(row=3, column=1, sticky="w")
    rbFemenino=tk.Radiobutton(ventanaRegistro, text="Femenino", variable=sexo,value="Femenino")
    rbFemenino.grid(row=4, column=1, sticky="w")
    #Emfermedades de base
    enfLabel=tk.Label(ventanaRegistro,text="Emfermedades base:")
    enfLabel.grid(row=5, column=0, padx=0, pady=5, sticky="w")
    diabetes=tk.BooleanVar()
    hipertension=tk.BooleanVar()
    asma=tk.BooleanVar()
    #Emfermedades base(checkbutton)
    cbDiabetes=tk.Checkbutton(ventanaRegistro,text="Diabetes",variable=diabetes)
    cbDiabetes.grid(row=5, column=1, sticky="w")
    cbHipertension=tk.Checkbutton(ventanaRegistro, text="Hipertension", variable=hipertension)
    cbHipertension.grid(row=6, column=1, sticky="w")
    cbAsma=tk.Checkbutton(ventanaRegistro, text="Asma", variable=asma)
    cbAsma.grid(row=7, column=1, sticky="w")
    #Cadena para mostrar los datos del formulario
    def registrarDatos():
        enfermedades=[]
        if diabetes.get():
            enfermedades.append("Diabetes")
        if hipertension.get():
            enfermedades.append("Hipertension")
        if asma.get():
            enfermedades.append("Asma")
        if len(enfermedades)>0:
            enfermedadesTexto=','.join(enfermedades)
        else:
            enfermedadesTexto='Ninguna'
        info=(
        f"Nombre: {entryNombre.get()}\n"
        f"Direccion:{entryDireccion.get()}\n"
        f"Telefono: {entryTelefono.get()}\n"
        f"Sexo:{sexo.get()}\n"
        f"Emfermedades:{enfermedadesTexto}"
    )
        messagebox.showinfo("Datos Registrado", info)
        ventanaRegistro.destroy() # Cierra la Ventana tras el mensaje
    btnRegistrar=tk.Button(ventanaRegistro, text="Datos Registrado", command=registrarDatos)
    btnRegistrar.grid(row=9, column=0, columnspan=2, pady=15)
def BuscarPaciente():
    messagebox.showinfo("Buscar Paciente","Busqueda de Pacientes")
def EliminarPaciente():
    messagebox.showinfo("Eliminar Paciente","Eliminacion de Pacientes")
#Doctores
def NuevoDoctor():
    messagebox.showinfo("Nuevo Nuevo", "Registrar Doctor")
def BuscarDoctor():
    messagebox.showinfo("Buscar Doctor","Busqueda de Doctores")
def EliminarDoctor():
    messagebox.showinfo("Eliminar Doctor","Eliminacion de Doctores")
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Sistema de registro de pacientes")
ventanaPrincipal.geometry("800x600")
ventanaPrincipal.configure(bg="#FF0000")
#Barra de menu
barraMenu=tk.Menu(ventanaPrincipal)
ventanaPrincipal.configure(menu=barraMenu)
#Menu Pacientes
menuPacientes=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Pacientes", menu=menuPacientes)
menuPacientes.add_command(label="Nuevo Paciente", command=NuevoPaciente)
menuPacientes.add_command(label="Buscar Paciente", command=BuscarPaciente)
menuPacientes.add_command(label="Eliminar Paciente", command=EliminarPaciente)
menuPacientes.add_separator()
menuPacientes.add_command(label="Salir", command=ventanaPrincipal.quit)
#Menu Doctores
menuDoctores=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor", command=NuevoDoctor)
menuDoctores.add_command(label="Buscar Doctor", command=BuscarDoctor)
menuDoctores.add_command(label="Eliminar Doctor", command=EliminarDoctor)
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir", command=ventanaPrincipal.quit)
#Ayuda
menuAyuda=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Version 1.0 - Sistema Biomedicina"))
ventanaPrincipal.mainloop()
 