# CH, de Christian. R, de Ruiz. F, de Fonseca.

# par(n) -------------> Devuelve 1 si es primo, 0 si no.
# primo(n) -----------> Devuelve 1 si n es primo, 0 si no.
# mult_list(lista) ---> Multiplica todos los elementos de la lista y devuelve un número.
# r_cuadrada_de(n) ---> Devuelve la raíz cuadrada de n.
# f_prim_de(n) -------> Devuelve una lista con los factores primos de n. Si no se puede factorizar devuelve un errror.
# a_de_un_c(r) -------> Devuelve el área de un circulo de radio r.
# sum_vec(v1, v2) ----> Suma dos vectores y devuelve una lista.
# mul_vec(v1, v2) ----> Multiplica dos vectores y devuelve un número.

def par(n):
    if n % 2 == 0:
        par = 1
    else:
        par = 0
    return par


def primo(n):
    primo = 0
    if (n > 1) and (n != 2):
        for i in range(2, n):
            if n % i == 0:
                primo = 0
                break
            else:
                primo = 1
    else:
        if n == 2:
            primo = 1
        else:
            primo = 0
    return primo

def mult_list(lista):
    r = 1
    for n in lista:
         r = r * n
    return r

def r_cuadrada_de(n):
  if n < 0:
    return "Error. No es posible obtener la raíz cuadrada."
  else:
    return n**0.5

def f_prim_de(n):
    f_primos = []
    if n > 1:
        while n % 2 == 0:
            f_primos.append(2)
            n = n / 2
        for i in range(3, int(r_cuadrada_de(n)) + 1, 2):
            while n % i == 0:
                f_primos.append(int(i))
                n = n / i
        if n > 2:
            f_primos.append(int(n))
        return f_primos
    else:
        return "Error. No es posible factorizar."

def a_de_un_c(r, red):
    if red != 1:
        return 3.1415926535897932384*r*r
    else:
        return round(3.1415926535897932384*r*r)

def sum_vec(v1, v2):
    vR = []
    for i in range(0, len(v1)):
        vR.append(v1[i] + v2[i])
    return str(vR)

def mul_vec(v1, v2):
    vR = []
    for i in range(0, len(v1)):
        vR.append(v1[i] * v2[i])
    return sum(vR)
