# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)

tipo_sorvete = input("Entre com o tipo do sorvete: [casquinha/cascão/cestinha] ").lower()
sabor = input("Entre com o sabor do sorvete: [morango/creme/chocolate] ").lower()
cobertura = input("Entre com a cobertura do sorvete: [caramelo/morango/chocolate/sem cobertura]" ).lower()


sorvetes = {
    'casquinha': 1.00,
    'cascão': 2.5,
    'cestinha': 4.00
}

valor = 0

if tipo_sorvete in sorvetes:
    valor += sorvetes[tipo_sorvete]
else:
    print("Seu pedido vai vir cagado. Entre com um valor válido!")

# Essa parte é da cobertura

coberturas = {
    'caramelo': 1.50,
    'morango': 1.50,
    'chocolate': 1.50,
    "": 0
}

if cobertura in coberturas:
    valor += coberturas[cobertura]
else:
        print("Seu pedido vai vir cagado. Entre com um valor válido!")


print(" Seu sorvete ", tipo_sorvete, " de ", sabor, "cobertura", cobertura, " custara: R$ ", valor, sep="")

