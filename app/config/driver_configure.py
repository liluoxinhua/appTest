# -*- coding: utf-8 -*-
from appium import webdriver
import app.config.globalparameter as gl
class driver_configure:
# 获取driver
    def get_driver(self):
        try:
            self.desired_caps={}
            self.desired_caps['platformName']=gl.platformName
            self.desired_caps['platformVersion']=gl.platformVersion
            self.desired_caps['appPackage']=gl.packageName
            self.desired_caps['appActivity']=gl.packageName+gl.appActivity
            #是否支持unicode的键盘，如果需要输入中文，要设置为true
            self.desired_caps['unicodeKeyboard']=True
            #是否在测试结束后将键盘重新为系统默认的输入法
            self.desired_caps['resetKeyboard']=True
            #appium服务器等待appium客户端发送新消息的时间，默认是60s
            self.desired_caps['newCommandTimeout']=6000
            self.desired_caps['deviceName']=gl.ipport
            self.desired_caps['noReset']=True
            self.driver=webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)
            return self.driver
        except Exception as e:
            raise e