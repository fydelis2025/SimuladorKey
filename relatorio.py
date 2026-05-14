import os

def gerar_relatorio(dados, suspeitos):
    if not os.path.exists("logs"):
        os.makedirs("logs")

    with open("logs/relatorio.txt", "w") as f:
        f.write("=== RELATÓRIO DE SEGURANÇA ===\n\n")

        f.write(">> Dados do Sistema:\n")
        for k, v in dados.items():
            f.write(f"{k}: {v}\n")

        f.write("\n>> Arquivos suspeitos:\n")
        if suspeitos:
            for item in suspeitos:
                f.write(f"- {item}\n")
        else:
            f.write("Nenhum arquivo suspeito encontrado.\n")