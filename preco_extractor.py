from selenium.webdriver.common.by import By


class PrecoExtractor:
    """Classe para extrair informações de preço do anúncio do Airbnb."""

    def __init__(self, driver):
        """
        Inicializa o extrator.

        Args:
            driver: WebDriver do Selenium
        """
        self.driver = driver

    def extrair_preco_total(self):
        """
        Extrai o preço total da estadia.

        Returns:
            str: Preço total formatado ou None se não encontrado
        """
        # Busca spans com "R$"
        spans = self.driver.find_elements(By.XPATH, "//span[contains(text(),'R$')]")
        preco_total = None

        # Procura o preço com informação de noites (mais completo)
        for span in spans:
            texto = span.text.strip()
            if "noite" in texto and "R$" in texto:
                preco_total = texto
                break

        # Se não encontrou preço com noites, procura outros valores
        if not preco_total:
            # No Airbnb atual, o total geralmente não tem a palavra "Total"
            for span in spans:
                texto = span.text.strip()
                if "R$" in texto and "noite" not in texto:
                    preco_total = texto
                    break

        return preco_total
