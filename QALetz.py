#Rodrigo Lara


import time
from selenium import webdriver  # Interfax oara interectuar con navegadores
from selenium.webdriver.chrome.service import Service # Inicia el controlador de chrome
from selenium.webdriver.common.by import By # Localizarmos los elementos por su identificador
from selenium.webdriver.support.ui import WebDriverWait # EL driver espera ciertas condiciones para ejecutar el codigo
from selenium.webdriver.support import expected_conditions as EC # Condiciones necesarias para utilizar WebDriverWait



# Ruta al controlador del navegador (en este caso, el de Chrome)
driver_path = 'C:\\Users\\RODRIGO\\Desktop\\chromedriver-win32\\chromedriver.exe' #Reemplazar con la ruta de tu Driver



# Inicializar el servicio del navegador
chrome_service = Service(driver_path)

# Inicializar el navegador con el servicio
driver = webdriver.Chrome(service=chrome_service)

# URL de la página con el formulario de inscripción
url = 'https://app.letz.com.co/auth/signup'
driver.get(url)

driver.maximize_window()

# Esperar hasta que la página se cargue completamente
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="v-field-6"]')))

# Encontrar elementos del formulario
campo_nombre = driver.find_element(By.CSS_SELECTOR, 'input[name="v-field-6"]')   
campo_apellido = driver.find_element(By.CSS_SELECTOR, 'input[name="v-field-7"]')
campo_email = driver.find_element(By.CSS_SELECTOR, 'input[name="v-field-8"]')
campo_codigo_empresa = driver.find_element(By.CSS_SELECTOR, 'input[name="v-field-9"]')

# Llenar el formulario
campo_nombre.send_keys(" ")
campo_apellido.send_keys(" ")
campo_email.send_keys(" ")
campo_codigo_empresa.clear()
time.sleep(2)

# Esperar un poco para que la página responda
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#vuero-signup > div.hero.is-fullheight > div > div > div:nth-child(1) > div > div > form > div.button-wrap.has-help > button'))
)  

# Hacer clic en el primer botón "Continue"
boton_continuar = driver.find_element(By.CSS_SELECTOR, '#vuero-signup > div.hero.is-fullheight > div > div > div:nth-child(1) > div > div > form > div.button-wrap.has-help > button')
boton_continuar.click()
print("Primer botón 'Continue' clicado exitosamente!")
time.sleep(2)

# Esperar hasta que la siguiente sección esté presente
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#vuero-signup > div.hero.is-fullheight > div > div > div:nth-child(2) > form > div.button-wrap.is-centered.has-text-centered > button:nth-child(2)')))
    
    # Hacer clic en el segundo botón "Continue"
    boton_siguiente_continuar = driver.find_element(By.CSS_SELECTOR, '#vuero-signup > div.hero.is-fullheight > div > div > div:nth-child(2) > form > div.button-wrap.is-centered.has-text-centered > button:nth-child(2)')
    boton_siguiente_continuar.click()
    print("Segundo botón 'Continue' clicado exitosamente!")

    # Agregar una pausa de 5 segundos antes de hacer clic en "Done"
    time.sleep(2)

    # Esperar hasta que el botón "Done" esté presente
    boton_done = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#vuero-signup > div.hero.is-fullheight > div > div > div:nth-child(3) > div > form > div.button-wrap.is-centered.has-text-centered > button.button.button.v-button.is-disabled.is-rounded.is-big.is-lower.is-primary'))
    )

    # Llenar los campos de contraseña y confirmación de contraseña
    campo_password = driver.find_element(By.CSS_SELECTOR, 'input[name="v-field-10"]')
    campo_confirmar_password = driver.find_element(By.CSS_SELECTOR, 'input[name="v-field-11"]')



    # Ingresa las contraseñas deseadas
    contrasena = " "  # Cambia "TuContrasena" por la contraseña deseada
    campo_password.send_keys(contrasena)
    campo_confirmar_password.send_keys(contrasena)

    time.sleep(5)

    # Hacer clic en el botón "Done"
    boton_done.click()
    print("Botón 'Done' clicado exitosamente!")

    # Agregar una pausa adicional para observar el resultado
    time.sleep(7)

except Exception as e:
    print("Error, contraseña no cumple parametros")

# Cerrar el navegador
driver.quit()
