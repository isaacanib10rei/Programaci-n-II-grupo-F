import tkinter as tk
from tkinter import ttk
#crear ventana principal
ventana_Principal= tk.Tk()
ventana_Principal.title("Libro de pacientes y Doctores")
ventana_Principal.geometry("400x400")
#crear contenedores Notebook
pestañas= ttk.Notebook(ventana_Principal)
#crear frames (uno por pestañas)
frame_Pacientes= ttk.Frame(pestañas)
#agregar pestañas
pestañas.add(frame_Pacientes, text="Pacientes")
#mostrar las pestañas
pestañas.pack(expand=True, fill="both")
#añadir doctores
frame_Doctores= ttk.Frame(pestañas)
pestañas.add(frame_Doctores, text="Doctores")
#NOMBRE
labelNombre= tk.Label(frame_Pacientes, text="Nombre completo: ")
labelNombre.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreP=tk.Entry(frame_Pacientes)
nombreP.grid(row=0, column=1, sticky="w", padx=5, pady=5)
#fecha de nacimient5o
labelFechaN=tk.Label(frame_Pacientes, text="fecha de Nacimiento: ")
labelFechaN.grid(row=1, column=0, sticky="w", pady=5, padx=5)
FechaN=tk.Entry(frame_Pacientes)
FechaN.grid(row=1, column=1, sticky="w", padx=5, pady=5)
#edad
labelEdad= tk.Label(frame_Pacientes, text="edad: ")
labelEdad.grid(row=2, column=0, sticky="w", padx=5, pady=5)
edadP=tk.Entry(frame_Pacientes, state="readonly")
edadP.grid(row=2,column=1, sticky="w", padx=5, pady=5)
#genero
labelGenero=tk.Label(frame_Pacientes, text="Genero: ")
labelGenero.grid(row=3, column=0, sticky="W", pady=5,padx=5)
genero=tk.StringVar()
genero.set("Masculino")
radioMasculino=ttk.Radiobutton(frame_Pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(frame_Pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4,column=1,sticky="w", padx=5)
#grupo sanguineo
labelGruposSanguineos=tk.Label(frame_Pacientes, text="Grupo Sanguineo: ")
labelGruposSanguineos.grid(row=5, column=0, sticky="w", padx=5, pady=5)
entryGrupoSanguineo= tk.Entry(frame_Pacientes)
entryGrupoSanguineo.grid(row=5, column=1, sticky="w", padx=5, pady=5)
#tipo de seguro
labelTipoSeguro=tk.Label(frame_Pacientes, text="Tipo de seguro:")
labelTipoSeguro.grid(row=5, column=0, sticky="w", pady=5, padx=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Público") #valor por defecto
comboTipoSeguro=ttk.Combobox(frame_Pacientes, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=5, column=1, sticky="w", pady=5, padx=5)
#centro medico
labelCentroMedico=tk.Label(frame_Pacientes, text="centro de salud: ")
labelCentroMedico.grid(row=6, column=0, sticky="w", padx=5, pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")
comboCentroMedico=ttk.Combobox(frame_Pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=6, column=1, sticky="w", padx=5, pady=5)
ventana_Principal.mainloop()