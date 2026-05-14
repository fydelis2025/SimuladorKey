import platform
import socket
import getpass

def coletar_dados():
    print("Simulação de coleta de dados (ambiente educativo)\n")

    dados = {
        "usuario": getpass.getuser(),
        "sistema": platform.system(),
        "versao": platform.version(),
        "hostname": socket.gethostname(),
        "ip_local": socket.gethostbyname(socket.gethostname())
    }

    return dados

def salvar_dados(dados):
    with open("dados_coletados.txt", "w") as arquivo:
        for chave, valor in dados.items():
            arquivo.write(f"{chave}: {valor}\n")

def main():
    print("Este script é apenas para fins educacionais.")
    consentimento = input("Deseja continuar? (s/n): ")

    if consentimento.lower() == "s":
        dados = coletar_dados()
        salvar_dados(dados)
        print("Dados coletados e salvos com sucesso.")
    else:
        print("Operação cancelada.")

if __name__ == "__main__":
    main()