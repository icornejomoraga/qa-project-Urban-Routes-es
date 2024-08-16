import time
import data
from selenium import webdriver
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
        routes_page.write_new_phone_number()
        assert routes_page.get_phone_number_input() == phone_number

    def test_submit_new_card(self):
        routes_page = UrbanRoutes(self.driver)
        time.sleep(5)
        routes_page.submit_new_credit_card()
        assert routes_page.get_new_tc_registered() == 'Tarjeta'
        routes_page.close_window()

    def test_new_comment(self):
        routes_page = UrbanRoutes(self.driver)
        time.sleep(5)
        routes_page.message_to_control()
        new_comment = data.message_for_driver
        assert routes_page.get_comments() == new_comment

    def test_blankets(self):
        routes_page = UrbanRoutes(self.driver)
        time.sleep(5)
        routes_page.blankets()
        assert routes_page.assert_blankets()

    def test_ice_cream(self):
        routes_page = UrbanRoutes(self.driver)
        time.sleep(5)
        routes_page.where_is_ice_cream()
        routes_page.where_is_ice_cream()
        assert routes_page.ice_cream_selected() == '2'

    def test_modal_appears(self):
        routes_page = UrbanRoutes(self.driver)
        time.sleep(5)
        routes_page.click_the_blue_button()
        assert routes_page.modal_appears() == 'Buscar automóvil'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
