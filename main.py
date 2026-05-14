from coletor import coletar_dados
from monitor import verificar_arquivos_suspeitos
from relatorio import gerar_relatorio
from utils import mostrar_banner

def main():
    mostrar_banner()

    print("Este sistema é apenas para fins educacionais.\n")
    consentimento = input("Deseja iniciar a simulação? (s/n): ")

    if consentimento.lower() != "s":
        print("Operação cancelada.")
        return

    print("\nColetando dados...")
    dados = coletar_dados()

    print("Monitorando atividades...")
    suspeitos = verificar_arquivos_suspeitos()

    print("Gerando relatório...")
    gerar_relatorio(dados, suspeitos)

    print("\n✔ Simulação concluída. Verifique a pasta 'logs'.")

if __name__ == "__main__":
    main()