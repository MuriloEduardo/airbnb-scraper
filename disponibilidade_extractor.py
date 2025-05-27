from selenium.webdriver.common.by import By


class DisponibilidadeExtractor:
    """Classe para verificar a disponibilidade do anúncio do Airbnb."""

    def __init__(self, driver):
        """
        Inicializa o extrator.

        Args:
            driver: WebDriver do Selenium
        """
        self.driver = driver

    def verificar_disponibilidade(self):
        """
        Verifica se o imóvel está disponível nas datas selecionadas.

        Returns:
            bool: True se disponível, False se indisponível
        """
        indisponivel = self.driver.find_elements(
            By.XPATH, "//*[contains(text(),'indisponível')]"
        )

        # Se não encontrou mensagem de indisponível, está disponível
        return len(indisponivel) == 0
