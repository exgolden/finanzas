#Librerias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Request
browser=webdriver.Firefox(executable_path="C:\BrowserDriver\geckodriver.exe")
browser.get("https://finance.yahoo.com/")
searchbar=browser.find_element_by_id("yfin-usr-qry")
searchbar.send_keys("TSLA")
#convertir la accion a buscar en un input del usuario
go=browser.find_element_by_id("header-desktop-search-button")
go.click()
 
