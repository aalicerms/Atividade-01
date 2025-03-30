num = int(input("Insira um número impar: "))


num_anterior = num - 2
num_posterior = num + 2


diferenca = (num_anterior)**2 - (num_posterior)**2


print(f"A diferença entre os quadrados do número anterios e posterior é {diferenca}")
