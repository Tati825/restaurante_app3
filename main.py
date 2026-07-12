from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

#Se crea el menú como se indica
def mostrar_menu():
    print("\n========================================")
    print("          SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")


def main():
    #Se crea el restaurante
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        #Se realiza el registro del producto
        if opcion == "1":
            try:
                print("\n--- Registrar Producto ---")

                nombre = input("Ingrese el nombre del producto: ")
                categoria = input("Ingrese la categoría del producto: ")
                precio = float(input("Ingrese el precio del producto: "))

                respuesta = input(
                    "¿El producto está disponible? (s/n): "
                ).lower()

                disponible = respuesta == "s"

                producto = Producto(
                    nombre,
                    categoria,
                    precio,
                    disponible
                )
                restaurante.registrar_producto(producto)

            except ValueError as error:
                print(f"Error: {error}")

        #Se enlistan los productos
        elif opcion == "2":
            restaurante.listar_productos()

        #Se busca un producto por su nombre
        elif opcion == "3":
            nombre = input(
                "Ingrese el nombre del producto a buscar: "
            )

            producto = restaurante.buscar_producto(nombre)

            if producto:
                print("\nProducto encontrado:")
                print(producto.mostrar_informacion())
            else:
                print("Producto no encontrado")

        #Se realiza el registro de un cliente
        elif opcion == "4":
            try:
                print("\n--- Registro de Cliente ---")

                nombre = input("Ingrese el nombre del cliente: ")
                correo = input("Ingrese el correo del cliente: ")
                id_cliente = int(input("Ingrese el ID del cliente: "))

                cliente = Cliente(
                    nombre,
                    correo,
                    id_cliente
                )
                restaurante.registrar_cliente(cliente)

            except ValueError:
                print("Error: El ID debe ser un número entero")

        #Se enlistan los clientes
        elif opcion == "5":
            restaurante.listar_clientes()

        #Se busca un cliente por su ID
        elif opcion == "6":
            try:
                id_cliente = int(
                    input("Ingrese el ID del cliente a buscar: ")
                )
                cliente = restaurante.buscar_cliente(id_cliente)

                if cliente:
                    print("\nCliente encontrado: ")
                    print(f"ID: {cliente.id_cliente}")
                    print(f"Nombre: {cliente.nombre}")
                    print(f"Correo: {cliente.correo}")
                else:
                    print("Cliente no encontrado")

            except ValueError:
                print("Error: El ID debe ser un número entero")

        #La opción para salir del programa
        elif opcion == "7":
            print("Está saliendo del sistema")
            break

        #Mensaje a opción incorrecta
        else:
            print("Opción incorrecta, debe escoger un número entre 1 y 7")


if __name__ == "__main__":
    main()
