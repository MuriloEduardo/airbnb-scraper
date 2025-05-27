from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class DriverManager:
    """Gerencia o WebDriver do Selenium."""

    def __init__(self):
        """Inicializa o driver do Selenium."""
        self.driver = None

    def iniciar_driver(self):
        """Inicia o driver do Chrome."""
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        return self.driver

    def carregar_url(self, url):
        """Carrega uma URL e aguarda o carregamento completo."""
        if not self.driver:
            self.iniciar_driver()

        self.driver.get(url)

        # Aguarda o carregamento de algum conteúdo
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "span"))
        )
        time.sleep(6)  # Garantir que tudo tenha carregado

    def encerrar_driver(self):
        """Encerra o driver do Selenium."""
        if self.driver:
            self.driver.quit()
            self.driver = None
