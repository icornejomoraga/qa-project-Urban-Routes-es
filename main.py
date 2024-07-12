import time
import data
import localizadores
import metodos
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from metodos import UrbanRoutes


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)

    def test_set_route(self):
        #self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutes(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(3)
        routes_page.setting_new_route()
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_comfort_selection(self):
        routes_page = UrbanRoutes(self.driver)
        time.sleep(5)
        routes_page.set_from_to_ask_taxi()
        assert routes_page.get_after_comfort_button_selected() == 'Manta y pañuelos'

    def test_submit_phone_number(self):
        routes_page = UrbanRoutes(self.driver)
        phone_number = data.phone_number
        time.sleep(5)
        #routes_page.write_new_phone_number()
        assert routes_page.get_phone_number_input() == phone_number

    def test_submit_new_card(self):
        routes_page = UrbanRoutes(self.driver)
        time.sleep(5)
        #routes_page.submit_new_credit_card()
        new_tc_registered = data.card_number
        assert routes_page.get_new_tc_registered() == new_tc_registered

    def test_new_comment(self):
        routes_page = UrbanRoutes(self.driver)
        time.sleep(5)
        new_comment = data.message_for_driver
        assert routes_page.get_comments() == new_comment




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
