# %%

minha_lista = []
print(minha_lista)



# %%

minha_lista = ['murilo', 'azarias', 27, 1.76]
print(minha_lista)

# %%

# Primeiro elemento:
minha_lista[0]

# Segundo elemento
minha_lista[1]

# Ultimo elemento
minha_lista[-1]# %%

# %%

# Slice start:stop:step

minha_lista[:2]

# %%

minha_lista[-2:]

# %%

nova_lista = minha_lista[:]
print(nova_lista)


# %%

minha_lista[::-1] # Inversao da lista

# %%

minha_lista[::2]

# %%

notas = []
nota = 7.75

notas.append(nota)
print(notas)

notas.append(10)
print(notas)

notas.extend([5.75, 6.24])
print(notas)

notas = notas + [10, 9.25]
print(notas)
# %%
notas.remove(10)
print(notas)

# %%

nome = 'Murilo'
nome_alto = nome.upper()

print(nome_alto)

# %%

nomes = ['murilo', 'azarias', 'araujo']
for nome in nomes:
    print( nome.title() )

nomes.extend(['Manuela'])
print(nomes)
# %%

dados = ['Murilo', 'Azarias', 27, ['Manuela', 'Dorta', 'Beloni', ['Isaac']]]

dados[3][-1]

# %%
dados[-1][0][0]

# %%
