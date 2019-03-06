# -*- coding: utf-8 -*-
from app.pages import course_page
from app.testcase.TestInterfaceCase import TestInterfaceCase
class testCourse(TestInterfaceCase):
    @classmethod
    def setUpClass(cls):
        super(testCourse,cls).setUpClass()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
        print('开始测试')
    def tearDown(self):
        print('测试完毕')
    def test01(self):
        self.course_pade=course_page.course_page(self.driver)
        self.course_pade.click_btn()
    def test02(self):
        super(testCourse,self).changePlayer()
    def test_03(self):
        super(testCourse,self).changeQuality()
    def test_04(self):
        super(testCourse,self).changeChannel()
    def test_05(self):
        super(testCourse,self).changeTowp()


