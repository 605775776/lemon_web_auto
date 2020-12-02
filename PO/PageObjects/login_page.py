from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.PageLocators.login_page_locs import LoginPageLocs as loc


class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.login_button))
        self.driver.find_element(*loc.user_input).send_keys(username)
        self.driver.find_element(*loc.pwd_input).send_keys(password)
        self.driver.find_element(*loc.login_button).click()

    def msg_from_login_form(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.error_msg))
        return self.driver.find_element(*loc.error_msg).text
