def verificar_primo(numero):
    if numero <= 1:
        return "não primo"
    if numero == 2:
        return "primo"
    if numero % 2 == 0:
        return "não primo"
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return "não primo"
    return "primo"

# Recebe um número inteiro positivo do usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é primo e imprime o resultado
resultado = verificar_primo(numero)
print(resultado)