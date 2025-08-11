# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)

tipo_sorvete = input("Entre com o tipo do sorvete: [casquinha/cascão/cestinha] ")
sabor = input("Entre com o sabor do sorvete: [morango/creme/chocolate] ")
cobertura = input("Entre com a cobertura do sorvete: [caramelo/morango/chocolate/sem cobertura]" )

valor = 0

# Essa parte é do tipo de sorvete

if tipo_sorvete == 'casquinha':
    valor  = valor + 1

elif tipo_sorvete == 'cascao':
    valor += 2.50 ## Quando voce ver um += significa que voce esta pegando o proprio valor daquela variavel, somando alguma coisa nela e reatribuindo

elif tipo_sorvete == 'cestinha':
    valor += 4.00

else:
    print('Seu pedido vai vir cagado, escolha corretamente')

# Essa parte é da cobertura

coberturas = 'caramelo,morango,chocolate'

if cobertura in coberturas:
    valor += 1.5

elif cobertura == '':
    pass

else:
    print('Seu pedido vira cagado, entre com uma cobertura válida')

print(" Seu sorvete ", tipo_sorvete, " de ", sabor, "cobertura", cobertura, " custara: R$ ", valor, sep="")

