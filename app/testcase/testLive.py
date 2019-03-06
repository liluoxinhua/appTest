# -*- coding: utf-8 -*-
import time
from app.pages.live_page import live_page
from app.testcase.TestInterfaceCase import TestInterfaceCase
class testLive(TestInterfaceCase):
    @classmethod
    def setUpClass(cls):
        super(testLive, cls).setUpClass()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_01(self):
        self.live_pade = live_page(self.driver)
        try:
            if self.live_pade.isfocus():
                self.driver.press_keycode(23)
        except:
            self.live_pade.itemClick()
            self.driver.press_keycode(23)
        time.sleep(10)
        self.driver.press_keycode(22)
        time.sleep(2)
        self.driver.press_keycode(23)
        time.sleep(2)
        self.live_pade.appPlayClick()
        time.sleep(5)
