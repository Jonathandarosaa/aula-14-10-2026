print("--- ALUNOS APROVADOS ---")
with open("aprovado.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(f"{linha.strip()}")

print("\n--- ALUNOS REPROVADOS ---")
with open("reprovados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(f"{linha.strip()}")