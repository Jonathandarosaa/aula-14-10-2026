print("--- CALCULADORA DE MÉDIA (GRAVAÇÃO) ---")
med2 = float(input("Qual a nota do exame: "))
with open("exame.txt", "r") as arquivo:
    name = arquivo.readline().strip()
    med = float(arquivo.readline().strip())
media = round((med+med2)/2, 1)
if media >= 5:
    with open("Aprovado.txt", "a") as aprovado:
        aprovado.write(f"{name}\n")
        aprovado.write(f"{media}\n")
else:
    with open("reprovados.txt", "a") as reprovado:
        reprovado.write(f"{name} - Reprovado após exame\n")
        reprovado.write(f"{media}\n")