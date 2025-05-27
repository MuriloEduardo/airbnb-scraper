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

# Aguarda até que algum conteúdo relevante carregue
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "span")))
time.sleep(5)  # Tempo extra pro layout assentar

# Busca spans com "R$" no texto
spans = driver.find_elements(By.XPATH, "//span[contains(text(),'R$')]")

preco_por_noite = None
total_estimado = None

for span in spans:
    texto = span.text.strip()
    if "noite" in texto and not preco_por_noite:
        preco_por_noite = texto
    elif "Total" in texto or "total" in texto:
        total_estimado = texto

# Busca qualquer aviso de "indisponível"
indisponivel = driver.find_elements(By.XPATH, "//*[contains(text(),'indisponível')]")

# Exibe os resultados
print("\n✅ Resultado da consulta:\n")

if preco_por_noite:
    print(f"💰 Preço por noite: {preco_por_noite}")
else:
    print("⚠️ Preço por noite não encontrado.")

if total_estimado:
    print(f"📦 Total estimado: {total_estimado}")
else:
    print("⚠️ Total estimado não encontrado.")

if indisponivel:
    print("❌ Imóvel indisponível nas datas selecionadas.")
else:
    print("✅ Imóvel disponível nas datas selecionadas.")

driver.quit()
