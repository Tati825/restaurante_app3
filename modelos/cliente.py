from dataclasses import dataclass

#Uso del decorador para generar los métodos de forma automática
@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: int
