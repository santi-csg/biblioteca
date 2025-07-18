# Clase base que representa una persona con nombre e identificación
class Persona:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
    # Método que retorna una descripción básica de la persona
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, ID: {self.identificacion}"
    
# Cliente hereda de Persona
class Cliente(Persona):
    def __init__(self, nombre, identificacion, categoria):
        super().__init__(nombre, identificacion)
        self.categoria = categoria
    # Metodo para incluir la categori del cliente
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Categoría: {self.categoria}"
    
# Empleado tambien hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, identificacion, cargo):
        super().__init__(nombre, identificacion)
        self.cargo = cargo
    # Metodo para incluir el cargo del empleado
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Cargo: {self.cargo}"
    
# Clase que representa un libro con título, autor y disponibilidad
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
    # Muestra información del libro junto a su estado (disponible o prestado)
    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({estado})"
    
# Clase que representa un préstamo entre un libro y una persona
class Prestamo:
    def __init__(self, libro, persona):
        self.libro = libro
        self.persona = persona
        self.realizar_prestamo()
    # Cambia el estado del libro a prestado si está disponible
    def realizar_prestamo(self):
        if self.libro.disponible:
            self.libro.disponible = False
        else:
            print("El libro no está disponible")
     # Muestra quién tiene qué libro en préstamo
    def mostrar_detalle(self):
        return f"{self.persona.nombre} tiene en préstamo el libro '{self.libro.titulo}'"
# Clase principal que gestiona los libros, personas y préstamos
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.personas = []
        self.prestamos = []
    # Agrega un libro a la lista de libros disponibles
    def agregar_libro(self, libro):
        self.libros.append(libro)
    # Agrega una persona (cliente o empleado) al sistema
    def agregar_persona(self, persona):
        self.personas.append(persona)
    # Registra un préstamo entre una persona y un libro
    def prestar_libro(self, libro, persona):
        prestamo = Prestamo(libro, persona)
        self.prestamos.append(prestamo)
# Ejecución del sistema con un ejemplo práctico
biblio = Biblioteca()
libro1 = Libro("1984", "George Orwell")
cliente1 = Cliente("Santiago", "123", "Estudiante")

biblio.agregar_libro(libro1)
biblio.agregar_persona(cliente1)
biblio.prestar_libro(libro1, cliente1)

for p in biblio.prestamos:
    print(p.mostrar_detalle())
