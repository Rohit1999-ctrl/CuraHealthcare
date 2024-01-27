from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Appointment:
    def __init__(self, driver):
        self.driver = driver

    checkbox = (By.ID, "chk_hospotal_readmission")
    health_program = (By.ID, "radio_program_medicaid")
    comment = (By.ID, "txt_comment")
    book_appointment_button = (By.ID, "btn-book-appointment")
    visit_date = (By.XPATH, "//table[@class='table-condensed']/tbody/tr[3]/td[5]")

    def facility_dropdown(self):
        facility_dropdown = Select(self.driver.find_element(By.ID, "combo_facility"))
        return facility_dropdown.select_by_index(2)

    def apply_for_hospital_readmission(self):
        return self.driver.find_element(*Appointment.checkbox)

    def apply_date(self):
        return self.driver.find_element(*Appointment.visit_date)

    def add_comment(self):
        return self.driver.find_element(*Appointment.comment)

    def select_health_program(self):
        return self.driver.find_element(*Appointment.health_program)

    def click_book_appointment_button(self):
        return self.driver.find_element(*Appointment.book_appointment_button)
