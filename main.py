
from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

app = FastAPI(
    title="Exemplo de Automação com Selenium e FastAPI",
    description="Uma aplicação simples que utiliza Selenium para automatizar buscas na web.",
    version="1.0.0"
)

# Configurações do Chrome

chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa o Chrome em modo headless
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Incializa o WebDriver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


@app.get("/search")
def search_duckduckgo(query: str):
    # Abrir o DuckDuckGo
    driver.get("https://duckduckgo.com")

    # Encontrar a barra de pesquisa
    search_box = driver.find_element(By.NAME, 'q')

    # Digitar a consulta e enviar
    search_box.send_keys(query)
    search_box.submit()

    # Aguardar os resultados carregarem
    time.sleep(3)

    # Capturar os títulos dos resultados
    titles = driver.find_elements(By.TAG_NAME, 'h3')
    results = [title.text for title in titles]

    # Fechar o navegador
    driver.quit()

    return {"query": query, "results": results}
