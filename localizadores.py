import main
import metodos
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from_field = (By.ID, 'from')
to_field = (By.ID, 'to')
ask_taxi_button = (By.XPATH,"//*[@id='root']/div/div[3]/div[3]/div[1]/div[3]/div[1]/button")
comfort_button = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
requirements = (By.XPATH, "//div[contains(text(),'Manta y pañuelos')]")
phone_number_input = (By.CLASS_NAME, 'np-text')
new_phone_number = (By. ID, 'phone')
phone_submit_button = (By.XPATH, "//[button[@type='submit'][@class='button full' and text()='Siguiente']")
code_input = (By.XPATH, "//label[@class='label' and text()='Introduce el código']")
code_submit = (By.XPATH, "//[button[@type='submit'][@class='button full' and text()='Confirmar']")
payment = (By.CLASS_NAME, 'pp-button filled')
payment_select = (By.CLASS_NAME, 'pp-plus-container')
card_input = (By.CLASS_NAME, 'card-number-input')
random_click = (By. CLASS_NAME, 'card-second-row')
card_code_input = (By.CLASS_NAME, 'card-code-input')
card_submit = (By.XPATH, "//button[@type='submit'][@class='button full' and text()='Agregar']")
card_registered = (By.XPATH, "//div[@class='pp-title' and text()='Tarjeta']")
message = (By.ID, 'comment')
tissue = (By.XPATH, "*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input")
ice_cream = (By.XPATH, "*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")



