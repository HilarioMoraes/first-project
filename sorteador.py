import random

# Sorteia um nome de uma lista fornecida pelo usuário
nomes = input("Digite os nomes separados por vírgula: ").split(",")
escolhido = random.choice(nomes)

print(f"O nome sorteado foi: {escolhido.strip()}")
