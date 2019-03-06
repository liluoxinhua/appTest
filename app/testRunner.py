# coding:utf-8
import threading
import traceback
import unittest,time,os
from unittest import TestSuite
from BeautifulReport import BeautifulReport as bf
import app.common.send_mail as send_mail
import app.config.globalparameter as gl
from app.testcase.testCourse import testCourse
from app.testcase.testLive import testLive
from app.testcase.testMonkey import testMonkey
from app.common.catchmemcpu import catchMemCpu
from app.common.paint import paint
from app.log import logs
from app.log.log import atp_log
from app.common.connectDevices import connectDevice

def catches():
    catchMemCpu()
    global t
    t = threading.Timer(0.5, catches)
    t.start()
def catchstop():
    print(t)
    t.cancel()
if __name__=='__main__':
    try:
        if connectDevice():
            reportPath = gl.reportpath()
            #将测试case加载到uinitest的suite中
            suite = TestSuite()
            testcases=(testMonkey,)
            for test_class in testcases:
                tests=unittest.TestLoader().loadTestsFromTestCase(test_class)
                suite.addTest(tests)
            #创建测试文件目录
            if not os.path.isdir(reportPath):
                os.mkdir(reportPath)
            #开始抓取日志
            logs.getlog()
            #开始抓取cpu，mem
            catches()
            #运行测试用例，使用beautifulreport生成测试报告
            resultpath=gl.newreport()
            run=bf(suite)
            run.report(filename=gl.report_name,description='test',log_path=resultpath)
            # fp = open(report_abspath, 'wb')
            # runner = HtmlTestRunner.HTMLTestRunner(stream=fp, output=reportPath,report_title='test report',descriptions='test result')
            # runner.run(suite)
            # fp.close()
            time.sleep(10)
            #停止抓取cpu，mem
            catchstop()
            #将抓取的cpu，mem绘制成图片
            print('.....strt draw pics.......')
            paint('CPU_a','com.pptv.tvsports.a')
            paint('CPU_ppdata','com.pptv.tvsports:ppdata')
            # paint('CPU_guard','com.pptv.tvsports:guard')
            paint('MEM_a','com.pptv.tvsports(total)')
            paint('MEM_ppdata','com.pptv.tvsports')
            # paint('MEM_guard','com.pptv.tvsports:guard')
            # paint('UsedRAM','System Used RAM')
            #停止抓取log
            logs.stoplog()
            #停止分析log
            logs.readlog()
            #发送邮件
            send_mail.send_email()
        else:
            print('cannot connect device')
            atp_log.error('cannot connect device')
    except Exception as e:
        traceback.print_exc()
        atp_log.error(traceback.format_exc())
        os.popen('taskkill /f /t /im python37.exe')
    finally:
        os.popen('taskkill /f /t /im python37.exe')







