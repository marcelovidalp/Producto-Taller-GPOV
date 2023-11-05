import random
from tkinter import *
from fpdf import FPDF

ejercicios = [
    {"nombre": "Sentadillas", "categoria": "Fuerza", "dificultad": "Intermedio", "dolor_relacionado": "Piernas"},
    {"nombre": "Estiramiento de espalda baja", "categoria": "Movilidad", "dificultad": "Facil", "dolor_relacionado": "Espalda"},
    {"nombre": "Rotacion de hombros", "categoria": "Movilidad", "dificultad": "facil", "dolor_relacionado": "Hombros"}
    #MAS EJERCICIOS   
]

class GeneradorRutinas:
    def __init__(self, ejercicios):
        self.ejercicios = ejercicios
        
    def generar_rutina(self, dolor):
        rutina = []
        ej_filter = [e for e in self.ejercicios if e['dolor_relacionado'] == dolor]
        if not ej_filter:
            print(f"No se encontraron ejercicios relacionados con el dolor: {dolor}")
        rutina = random.sample(ej_filter, min(3, len(ej_filter)))
        return rutina
    
    def guardar_rutina(self, rutina, file, dolor):
        with open(file, 'a') as archivo_rutina:
            archivo_rutina.write(f"\n\n############### {dolor} Ejercicio ###############\n\n")
            for ejercicio in rutina:
                archivo_rutina.write(f"- Ejercicio: {ejercicio['nombre']}\n- Categoria: {ejercicio['categoria']}\n- Dificultad: {ejercicio['dificultad']}")
        print(f"Rutina Guardada en {file}")  

    def main(self):
        ventana = Tk()
        ventana.title("Generador de Ejercicios.")

        frame1 = Frame(ventana, bg="DeepSkyBlue2", height="600", width="200")
        frame1.pack_propagate(False)
        frame1.pack(side=LEFT)

        label_dolor = Label(frame1, text="LUGAR DEL DOLOR:", font="BOLD")
        label_dolor.config(justify=LEFT)
        label_dolor.pack()

        boton1 = Button(frame1, text="Piernas.")
        boton1.place(x="10", y="50")
        boton1.pack()

        boton2 = Button(frame1, text="Espalda.")
        boton2.place(x="10", y="100")
        boton2.pack()

        boton3 = Button(frame1, text="Hombros.")
        boton3.place(x="10", y="150")
        boton3.pack()

        boton4 = Button(frame1, text="Necesito Atencion Medica.")
        boton4.place(x="10", y="200")
        boton4.pack()

        ventana.geometry("800x600")
        ventana.mainloop()
'''        
while True:
    print("\n-------------MENU PRINCIPAL----------------")
    print("1.Generar ejercicio.")
    print("2.Salir")
    opcion = int(input("Ingrese una opcion: "))
    
    if opcion == 1:
        generador = GeneradorRutinas(ejercicios)
        dolor = input("Ingrese el dolor del paciente: ")
        rutina = generador.generar_rutina(dolor)
        
        if rutina:
            print(f"\nRutina generada para el dolor: {dolor}")
            for ejercicio in rutina:
                print(f"Ejercicio: {ejercicio['nombre']}\n Categoria: {ejercicio['categoria']}\n Dificultad: {ejercicio['dificultad']}")
                print("-------------------------------------------------------")
            subopcion = input(f"\nDesea guardar la rutina? Escriba 'si' o cualquier otro caracter para volver:")
        
            if subopcion == "si":
                generador.guardar_rutina(rutina,'rutinas.txt')
        else:
            print("No se encontraron ejercicios relacionados con el dolor ingresado.")
            
    elif opcion == 2:
        print("Saliendo del programa...")
        break
    else:
        print("ERROR, DEBES INGRESAR UNA OPCION VALIDA.\n")
'''        
generador = GeneradorRutinas(ejercicios)
generador.main()