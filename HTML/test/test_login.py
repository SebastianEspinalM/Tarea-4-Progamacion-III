import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

def take_screenshot(driver, name):
    path = f"screenshots/{name}.png"
    driver.save_screenshot(path)

def test_login_exitoso(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    
    assert "inventory" in driver.current_url
    take_screenshot(driver, "login_exitoso")

def test_login_fallido(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("clave_invalida")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

    mensaje = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username and password do not match" in mensaje or "Epic sadface" in mensaje
    take_screenshot(driver, "login_fallido")
