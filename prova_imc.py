nome = input("Digite o nome do aluno: ")
peso = float(input("digite o peso do aluno "))
altura = float(input("digite a altura do aluno "))
imc = peso / altura ** 2

print(f"\nAluno: {nome}")
print(f"imc: {imc:.2f}")
if imc < 18.5:
    print("situação: Abaixo do peso ⚖️")
elif imc < 24.9:
    print("situação: Peso normal 💪")
elif imc < 29.9:
    print("situação: Sobrepeso 🍔")
elif imc < 34.9:
    print("situação: Obesidade Grau I 🔴")
elif imc < 39.9:
    print("situação: Obesidade Grau II 🔴")
else:
    print("situação: Cuidado com a Saúde, obesidade grau III ⚠️")       