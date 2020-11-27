import chrf

a = int(input("Bienvenido. Dame por favor un número mayor que uno y que esté entero. "))
print("Se va a factorizar ", a, " en primos. ")
b = chrf.f_prim_de(a)
print("Los factores primos de ", a, " son ", b)
print("El producto de la multiplicación de los factores primos de ", a, " es ", chrf.mult_list(b))
