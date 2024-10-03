from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from DBConnection import getAllDocuments, addDocument, deleteAllDocuments

def paisValido(pais):
    if (pais == "SUD" or pais == "ECUA" or pais == "COL" or pais == "PE" or pais == "AR" or pais == "CH" or pais == "BRA" or pais == "URU" or pais == "AFCCHA" or pais =="IT" or pais == "ENG"):
        return True
    else:
        return False

# Configurar opciones de Chrome para que funcione en modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Modo headless
chrome_options.add_argument("--no-sandbox")  # Necesario para algunos entornos
chrome_options.add_argument("--disable-dev-shm-usage")  # Evitar problemas de memoria
chrome_options.add_argument("--disable-gpu")  # Desactivar GPU para evitar problemas
chrome_options.add_argument("--window-size=1920x1080")  # Establecer un tamaño de ventana


# Inicializar el navegador
driver = webdriver.Chrome(options=chrome_options)

try:

    deleteAllDocuments()

    # Navegar a la página
    driver.get("https://pelotalibre.org/")

    partidos_destacados = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/article/div/h1")  
    iframe = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/article/div/iframe')

    # Cambia el contexto de Selenium al iframe
    driver.switch_to.frame(iframe)

    contenedorPartidos = driver.find_element(By.CLASS_NAME, "menu")
    lista_LI_contenedores = contenedorPartidos.find_elements(By.TAG_NAME, "li")

    contadorPartido = 1

    for contenedorListaDeEnlaces in lista_LI_contenedores:

        opcion = contenedorListaDeEnlaces.get_attribute("class")

        if(paisValido(opcion)):

            contendorEnlace = contenedorListaDeEnlaces.find_element(By.TAG_NAME, "ul")
            listaEnlaces = contendorEnlace.find_elements(By.TAG_NAME, "li")

            print(f"------------------------------------------------- PARTIDO NUMERO {contadorPartido} -------------------------------------------------\n")

            contadorEnlace = 1

            urlPartidos = []
            programasTransmision = []

            for enlace in listaEnlaces:

                url = enlace.find_element(By.TAG_NAME, "a")
                urlPartido = url.get_attribute("href")
                descripcionPartido = contenedorListaDeEnlaces.find_element(By.TAG_NAME, "a").text

                programa = url.get_attribute("textContent")

                # Agrego en la base de datos.

                urlPartidos.append(urlPartido)
                programasTransmision.append(programa)

                # Muestro los valores.
                print(f"-------------------------- Enlace numero {contadorEnlace} ---------------------------\n")
                print(f"#Partido: {descripcionPartido}\n#Enlace: {urlPartido}\n#Sitio: {programa}\n")
                print(f"-------------------------------------------------------------------------------------\n")
                contadorEnlace = contadorEnlace + 1
            
            if (len(urlPartidos) != 0):
                addDocument(f"{descripcionPartido}", {"URLs": urlPartidos, "Programas": programasTransmision, "Categoria": opcion})

            contadorPartido = contadorPartido + 1

    # Volver al contenido principal
    driver.switch_to.default_content()

finally:
    # Cerrar el navegador
    driver.quit()
