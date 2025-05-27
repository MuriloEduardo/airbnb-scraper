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
        # Verifica diferentes mensagens de indisponibilidade que podem aparecer
        xpath_query = (
            "//*[contains(text(),'indisponível') or "
            "contains(text(),'Essas datas não estão disponíveis') or "
            "contains(text(),'não estão disponíveis')]"
        )
        
        indisponivel = self.driver.find_elements(By.XPATH, xpath_query)
        
        # Salvar a mensagem encontrada para debug e exibição
        self.mensagem_indisponivel = None
        if indisponivel:
            self.mensagem_indisponivel = indisponivel[0].text.strip()
            
        # Se não encontrou nenhuma das mensagens, está disponível
        return len(indisponivel) == 0
