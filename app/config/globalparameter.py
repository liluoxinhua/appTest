# -*- coding: utf-8 -*-
import time,os
import yaml
# 获取项目路径
project_path=os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]),'.'))
# 测试用例代码存放路径（用于构建suite，该文件夹下的文件都应该以test开头）
test_case_path=project_path+'\\app\\testcase'
#测试报告存贮路径
report_path = project_path + '\\report\\'
timepath = time.strftime('%Y-%m-%d-%H_%M_%S') + '\\'
def reportpath():
    reportpath = report_path + timepath
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)
    return reportpath
#获取report目录下最新的文件目录路径
def newreport():
    report_list = os.listdir(report_path)
    report_list.sort(
        key=lambda fn: os.path.getmtime(report_path + fn) if not os.path.isdir(report_path + fn) else 0)
    new_report = os.path.join(report_path, report_list[-1])
    return new_report+'\\'
#设置抓取cpu和mem的进程名称
cpuppdata='CPU_ppdata'
cpuguard='CPU_guard'
cputotall='CPU_a'
memppdata='MEM_ppdata'
memguard='MEM_guard'
memtotall='MEM_a'
usedram='UsedRAM'
#测试报告名称
report_name='result.html'
#获取yaml配置中的机器配置信息
yamlpath = r'C:\Users\cherrylixh\PycharmProjects\appTest\app\config\devices.yaml'
f = open(yamlpath)
res = yaml.load(f)
deviceip = str(res['Devices'][0]['deviceId'])
deviceport = str(res['Devices'][0]['port'])
ipport = deviceip + ':' + deviceport
packageName=str(res['Devices'][0]['packageName'])
appActivity=str(res['Devices'][0]['appActivity'])
platformVersion=str(res['Devices'][0]['platformVersion'])
platformName=str(res['Devices'][0]['platformName'])
#log路径
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
now=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
LOG_PATH=os.path.join(BASE_PATH,'log',now+'.log')
LOG_LEVEL='debug'
#设置发送测试报告的公共邮箱，用户名和密码
smtp_server='smtp.qq.com'
email_name='872677171@qq.com'
#email_password='xinhua@234567$%'
email_password='fmmnadptslckbbgf'
email_to='872677171@qq.com'