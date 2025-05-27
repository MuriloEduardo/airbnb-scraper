import argparse
from driver_manager import DriverManager
from titulo_extractor import TituloExtractor
from preco_extractor import PrecoExtractor
from disponibilidade_extractor import DisponibilidadeExtractor


def main():
    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(description='Verificador de disponibilidade do Airbnb')
    parser.add_argument('--id', required=True, help='ID do quarto no Airbnb')
    parser.add_argument('--check_in', required=True, help='Data de check-in (YYYY-MM-DD)')
    parser.add_argument('--check_out', required=True, help='Data de check-out (YYYY-MM-DD)')
    parser.add_argument('--adults', default=1, type=int, help='Número de adultos (padrão: 1)')
    args = parser.parse_args()

    # Inicializa o gerenciador de driver
    driver_manager = DriverManager()
    driver = driver_manager.iniciar_driver()

    try:
        # URL com os parâmetros fornecidos via linha de comando
        url = f"https://www.airbnb.com.br/rooms/{args.id}?check_in={args.check_in}&check_out={args.check_out}&adults={args.adults}"
        print(f"🔗 URL: {url}")
        driver_manager.carregar_url(url)

        # Extrai as informações usando as classes especializadas
        titulo_extractor = TituloExtractor(driver)
        preco_extractor = PrecoExtractor(driver)
        disponibilidade_extractor = DisponibilidadeExtractor(driver)

        # Obtém as informações
        titulo = titulo_extractor.extrair_titulo()
        preco_total = preco_extractor.extrair_preco_total()
        disponivel = disponibilidade_extractor.verificar_disponibilidade()

        # Exibe os resultados
        print(f"🏡 Título do anúncio: {titulo}")

        if preco_total:
            print(f"💰 Valor total: {preco_total}")
        else:
            print("⚠️ Preço não encontrado.")

        if disponivel:
            print("✅ Imóvel disponível nas datas selecionadas.")
        else:
            print("❌ Imóvel indisponível nas datas selecionadas.")
            # Se tiver uma mensagem específica, mostre-a
            if (hasattr(disponibilidade_extractor, 'mensagem_indisponivel') and
                    disponibilidade_extractor.mensagem_indisponivel):
                motivo = disponibilidade_extractor.mensagem_indisponivel
                print(f"📝 Motivo: {motivo}")

    finally:
        # Garante que o driver será encerrado
        driver_manager.encerrar_driver()


# Exemplo de uso:
# python main.py --id 769729843373520689 --check_in 2025-06-01 --check_out 2025-06-08 --adults 1

if __name__ == "__main__":
    main()
