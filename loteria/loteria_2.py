numero_sorte = 7

for i in range(3):

    while True:
        try:
            numero = int(input("Entre com um numero entre 1 e 15: "))
            break

        except ValueError:
            print("O animal eu pedi um numero")


    if numero == numero_sorte:
     print("Voce acertou")
     break
    elif numero > numero_sorte:
     print("Voce errou tente! um numero menor!")
    else:
     print("voce errou! tente um numero maior!")

# %%

try:
    numero = int(input("Entre com um numero: "))

except ValueError as err:
  print("Mano, tu é burro? pedi um numero")


# %%
