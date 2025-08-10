import random
import string

# Gera uma senha simples
tamanho = int(input("Digite o tamanho da senha: "))

caracteres = string.ascii_letters + string.digits
senha = "".join(random.choice(caracteres) for i in range(tamanho))

print(f"Sua senha gerada é: {senha}")
