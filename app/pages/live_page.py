# coding : utf-8
import app.pages.Base_page as Base_page
from appium.webdriver.common import mobileby
from selenium.common.exceptions import TimeoutException
class live_page(Base_page.Base_page):
    by=mobileby.MobileBy
    focus_loc=(by.XPATH,'//*[@resource-id="com.pptv.tvsports:id/all_schedule_item"]/android.widget.ImageView')
    item_loc=(by.ID,'com.pptv.tvsports:id/all_schedule_item')
    play_loc=(by.ID,'com.pptv.tvsports:id/full_play_button')
    def itemClick(self):
        try:
            self.find_element(*self.item_loc).click()
        except TimeoutException as e:
            print (e.stacktrace)
    def appPlayClick(self):
        try:
            self.find_element(*self.play_loc).click()
        except TimeoutException as e:
            print(e.stacktrace)
    def isfocus(self):
        try:
            return self.find_element(*self.focus_loc)
        except Exception as e1:
            print(e1)


