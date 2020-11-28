from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def iniciar_selenium():
    option = Options()
    option.headless = True
    return webdriver.Firefox(executable_path='C://geckodriver.exe')
