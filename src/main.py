import sys
import tkinter as tk
from tkinter import simpledialog, messagebox
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configuración del webdriver
options = Options()
options.add_argument("--user-data-dir=C:/Users/tu_user/AppData/Local/Google/Chrome/User Data") # 'chrome://version' copiar y pegar hasta 'User Data'
options.add_argument("--profile-directory=Default") # 'chrome://version' copiar el perfil que sigue a 'User Data'
options.add_argument("--start-maximized")

# Lista de usuarios y contraseñas de los bots
bot_accounts = [
    {"username": "bot1", "password": "ps"},
    {"username": "bot3", "password": "ps"},
    {"username": "bot4", "password": "ps"},
    {"username": "bot2", "password": "ps"},
    {"username": "bot5", "password": "ps"},
    {"username": "bot6", "password": "ps"},
    # Agrega los bots que quieras
]

# Crear una ventana emergente para ingresar la URL del tweet
root = tk.Tk()
root.withdraw()
tweet_url = simpledialog.askstring("NOVA Automatizer", "Introduce la URL del tweet \t\t\t\t\t\t")

# Verificar si no se ingresó ninguna URL
if tweet_url is None:
    messagebox.showerror("Error", "No has introducido ninguna URL. El programa se cerrará.")
    sys.exit(1)

# Iterar sobre cada cuenta de bot
for bot in bot_accounts:
    
    # Iniciar Chrome
    # Es necesario tener Chrome cerrado del todo (incluido del menú de la parte inferior derecha) y no estar logueado de por sí en ninguna cuenta del perfil
    driver = webdriver.Chrome(options=options)
    time.sleep(2)
    
    # Iniciar sesión en Twitter con la cuenta del bot actual
    username = bot["username"]
    password = bot["password"]
    
    # Ir al Login
    driver.get("https://twitter.com/login")
    time.sleep(4)
    
    # Buscar el input y clickar en él
    username_input = driver.find_element(By.XPATH, "//div[contains(@class, 'css-175oi2r')]/div/input[@name='text']")
    username_input.click()
    time.sleep(1)
    
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
    time.sleep(4)  # Esperar a que la página se cargue completamente

    # Visitar el tweet objetivo
    driver.get(tweet_url)
    time.sleep(3)  # Esperar a que la página se cargue completamente
    
    # Dar "me gusta" al tweet
    try:
        like_button = driver.find_element(By.XPATH, '//div[@data-testid="like"]')
        if like_button:
            # Desplazarse hasta el botón de "Me gusta" para asegurarse de que esté visible en la pantalla
            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'nearest' });", like_button)
            time.sleep(2)
            like_button.click()
            print(f'Liked: {username}')
            time.sleep(1)
    except Exception as e:
        print("Error:", e)
        
    # Dar "RT" al tweet
    try:
        rt_button =  driver.find_element(By.XPATH, '//div[@data-testid="retweet"]')
        if rt_button:
            rt_button.click()
            time.sleep(1)
    except Exception as e:
        print("Error:", e)
    
    # Confirmar "RT" al tweet
    try:
        rt_confirm = driver.find_element(By.XPATH, '//div[@data-testid="retweetConfirm"]')
        if rt_confirm:
            rt_confirm.click()
            print(f'Retweeted: {username}')
            time.sleep(1)
    except Exception as e:
        print("Error:", e)
    
    # Cerrar sesión en Twitter
    driver.get("https://twitter.com/logout")
    logout_confirm = driver.find_element(By.XPATH, '//div[@data-testid="confirmationSheetConfirm"]')
    time.sleep(2)
    logout_confirm.click()
    time.sleep(4)  # Esperar a que cierre sesión
    
    # Cerrar el navegador
    driver.quit()
    print(f'Bot finalizado: {username}')