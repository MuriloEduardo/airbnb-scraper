import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configura o navegador Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL com datas e 1 adulto
url = "https://www.airbnb.com.br/rooms/1131434074821709093?check_in=2025-06-01&check_out=2025-06-05&adults=1"
driver.get(url)

# Aguarda o carregamento de algum conteúdo
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "span")))
time.sleep(6)  # Garantir que tudo tenha carregado

# 🔠 Título do anúncio
try:
    titulo = driver.find_element(By.TAG_NAME, "h1").text.strip()
except:
    titulo = "⚠️ Título não encontrado"

# 💸 Busca spans com "R$"
spans = driver.find_elements(By.XPATH, "//span[contains(text(),'R$')]")
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

# ❌ Disponibilidade
indisponivel = driver.find_elements(By.XPATH, "//*[contains(text(),'indisponível')]")

print(f"🏡 Título do anúncio: {titulo}")

if preco_total:
    print(f"💰 Valor total: {preco_total}")
else:
    print("⚠️ Preço não encontrado.")

if indisponivel:
    print("❌ Imóvel indisponível nas datas selecionadas.")
else:
    print("✅ Imóvel disponível nas datas selecionadas.")

driver.quit()
