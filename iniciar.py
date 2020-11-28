from partes import bot
from partes import selenium


driver = selenium.iniciar_selenium()
bot.iniciar(driver)
