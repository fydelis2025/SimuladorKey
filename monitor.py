import os

def verificar_arquivos_suspeitos():
    arquivos_suspeitos = []

    for arquivo in os.listdir():
        if arquivo.endswith(".exe") or arquivo.endswith(".bat"):
            arquivos_suspeitos.append(arquivo)

    return arquivos_suspeitos