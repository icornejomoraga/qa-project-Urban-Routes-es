import data


# no modificar


def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutes:

    import localizadores

    def __init__(self, driver):
        self.driver = driver

    def set_from(self):
        from_address = data.address_from
        self.driver.find_element(*self.localizadores.from_field).send_keys(from_address)

    def set_to(self):
        to_address = data.address_to
        self.driver.find_element(*self.localizadores.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.localizadores.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.localizadores.to_field).get_property('value')

    def taxi_button(self):
        self.driver.find_element(*self.localizadores.ask_taxi_button).click()

    def comfort_button(self):
        self.driver.find_element(*self.localizadores.comfort_button).click()

    def get_after_comfort_button_selected(self):
        return self.driver.find_element(*self.localizadores.requirements).text

    def number_button(self):
        self.driver.find_element(*self.localizadores.phone_number).click()

    def set_phone_number(self):
        number_phone = data.phone_number
        self.driver.find_element(*self.localizadores.new_phone_number).send_keys(number_phone)

    def get_phone_number_input(self):
        return self.driver.find_element(*self.localizadores.new_phone_number).get_property('value')

    def phone_number_button_submit(self):

        self.driver.find_element(*self.localizadores.phone_submit_button).click()

    def input_code(self):
        code_sms = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.localizadores.code_input).send_keys(code_sms)

    def submit_code(self):
        self.driver.find_element(*self.localizadores.code_submit).click()

    def pay_click(self):
        self.driver.find_element(*self.localizadores.payment).click()

    def payment_selection(self):
        self.driver.find_element(*self.localizadores.payment_select).click()

    def clic_input_card_number(self):
        self.driver.find_element(*self.localizadores.card_input).click()

    def write_card_number(self):
        number = data.card_number
        self.driver.find_element(*self.localizadores.card_input).send_keys(number)

    def get_new_card_number(self):
        return self.driver.find_element(*self.localizadores.card_input).get_property('value')

    def random(self):
        self.driver.find_element(*self.localizadores.random_click).click()

    def click_tc_code(self):
        self.driver.find_element(*self.localizadores.card_code_input).click()

    def write_tc_code(self):
        code_tc = data.card_code
        self.driver.find_element(*self.localizadores.card_code_input).send_keys(code_tc)

    def submit_new_tc(self):
        self.driver.find_element(*self.localizadores.card_submit).click()

    def get_new_tc_registered(self):
        return self.driver.find_element(*self.localizadores.card_registered).text

    def close_window(self):
        self.driver.find_element(*self.localizadores.close_button).click()

    def comments(self):
        self.driver.find_element(*self.localizadores.message).click()

    def write_comments(self):
        new_comment = data.message_for_driver
        self.driver.find_element(*self.localizadores.message).send_keys(new_comment)

    def get_comments(self):
        return self.driver.find_element(*self.localizadores.message).get_property('value')

    def blankets(self):
        self.driver.find_element(*self.localizadores.blanket).click()

    def setting_new_route(self):
        self.set_from()
        self.set_to()

    def set_from_to_ask_taxi(self):
        self.driver.find_element(*self.localizadores.ask_taxi_button).click()
        self.driver.find_element(*self.localizadores.comfort_button).click()

    def write_new_phone_number(self):
        self.driver.find_element(*self.localizadores.phone_number).click()
        number_phone = data.phone_number
        self.driver.find_element(*self.localizadores.new_phone_number).send_keys(number_phone)
        self.driver.find_element(*self.localizadores.phone_submit_button).click()
        code_sms = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.localizadores.code_input).send_keys(code_sms)
        self.driver.find_element(*self.localizadores.code_submit).click()

    def submit_new_credit_card(self):
        self.driver.find_element(*self.localizadores.payment).click()
        self.driver.find_element(*self.localizadores.payment_select).click()
        self.driver.find_element(*self.localizadores.random_click).click()
        self.driver.find_element(*self.localizadores.card_input).click()
        number = data.card_number
        self.driver.find_element(*self.localizadores.card_input).send_keys(number)
        self.driver.find_element(*self.localizadores.random_click).click()
        self.driver.find_element(*self.localizadores.card_code_input).click()
        code_tc = data.card_code
        self.driver.find_element(*self.localizadores.card_code_input).send_keys(code_tc)
        self.driver.find_element(*self.localizadores.random_click).click()
        self.driver.find_element(*self.localizadores.card_submit).click()

    def message_to_control(self):
        new_comment = data.message_for_driver
        self.driver.find_element(*self.localizadores.message).send_keys(new_comment)

    def assert_blankets(self):
        return self.driver.find_element(*self.localizadores.blanket_on).is_selected()

    def where_is_ice_cream(self):
        self.driver.find_element(*self.localizadores.ice_cream).click()

    def ice_cream_selected(self):
        return self.driver.find_element(*self.localizadores.ice_cream_plus).text

    def click_the_blue_button(self):
        self.driver.find_element(*self.localizadores.blue_button).click()

    def modal_appears(self):
        return self.driver.find_element(*self.localizadores.modal).text
