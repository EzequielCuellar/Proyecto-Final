import sqlite3
import os

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR_ENABLED = True
except ImportError:
    COLOR_ENABLED = False


def c(text, color):
    if COLOR_ENABLED:
        return f"{color}{text}{Style.RESET_ALL}"
    return text

# -------------------------------
# INICIALIZACIÓN DE BASE DE DATOS
# -------------------------------

def inicializar_db():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """)
    conn.commit()
    conn.close()

# -------------------------------
# FUNCIONES PRINCIPALES
# -------------------------------

def registrar_producto():
    print(c("\nRegistrar nuevo producto", Fore.GREEN))
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    categoria = input("Categoría: ")

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, descripcion, cantidad, precio, categoria))
    conn.commit()
    conn.close()
    print(c("Producto registrado con éxito.", Fore.CYAN))

def ver_productos():
    print(c("\nLista de productos", Fore.GREEN))
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    
    if not productos:
        print("No hay productos registrados.")
        return

    for prod in productos:
        print(f"ID: {prod[0]} | Nombre: {prod[1]} | Cantidad: {prod[3]} | Precio: ${prod[4]:.2f} | Categoría: {prod[5]}")
        print(f"Descripción: {prod[2]}")
        print("-" * 50)

def buscar_producto():
    print(c("\nBuscar producto por ID", Fore.GREEN))
    id = input("Ingrese el ID del producto: ")
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    producto = cursor.fetchone()
    conn.close()
    if producto:
        print(f"ID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[3]} | Precio: ${producto[4]:.2f}")
        print(f"Descripción: {producto[2]} | Categoría: {producto[5]}")
    else:
        print(c("Producto no encontrado.", Fore.RED))

def actualizar_producto():
    print(c("\nActualizar producto", Fore.GREEN))
    id = input("Ingrese el ID del producto a actualizar: ")
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    producto = cursor.fetchone()

    if not producto:
        print(c("Producto no encontrado.", Fore.RED))
        conn.close()
        return

    print("Deje vacío un campo si se quiere modificarlo.")
    nombre = input(f"Nombre ({producto[1]}): ") or producto[1]
    descripcion = input(f"Descripción ({producto[2]}): ") or producto[2]
    cantidad = input(f"Cantidad ({producto[3]}): ")
    precio = input(f"Precio ({producto[4]}): ")
    categoria = input(f"Categoría ({producto[5]}): ") or producto[5]

    cantidad = int(cantidad) if cantidad else producto[3]
    precio = float(precio) if precio else producto[4]

    cursor.execute("""
        UPDATE productos
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?
    """, (nombre, descripcion, cantidad, precio, categoria, id))
    conn.commit()
    conn.close()
    print(c("Producto actualizado con éxito.", Fore.CYAN))

def eliminar_producto():
    print(c("\nEliminar producto", Fore.GREEN))
    id = input("Ingrese el ID del producto a eliminar: ")
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    if cursor.rowcount == 0:
        print(c("Producto no encontrado.", Fore.RED))
    else:
        print(c("Producto eliminado correctamente.", Fore.CYAN))
    conn.commit()
    conn.close()

def reporte_cantidad_baja():
    print(c("\nReporte de productos con stock bajo", Fore.GREEN))
    limite = int(input("Ingrese el límite mínimo de stock: "))
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()
    conn.close()

    if not productos:
        print("No hay productos con stock bajo.")
    else:
        for prod in productos:
            print(f"ID: {prod[0]} | Nombre: {prod[1]} | Cantidad: {prod[3]}")

# -------------------------------
# INTERFAZ
# -------------------------------

def menu():
    while True:
        print(c("\n=== SISTEMA DE INVENTARIO ===", Fore.YELLOW))
        print("1. Registrar producto")
        print("2. Ver productos")
        print("3. Buscar producto por ID")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Reporte por stock mínimo")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            buscar_producto()
        elif opcion == '4':
            actualizar_producto()
        elif opcion == '5':
            eliminar_producto()
        elif opcion == '6':
            reporte_cantidad_baja()
        elif opcion == '7':
            print(c("¡Hasta luego!", Fore.MAGENTA))
            break
        else:
            print(c("Opción inválida. Intente nuevamente.", Fore.RED))

# -------------------------------
# Labura
# -------------------------------

if __name__ == "__main__":
    inicializar_db()
    menu()
