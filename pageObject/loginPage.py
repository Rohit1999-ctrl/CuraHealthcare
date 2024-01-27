from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "txt-username")
    password = (By.ID, "txt-password")
    login_button = (By.XPATH, "//button[@id='btn-login']")

    def fill_login_form_username(self):
        return self.driver.find_element(*LoginPage.username)

    def fill_login_form_password(self):
        return self.driver.find_element(*LoginPage.password)

    def click_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)
