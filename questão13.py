salario = float(input("Insira o salário inícial: "))
qtd_anos = int(input("Insira a quantidade de anos: "))


for i in range (qtd_anos):
    salario_atual = (salario*2)*qtd_anos
    print(f"O salário vai ser: {salario_atual}")
