n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
n3 = float(input("Insira o terceiro número: "))


if n1 > n2 and n1 > n3:
    maior_nota = n1
elif n2 > n1 and n2 > n3:
    maior_nota = n2
elif n3 > n1 and n3 > n2:
    maior_nota = n3


if n1 < n2 and n1 < n3:
    menor_nota = n1
elif n2 < n1 and n2 < n3:
    menor_nota = n2
elif n3 < n1 and n3 < n2:
    menor_nota = n3


print(f"O maior número é {maior_nota} e o menor número é {menor_nota}")
