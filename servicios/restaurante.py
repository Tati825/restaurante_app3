class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    #Se realiza el registro de un nuevo producto
    def registrar_producto(self, producto):
        self.productos.append(producto)
        print("Producto registrado correctamente.")

    #Se muestran los productos
    def listar_productos(self):
        if not self.productos:
            print("No existen productos registrados.")
            return

        print("\n--- Lista de Productos ---")

        for producto in self.productos:
            print(producto.mostrar_informacion())

    #Permite buscar un producto ingresando su nombre
    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto

        return None

    #Se realiza el registro de un nuevo cliente
    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print("Cliente registrado correctamente.")

    #Se muestran los clientes
    def listar_clientes(self):
        if not self.clientes:
            print("No existen clientes registrados.")
            return

        print("\n--- Lista de Clientes ---")

        for cliente in self.clientes:
            print(
                f"ID: {cliente.id_cliente} | "
                f"Nombre: {cliente.nombre} | "
                f"Correo: {cliente.correo}"
            )

    #Se busca un cliente por su ID
    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente

        return None
