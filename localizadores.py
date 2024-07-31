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
phone_number = (By.CLASS_NAME, 'np-text')
new_phone_number = (By.XPATH, "//input[@id='phone'][@class='input']")
phone_submit_button = (By.XPATH, "//button[@type='submit'][@class='button full' and text()='Siguiente']")
code_input = (By.XPATH, "//input[@id='code'][@class='input'][@type='text']")
code_submit = (By.XPATH, "//button[@type='submit'][@class='button full' and text()='Confirmar']")
payment = (By.CLASS_NAME, 'pp-value-text')
payment_select = (By.CLASS_NAME, 'pp-plus')
card_input = (By. ID, 'number')
random_click = (By. CLASS_NAME, 'plc')
card_code_input = (By.XPATH, "//input[@type='text'][@id='code'][@name='code'][@placeholder='12']")
card_submit = (By.XPATH, "//button[@type='submit'][@class='button full' and text()='Agregar']")
card_registered = (By.XPATH, "//div[@class='pp-title' and text()='Tarjeta']")
close_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
message = (By. ID, 'comment')
blanket = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
blanket_on = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input")
ice_cream = (By.XPATH, "//*[@id='root']//div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")
ice_cream_plus = (By. XPATH, "//*[@id='root']//div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]")
#"//div[@class='counter-value' and text()='2']")


