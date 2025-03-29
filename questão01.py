n1 = float(input("Insira a primeira nota"))
n2 = float(input("Insira a segunda nota"))
n3 = float(input("Insira a terceira nota"))

media_ari = (n1+n2+n3)/3
media_pon1 = ((n1*2)+(n2*2)+(n3*3))/7
media_pon2 = (n1+(n2*2)+(n3*2))/5

print(f"A média aritmética dos números foi {media_ari}, média ponderada com os pesos 2, 2 e 3 é {media_pon1} e média ponderada com os pesos 1, 2, 2 é {media_pon2}")
