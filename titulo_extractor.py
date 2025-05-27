from selenium.webdriver.common.by import By


class TituloExtractor:
    """Classe para extrair o título do anúncio do Airbnb."""

    def __init__(self, driver):
        """
        Inicializa o extrator.

        Args:
            driver: WebDriver do Selenium
        """
        self.driver = driver

    def extrair_titulo(self):
        """
        Extrai o título do anúncio.

        Returns:
            str: Título do anúncio
        """
        try:
            titulo = self.driver.find_element(By.TAG_NAME, "h1").text.strip()
            return titulo
        except:
            return "⚠️ Título não encontrado"
