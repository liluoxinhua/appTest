# -*- coding: utf-8 -*-
import random
import time,os
import traceback
import unittest
import app.config.globalparameter as gl
from app.config import driver_configure
from app.config.globalparameter import packageName
class TestInterfaceCase(unittest.TestCase):
    global driver
    def __init__(self,methodName='runTest'):
        super(TestInterfaceCase,self).__init__(methodName)
    @classmethod
    def setUpClass(cls):
        dconfigur= driver_configure.driver_configure()
        driver=cls.driver=dconfigur.get_driver()
    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass
    def changePlayer(self):
        # 切换播放器
        self.driver.press_keycode(82)
        time.sleep(2)
        self.driver.press_keycode(82)
        time.sleep(2)
        self.driver.press_keycode(20)
        self.driver.press_keycode(20)
        self.driver.press_keycode(22)
        self.driver.press_keycode(random.randint(19, 20))
        self.driver.press_keycode(23)
        self.driver.press_keycode(4)
        time.sleep(5)
        self.driver.press_keycode(82)
        self.driver.press_keycode(19)
        self.driver.press_keycode(19)
        self.driver.press_keycode(4)
        time.sleep(2)


    def changeQuality(self):
        # 切换画质
        self.driver.press_keycode(82)
        time.sleep(2)
        self.driver.press_keycode(22)
        time.sleep(2)
        n = random.randint(1, 3)
        for i in range(n):
            self.driver.press_keycode(random.randint(19, 20))
        time.sleep(2)
        self.driver.press_keycode(23)


    def changeTowp(self):
        # 切换到点播
        self.changeChannel()
        self.driver.press_keycode(20)
        time.sleep(1)
        self.driver.press_keycode(22)
        time.sleep(1)
        self.driver.press_keycode(23)
        time.sleep(5)


    def changeChannel(self):
        # 切换频道
        n = random.randint(1, 10)
        for i in range(n):
            self.driver.press_keycode(random.randint(19, 20))
        time.sleep(1)
        self.driver.press_keycode(23)
        time.sleep(10)


    def fastForwardTest(self):
        # 快进
        while True:
            try:
                self.driver.press_keycode(22)
                time.sleep(0.1)
                dt = self.driver.find_element_by_id(packageName + ":id/duration_time").text
                ct = self.driver.find_element_by_id(packageName + ":id/current_time").text
                dtt = int(dt.strip(' ').split(':')[0]) * 3600 + int(dt.strip(' ').split(':')[1]) * 60 + int(
                    dt.strip(' ').split(':')[2])
                ctt = int(ct.strip(' ').split(':')[0]) * 3600 + int(ct.strip(' ').split(':')[1]) * 60 + int(
                    ct.strip(' ').split(':')[2])
                if dtt - ctt == 8:
                    time.sleep(10)
            except:
                print (traceback.format_exc())
                pass
#monkey测试脚本
    def monkey_android(self, IPPORT,number):
        filepath = gl.newreport()
        monkeyresult = os.popen(
            'adb -s ' + IPPORT + ' shell monkey -p com.pptv.tvsports -s 2992 --pct-nav 30 --pct-syskeys 30 --pct-majornav 30 --pct-appswitch 10 --throttle 300  --ignore-timeouts --ignore-crashes --ignore-security-exceptions -v -v -v ' + number).read()
        print(monkeyresult)
        file_monkey = open(filepath + '\\monkey.log', 'w', encoding='utf-8')
        file_monkey.write(monkeyresult)
        file_monkey.close()