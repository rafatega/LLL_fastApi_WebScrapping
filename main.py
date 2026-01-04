from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


# Configurações do Chrome

chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa o Chrome em modo headless
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Incializa o WebDriver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abrir o DuckDuckGo
driver.get("https://duckduckgo.com")

# Encontrar a barra de pesquisa
search_box = driver.find_element(By.NAME, 'q')

# Digitar a consulta e enviar
search_query = 'Venezuela'
search_box.send_keys(search_query)
search_box.submit()

# Aguardar os resultados carregarem
time.sleep(3)

# Capturar os títulos dos resultados
titles = driver.find_elements(By.TAG_NAME, 'h3')
print(f"Resultados para a pesquisa: '{search_query}'\n")
for idx, title in enumerate(titles, start=1):
    print(f"{idx}. {title.text}")

# Fechar o navegador
driver.quit()
