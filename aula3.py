def eh_primo(n):
    cont = 1
    x = []
    while cont < n: 
        if n % cont == 0:
            x.append(cont)
        cont = cont + 1

    cont = 0
    soma = 0
    while cont < len(x):
        soma = soma + x[cont]
        cont = cont + 1

    if soma == n:
        return True
    else:
        return False  


def lista_perfeitos(n):
    x2 = []
    for i in range(1, n):
        if eh_primo(i):
            x2.append(i)
    return x2       


print(lista_perfeitos(28))
