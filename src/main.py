import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Lista de usuarios y contraseñas de los bots
bot_accounts = [
    {"username": "bot1_username", "password": "password"},
    # {"username": "bot2_username", "password": "password"},
    # {"username": "bot4_username", "password": "password"},
    # {"username": "bot3_username", "password": "password"},
    # {"username": "bot6_username", "password": "password"},
    # {"username": "bot5_username", "password": "password"},
    # Agrega los bots que quieras
]

# URL del tweet al que quieres que los bots le den "me gusta"
tweet_url = input("Introduce la URL del tweet: ")

# Iterar sobre cada cuenta de bot
for bot in bot_accounts:
    # Configuración de Selenium
    driver = webdriver.Chrome()
    time.sleep(2)

    # Maximizar la ventana del navegador
    driver.maximize_window()
    
    # Iniciar sesión en Twitter con la cuenta del bot actual
    username = bot["username"]
    password = bot["password"]
    
    # Ir al Login
    driver.get("https://twitter.com/login")
    time.sleep(5)
    
    # Buscar el input y clickar en él
    username_input = driver.find_element(By.XPATH, "//div[contains(@class, 'css-175oi2r')]/div/input[@name='text']")
    username_input.click()
    time.sleep(2)
    
    # Ingresar el usuario y presionar Enter
    username_div = driver.find_element(By.XPATH, "//div[contains(@class, 'css-175oi2r')]")
    username_input = username_div.find_element(By.NAME, "text")
    username_input.send_keys(username)
    time.sleep(2)
    username_input.send_keys(Keys.RETURN)
    time.sleep(2)  # Esperar a que la página se cargue completamente
    
    # Ingresar la contraseña y presionar Enter
    password_div = driver.find_element(By.XPATH, "//div[contains(@class, 'css-175oi2r')]")
    password_input = password_div.find_element(By.NAME, "password")
    password_input.send_keys(password)
    time.sleep(1)
    password_input.send_keys(Keys.RETURN)
    time.sleep(6)  # Esperar a que la página se cargue completamente

    # Visitar el tweet objetivo
    driver.get(tweet_url)
    time.sleep(4)  # Esperar a que la página se cargue completamente
    
    # Dar "me gusta" al tweet
    try:
        like_button = driver.find_element(By.XPATH, '//div[@data-testid="like"]')
        if like_button:
            # Desplazarse hasta el botón de "Me gusta" para asegurarse de que esté visible en la pantalla
            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'nearest' });", like_button)
            time.sleep(2)
            like_button.click()
            print(f'Liked: {username}')
            time.sleep(2)
    except Exception as e:
        print("Error:", e)
        
    # Dar "RT" al tweet
    try:
        rt_button =  driver.find_element(By.XPATH, '//div[@data-testid="retweet"]')
        if rt_button:
            rt_button.click()
            time.sleep(2)
    except Exception as e:
        print("Error:", e)
    
    # Confirmar "RT" al tweet
    try:
        rt_confirm = driver.find_element(By.XPATH, '//div[@data-testid="retweetConfirm"]')
        if rt_confirm:
            rt_confirm.click()
            time.sleep(2)
    except Exception as e:
        print("Error:", e)
    
    # Cerrar el navegador después de que todos los bots hayan terminado
    driver.quit()
    


