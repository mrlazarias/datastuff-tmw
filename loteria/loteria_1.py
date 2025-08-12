numero = int(input("Entre com um numero entre 1 e 15: "))

numero_sorte = 7

if numero == numero_sorte:
    print("Voce acertou")
elif numero > numero_sorte:
    print("Voce errou tente! um numero menor!")
else:
    print("voce errou! tente um numero maior!")
