import os
from app.testcase.TestInterfaceCase import TestInterfaceCase
import app.config.globalparameter as gl
class testMonkey(TestInterfaceCase):
    @classmethod
    def setUpClass(cls):
        super(testMonkey, cls).setUpClass()
    @classmethod
    def tearDownClass(cls):
        #monkey测试完成后会自动停止脚本，这里不需要在停止driver
        # cls.driver.quit()
        pass
    def test_01(self):
        IPPORT=gl.ipport()
        number='5000'
        TestInterfaceCase().monkey_android(IPPORT,number)