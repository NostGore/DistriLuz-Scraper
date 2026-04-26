import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://servicios.distriluz.com.pe/OficinaVirtualConsulta/Consultas/Consultas/ConsultaMiRecibo"

tipo = input("1: Suministro | 2: DNI -> ").strip()
while tipo not in ("1", "2"):
    tipo = input("Seleccione una opción valida: ").strip()

valor = input("Número: ").strip()

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

try:
    driver.get(URL)

    select = wait.until(EC.presence_of_element_located((By.ID, "cmbType")))
    for o in select.find_elements(By.TAG_NAME, "option"):
        if o.get_attribute("value") == tipo:
            o.click()
            break

    driver.find_element(By.ID, "txtIdNroServicio").send_keys(valor)
    driver.find_element(By.ID, "btnSearch").click()

    img = wait.until(EC.presence_of_element_located((By.ID, "imgRecibo")))
    wait.until(lambda d: "base64" in img.get_attribute("src"))

    src = img.get_attribute("src")

    if "base64," not in src:
        print("No se encontró el recibo")
    else:
        data = base64.b64decode(src.split("base64,")[1])
        with open(f"recibo-de-luz-{valor}.png", "wb") as f:
            f.write(data)
        print("Archivo guardado")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()