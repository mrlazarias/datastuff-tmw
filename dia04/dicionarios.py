# %%

dados = {"nome":"Murilo",
         "sobrenome":"Azarias",
         "idade":27,
         "ex": ["Nah", "Josefina", "Elaine"],
         "filhos":[{"nome":"Maria", "idade":2}, {"nome":"Murilo", "idade":27}]
         }

nome = dados['nome']

print(nome)

print(dados["filhos"][0]["idade"])

# %%

dados.keys()

# %%

dados.values()
# %%

dados.items()
# %%
