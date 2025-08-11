# Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

# %%

nome = input("Entre com o seu nome: ")
nome = nome.lower()

if 'calvo' in nome or 'silva' in nome:
    print('Voce pertence a familia calvo ou silva')
else:
    print('Nao conheço sua familia')
