import random
from tkinter import *
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class GeneradorRutinas:
    def __init__(self, ejercicios):
        self.ejercicios = ejercicios

        self.ventana = Tk()
        self.ventana.title("Generador de Ejercicios.")

        self.frame1 = Frame(self.ventana, bg="dark green", height="400", width="200")
        self.frame1.pack_propagate(False)
        self.frame1.config(border = "10")
        self.frame1.config(relief = SUNKEN)
        self.frame1.pack()
        self.frame1.place(x=0, y=0)
        
        self.frame2 = Frame(self.ventana, bg="dark green", height="200", width="200", relief=SUNKEN)
        self.frame2.pack_propagate(False)
        self.frame2.config(border = "10")
        self.frame2.config(relief = SUNKEN)
        self.frame2.pack()
        self.frame2.place(x=0, y=400)

        self.label_dolor = Label(self.frame1, text="LUGAR DEL DOLOR:", font="BOLD")
        self.label_dolor.pack()
        self.label_dolor.place(x=10, y=0)
        
        self.label_dolor2 = Label(self.frame1, text="Otro:")
        self.label_dolor2.pack()
        self.label_dolor2.place(x=10, y=230)
        
        self.entry_dolor = Entry(self.frame1)
        self.entry_dolor.pack()
        self.entry_dolor.place(x=50, y=230)

        self.boton1 = Button(self.frame1, text="Piernas.", height="2", width="9")
        self.boton1.pack()
        self.boton1.place(x=50, y=50)

        self.boton2 = Button(self.frame1, text="Espalda.", height="2", width="9")
        self.boton2.pack()
        self.boton2.place(x=50, y=100)

        self.boton3 = Button(self.frame1, text="Hombros.", height="2", width="9")
        self.boton3.pack()
        self.boton3.place(x=50, y=150)

        self.boton4 = Button(self.frame2, text="Necesito Atención Medica.", command=lambda: self.mostrarMensaje())
        self.boton4.pack()
        self.boton4.place(x=15, y=70)

        self.boton5 = Button(self.frame1,text="Buscar")
        self.boton5.pack()
        self.boton5.place(x=50, y=250)

        self.label_ejercicio = Label(self.ventana, text="", font="BOLD")
        self.label_ejercicio.pack()
        self.label_ejercicio.place(x=400, y=75)

        self.label_categoria = Label(self.ventana, text="", font="BOLD")
        self.label_categoria.pack()
        self.label_categoria.place(x=399, y=103)

        self.label_dificultad = Label(self.ventana, text="", font="BOLD")
        self.label_dificultad.pack()
        self.label_dificultad.place(x=400, y=130)

        self.ventana.geometry("800x600")

    def mostrarEjercicio(self, dolor):
        rutina = self.generar_rutina(dolor)
        if rutina:
            for ejercicio in rutina:
               self.mostrarDetalle(ejercicio)
        else:
            messagebox.showinfo("Generador de Ejercicios", f"No se encontraron ejercicios relacionados con el dolor: {dolor}")
        
    def generar_rutina(self, dolor):
        ej_filter = [e for e in self.ejercicios if e['dolor_relacionado'] == dolor]
        if not ej_filter:
            print(f"No se encontraron ejercicios relacionados con el dolor: {dolor}")
        return ej_filter
    
    def guardar_rutina(self, rutina, file, dolor):
        c = canvas.Canvas(file, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(72, 720, f"----------------- {dolor} Ejercicio ----------------------")
        for ejercicio in rutina:
            c.drawString(72, 720, f"- Ejercicio: {ejercicio['nombre']}")
            c.drawString(72, 720, f"- Categoria: {ejercicio['categoria']}")
            c.drawString(72, 720, f"- Dificultad: {ejercicio['dificultad']}")

        c.save()
        print(f"La rutina ha sido guardada en {file}")

    def mostrarMensaje(self):
        messagebox.showinfo("Atención Medica", "Acercate a un centro medico para obtener ayuda.")

    def mostrarDetalle(self, ejercicio):
        self.label_ejercicio.config(text=f"Ejercicio: {ejercicio['nombre']}")
        self.label_categoria.config(text=f"Categoria: {ejercicio['categoria']}")
        self.label_dificultad.config(text=f"Dificultad: {ejercicio['dificultad']}")

    def main(self):
        self.boton1.config(command=lambda: self.mostrarEjercicio("Piernas"))
        self.boton2.config(command=lambda: self.mostrarEjercicio("Espalda"))
        self.boton3.config(command=lambda: self.mostrarEjercicio("Hombros"))

        self.ventana.mainloop()
 

ejercicios = [
    {"nombre": "Sentadillas", "categoria": "Fuerza", "dificultad": "Intermedio", "dolor_relacionado": "Piernas"},
    {"nombre": "Estiramiento de espalda baja", "categoria": "Movilidad", "dificultad": "Facil", "dolor_relacionado": "Espalda"},
    {"nombre": "Rotacion de hombros", "categoria": "Movilidad", "dificultad": "Facil", "dolor_relacionado": "Hombros"},
    {"nombre": "Extensión de pierna", "categoria": "Movilidad", "dificultad": "Facil", "dolor_relacionado": "Piernas"}
]

generador = GeneradorRutinas(ejercicios)
generador.main()