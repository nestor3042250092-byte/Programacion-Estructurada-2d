'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones
'''

num = int(input("Ingresa un número para la tabla (Sin estructuras): "))

print(num, "x 1 =", num * 1)
print(num, "x 2 =", num * 2)
print(num, "x 3 =", num * 3)
print(num, "x 4 =", num * 4)
print(num, "x 5 =", num * 5)
print(num, "x 6 =", num * 6)
print(num, "x 7 =", num * 7)
print(num, "x 8 =", num * 8)
print(num, "x 9 =", num * 9)
print(num, "x 10 =", num * 10)


'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control
  2.- Sin funciones
'''

print("\033c") # Limpia la pantalla en algunas terminales

num_tabla = int(input("Numero de la tabla de multiplicar (Con estructuras): "))

print("\n--- Resultado con ciclo FOR ---")
for num in range(1, 11):
    multi = num_tabla * num
    print(f"{num_tabla} x {num} = {multi}")


print("\n--- Resultado con ciclo WHILE ---")
num = 1
while num < 11:
    multi = num_tabla * num
    print(f"{num_tabla} x {num} = {multi}")
    num += 1