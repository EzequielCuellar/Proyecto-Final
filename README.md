# Proyecto-Final
----------------------------------------
Descripción del proyecto
----------------------------------------
Este sistema facilita la administración de un inventario de productos mediante Python y una base de datos SQLite. 
Es posible registrar, visualizar, buscar, actualizar y eliminar productos, así como crear un informe de productos con escaso stock. 
La comunicación se lleva a cabo a través de un menú en la consola. 
----------------------------------------

1. Abrí una terminal o consola.
2. Anda hasta la carpeta donde está el archivo `proyecto final.py`.
3. Ejecutá el siguiente comando:

    python "proyecto final.py"

----------------------------------------
Funcionalidades del menú
----------------------------------------

1. Registrar artículo:
   - Introduce el nombre, la descripción, la cantidad, el precio y la categoría. 

2.  Visualizar artículos:
   - Presenta todos los artículos que han sido registrados. 

3.  Encontrar artículo por ID:
   - Exhibe los detalles del artículo ingresando su ID. 

4.  Modificar artículo:
   - Permite cambiar uno o más campos de un artículo ya existente. 

5.  Suprimir artículo:
   - Elimina un artículo de acuerdo a su ID. 

6.  Informe de stock mínimo:
   - Muestra artículos cuya cantidad sea igual o inferior a un número ingresado. 

7.  Cerrar:
   - Termina la ejecución del programa.

----------------------------------------
Estructura de la base de datos (inventario.db)
----------------------------------------

Tabla: productos

- id: INTEGER, clave primaria, autoincremental
- nombre: TEXT, no nulo
- descripcion: TEXT
- cantidad: INTEGER, no nulo
- precio: REAL, no nulo
- categoria: TEXT

----------------------------------------
Notas finales
----------------------------------------

- Si `inventario.db` no existe, el programa lo crea automáticamente al ejecutarse.
- El programa maneja errores básicos como entradas inválidas o búsquedas sin resultados.
----------------------------------------