# -*- coding: utf-8 -*-

import app.pages.Base_page as Base_page
from appium.webdriver.common import mobileby
from app.config.globalparameter import packageName
class course_page(Base_page.Base_page):
    by=mobileby.MobileBy()
    course_loc=(by.ID,packageName+':id/home_videoview')
    player_loc=(by.XPATH,'//android.support.v7.widget.RecyclerView[2]/android.widget.FrameLayout')
    def click_btn(self):
        self.find_element(*self.course_loc).click()
    def chickPlayer(self):
        print (self.find_element(*self.player_loc).isfocused())
        if not self.find_element(*self.player_loc).isfocused():
            self.find_element(*self.player_loc).click()


