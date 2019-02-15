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


numero = int(input("Informe um numero: "))
y = eh_primo(numero)

if y:
    print("È perfeito")
else:
    print("Não é perfeito")
