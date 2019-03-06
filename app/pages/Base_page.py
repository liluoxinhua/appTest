# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Base_page:
    def __init__(self,driver):
        self.driver=driver
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_any_elements_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e
    def send_keys(self,value,*loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except ArithmeticError as e:
            raise e
