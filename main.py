from driver_manager import DriverManager
from titulo_extractor import TituloExtractor
from preco_extractor import PrecoExtractor
from disponibilidade_extractor import DisponibilidadeExtractor


def main():
    # Inicializa o gerenciador de driver
    driver_manager = DriverManager()
    driver = driver_manager.iniciar_driver()

    try:
        # URL com datas e 1 adulto
        url = "https://www.airbnb.com.br/rooms/1131434074821709093?check_in=2025-06-01&check_out=2025-06-05&adults=1"
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

    finally:
        # Garante que o driver será encerrado
        driver_manager.encerrar_driver()


if __name__ == "__main__":
    main()
