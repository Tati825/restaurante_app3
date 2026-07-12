#Se crea la clase para poner los Productos
class Producto:
    def __init__(self, nombre, categoria, precio, disponible):
        # Se utilizan los setters para validar los datos
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    #Uso del decorador para el nombre
    @property
    def nombre(self):
        return self._nombre

    #Uso del setter para modificar el nombre
    @nombre.setter
    def nombre(self, nombre):
        if not nombre.strip():
            raise ValueError("Debe colocar un nombre")
        self._nombre = nombre

    #Uso del decorador para la categoría
    @property
    def categoria(self):
        return self._categoria

    #Uso del setter para modificar la categoría
    @categoria.setter
    def categoria(self, categoria):
        if not categoria.strip():
            raise ValueError("Debe colocar una categoría")
        self._categoria = categoria

    #Uso del decorador para el precio
    @property
    def precio(self):
        return self._precio

    #Uso del setter para modificar el precio
    @precio.setter
    def precio(self, precio):
        if precio <= 0:
            raise ValueError("El valor del precio no puede ser negativo")
        self._precio = precio

    #Uso del decorador para la disponibilidad
    @property
    def disponible(self):
        return self._disponible

    #Uso del setter para modificar la disponibilidad
    @disponible.setter
    def disponible(self, disponible):
        if not isinstance(disponible, bool):
            raise ValueError("Se debe indicar la disponibilidad por True o False")
        self._disponible = disponible

    #Se muestran los datos del Producto
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Estado: {estado}"
        )
