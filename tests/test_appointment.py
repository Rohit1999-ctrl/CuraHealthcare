import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from pageObject.loginPage import LoginPage
from pageObject.appointmentSchedule import Appointment
import time

from utilities.base import Base


class TestHome(Base):

    @pytest.mark.run
    def test_loginStatus(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "btn-make-appointment").click()
        log.info("Appointment button clicked")
        time.sleep(5)
        log.info("Begin login")
        login = LoginPage(self.driver)
        login.fill_login_form_username().send_keys("John Doe")
        login.fill_login_form_password().send_keys("ThisIsNotAPassword")
        login.click_login_button().click()
        log.info("login completed")
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[@class='lead text-danger']")))
            if self.driver.find_element(By.XPATH, "//p[@class='lead text-danger']"):
                assert False, log.error("login failed")
            else:
                log.info("login successful")
            time.sleep(3)
        except AssertionError as ae:
            assert False, log.error(f"Assertion error: {ae}")
        except Exception as exc:
            log.error(f"Exception error: {exc}")

        time.sleep(3)

    @pytest.mark.run
    def test_appointment_details(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        log.info("filling the appointment form")
        appointment = Appointment(self.driver)
        log.info("Selecting facility")
        appointment.facility_dropdown()
        log.info("ticking hospital re-admission facility")
        appointment.apply_for_hospital_readmission().click()
        log.info("Selecting Healthcare program")
        appointment.select_health_program().click()
        select_date = self.driver.find_element(By.ID, "txt_visit_date")
        select_date.click()
        appointment.apply_date().click()
        appointment.add_comment().send_keys("Hello, trying my automation")
        appointment.click_book_appointment_button().click()
        log.info("check weather Appointment was book successfully or not")
        try:
            confirmation_text = self.driver.find_element(By.XPATH, "//div[@class='col-xs-12 text-center']/h2").text
            assert "Appointment Confirmation" in confirmation_text, log.error("Appointment unsuccessful")
        except AssertionError as ae:
            assert False, log.error(f"Assertion Error: {ae}")
        except Exception as exc:
            log.error(f"Exception error: {exc}")

    def test_login_with_invalid_creds(self):
        log = self.getLogger()
        try:
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.ID, "btn-make-appointment").click()
            log.info("Appointment button clicked")
            time.sleep(5)
            log.info("Begin login")
            login = LoginPage(self.driver)
            login.fill_login_form_username().send_keys("Jane Doe")
            login.fill_login_form_password().send_keys("ThisIsNotAPassword")
            login.click_login_button().click()
            wait = WebDriverWait(self.driver, 5)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[@class='lead text-danger']")))
            if self.driver.find_element(By.XPATH, "//p[@class='lead text-danger']"):
                log.info("Successfully got error for invalid credentials")
        except AssertionError as ae:
            assert False, log.error(f"Assertion error: {ae}")
        except Exception as exc:
            log.error(f"Exception error: {exc}")

