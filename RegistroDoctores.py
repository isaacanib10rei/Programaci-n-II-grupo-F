import tkinter as tk
from tkinter import ttk, messagebox
import os

ventana_principal = tk.Tk()
ventana_principal.title("Registro de Doctores")
ventana_principal.geometry("650x450")

# Frame principal
frame_doctores = tk.Frame(ventana_principal)
frame_doctores.pack(pady=10)

# Nombre
tk.Label(frame_doctores, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreD = tk.Entry(frame_doctores)
nombreD.grid(row=0, column=1, pady=5, padx=5)

# Especialidad
tk.Label(frame_doctores, text="Especialidad:").grid(row=1, column=0, sticky="w", pady=5, padx=5)
especialidad_var = tk.StringVar()
comboEspecialidad = ttk.Combobox(frame_doctores, textvariable=especialidad_var, 
                                 values=("Cardiología", "Pediatría", "Traumatología", "Neurología"))
comboEspecialidad.grid(row=1, column=1, pady=5, padx=5)

# Años de experiencia
tk.Label(frame_doctores, text="Años de Experiencia:").grid(row=2, column=0, sticky="w", pady=5, padx=5)
añosD = tk.Entry(frame_doctores)
añosD.grid(row=2, column=1, pady=5, padx=5)

# Género
labelGenero = tk.Label(frame_doctores, text="Género:")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
generoP = tk.StringVar(value="Masculino")
radioMasculino = ttk.Radiobutton(frame_doctores, text="Masculino", variable=generoP, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino = ttk.Radiobutton(frame_doctores, text="Femenino", variable=generoP, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5)

# Hospital
labelcentromedico = tk.Label(frame_doctores, text="Hospital")
labelcentromedico.grid(row=5, column=0, sticky="w", pady=5, padx=5)
centromedico = tk.StringVar(value="Hospital Central")
combotcentromedico = ttk.Combobox(frame_doctores, values=("Hospital Central", "Hospital Norte", 
                                                         "Clínica Santa María", "Clínica Vida"), 
                                  textvariable=centromedico)
combotcentromedico.grid(row=5, column=1, sticky="w", pady=5, padx=5)

# Frame de botones
btn_frame = tk.Frame(frame_doctores)
btn_frame.grid(row=6, column=0, columnspan=2, pady=5)

# Datos de los doctores
doctor_data = []

archivo_registro = "doctoresRegistro.txt"

# Guardar datos en archivo
def guardar_en_archivo():
    with open(archivo_registro, "w") as archivo:
        for doctor in doctor_data:
            datos = f"{doctor['Nombre']} | {doctor['Especialidad']} | {doctor['Años de Experiencia']} | {doctor['Género']} | {doctor['Hospital']}\n"
            archivo.write(datos)

# Leer datos desde archivo
def cargar_desde_archivo():
    if os.path.exists(archivo_registro):
        with open(archivo_registro, "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split(" | ")
                if len(partes) == 5:
                    Doctor = {
                        "Nombre": partes[0],
                        "Especialidad": partes[1],
                        "Años de Experiencia": partes[2],
                        "Género": partes[3],
                        "Hospital": partes[4]
                    }
                    doctor_data.append(Doctor)

# Registrar doctores
def registrarDoctores():
    if not nombreD.get() or not especialidad_var.get() or not añosD.get():
        messagebox.showwarning("Error", "Complete todos los campos.")
        return
    Doctor = {
        "Nombre": nombreD.get(),
        "Especialidad": especialidad_var.get(),
        "Años de Experiencia": añosD.get(),
        "Género": generoP.get(),
        "Hospital": centromedico.get()
    }
    doctor_data.append(Doctor)
    cargar_treeview()
    guardar_en_archivo()
    limpiar_campos()

# Eliminar doctor
def eliminarDoctor():
    seleccionado = treeview_doctores.selection()
    if not seleccionado:
        messagebox.showwarning("Atención", "Seleccione un doctor para eliminar.")
        return
    indice = int(seleccionado[0])
    doctor_data.pop(indice)
    cargar_treeview()
    guardar_en_archivo()

# Limpiar campos
def limpiar_campos():
    nombreD.delete(0, tk.END)
    comboEspecialidad.set("")
    añosD.delete(0, tk.END)
    generoP.set("Masculino")
    centromedico.set("Hospital Central")

# Cargar Treeview
def cargar_treeview():
    for item in treeview_doctores.get_children():
        treeview_doctores.delete(item)
    for i, item in enumerate(doctor_data):
        treeview_doctores.insert("", "end", iid=str(i), values=(
            item["Nombre"],
            item["Especialidad"],
            item["Años de Experiencia"],
            item["Género"],
            item["Hospital"]
        ))

# Botones
btn_registrar = tk.Button(btn_frame, text="Registrar", bg="green", fg="white", command=registrarDoctores)
btn_registrar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(btn_frame, text="Eliminar", bg="red", fg="white", command=eliminarDoctor)
btn_eliminar.grid(row=0, column=1, padx=5)

# Treeview con columnas separadas
treeview_doctores = ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Años de Experiencia", "Género", "Hospital"), show="headings")
treeview_doctores.heading("Nombre", text="Nombre")
treeview_doctores.heading("Especialidad", text="Especialidad")
treeview_doctores.heading("Años de Experiencia", text="Años de Experiencia")
treeview_doctores.heading("Género", text="Género")
treeview_doctores.heading("Hospital", text="Hospital")

treeview_doctores.column("Nombre", width=150)
treeview_doctores.column("Especialidad", width=120)
treeview_doctores.column("Años de Experiencia", width=130, anchor="center")
treeview_doctores.column("Género", width=100)
treeview_doctores.column("Hospital", width=120)

treeview_doctores.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)

# Scrollbar
scroll_y = ttk.Scrollbar(frame_doctores, orient="vertical", command=treeview_doctores.yview)
treeview_doctores.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=7, column=2, sticky="ns")

# Cargar datos previos del archivo
cargar_desde_archivo()
cargar_treeview()

ventana_principal.mainloop()