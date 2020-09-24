def concatenar(str1, str2):
    return str1 + str2

def repetir(str1, n):
    return str1 * n

def ambos(str1, str2, n):
    concatenada = concatenar(str1, str2)
    return repetir(concatenada, n)

str1, str2, n = input().split()
print(concatenar(str1, str2))
print(repetir(str1, int(n)))
print(ambos(str1, str2, int(n)))
