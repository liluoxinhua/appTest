#coding=utf-8
import os,time
import threading
import traceback

import xlwt
import xlrd
from xlutils.copy import copy
import app.config.globalparameter as gl
#将数据写入excel文件中
from app.log.log import atp_log


def writexlwt(filename,ctime,cpumem):
    try:
        if os.path.exists(filename):
            workbook=xlrd.open_workbook(filename)
            wxlwt=copy(workbook)
            sheet1=wxlwt.get_sheet(0)
            nrows=workbook.sheet_by_index(0).nrows
            if ctime in workbook.sheet_by_index(0).col_values(0):
                pass
            else:
                sheet1.write(nrows, 0, ctime)
                sheet1.write(nrows, 1, cpumem)
            wxlwt.save(filename)
        else:
            workbook=xlwt.Workbook(encoding='utf-8')
            sheet1=workbook.add_sheet('sheet1')
            sheet1.write(0,0,ctime)
            sheet1.write(0,1,cpumem)
            workbook.save(filename)
    except Exception as e:
        traceback.print_exc()
        atp_log.error(traceback.format_exc())
        raise e
#获取cpu和mem的脚本
def catchMemCpu():
    # 文件的存储路径,不能写在方法外，导入包时会先执行这些代码
    IPPORT = gl.ipport
    filepath = gl.newreport()
    cpuppdatarpath = filepath + gl.cpuppdata + '.csv'
    cpuguardpath = filepath + gl.cpuguard + '.csv'
    cputotallpath = filepath + gl.cputotall + '.csv'
    memppdatapath = filepath + gl.memppdata + '.csv'
    memguardpath = filepath + gl.memguard + '.csv'
    memtotallpath = filepath + gl.memtotall + '.csv'
    usedrampath = filepath + gl.usedram + '.csv'
    try:
        #获取当前时间
        ctime=time.strftime('%Y%d%m%H%M%S',time.localtime())
        #adb指令
        cmdcpuinfo='adb -s '+IPPORT+' shell dumpsys cpuinfo |findstr com.pptv.tvsports'
        mem_a='adb -s '+IPPORT+' shell dumpsys meminfo com.pptv.tvsports.a |findstr TOTAL'
        mem_ppdata = 'adb -s '+IPPORT+' shell dumpsys meminfo com.pptv.tvsports:ppdata |findstr TOTAL'
        mem_guard = 'adb -s '+IPPORT+' shell dumpsys meminfo com.pptv.tvsports:guard |findstr TOTAL'
        #打开系统，发送指令
        cpuinfo=os.popen(cmdcpuinfo)
        for eachline in cpuinfo.readlines():
            #在返回的cpu中进行过滤，注意带上：，将结果写入文件中
            if 'com.pptv.tvsports.a:' in eachline:
                a_cpu=eachline.strip(' ').split(' ')[0].strip('%')
                print(a_cpu)
                writexlwt(cputotallpath,ctime,a_cpu)
            elif 'com.pptv.tvsports:ppdata' in eachline:
                ppdata_cpu=eachline.strip(' ').split(' ')[0].strip('%')
                # cpuprovider.append(provider_cpu)
                writexlwt(cpuppdatarpath,ctime,ppdata_cpu)
            elif 'com.pptv.tvsports:guard:' in eachline:
                # cpuguard.append(ctime)
                guard_cpu=eachline.strip(' ').split(' ')[0].strip('%')
                # cpuguard.append(guard_cpu)
                writexlwt(cpuguardpath,ctime,guard_cpu)
        #将com.pptv.tvsport.a的进程的mem写进内存中，内存取的是总内存
        meminfo_a = os.popen(mem_a).read()
        if len(meminfo_a)>0:
            a_mem=meminfo_a.split( )[1]
            writexlwt(memtotallpath,ctime,a_mem)
        # 将com.pptv.tvsport.ppdata的进程的mem写进内存中，内存取的是总内存
        meminfo_ppdata=os.popen(mem_ppdata).read()
        if len(meminfo_ppdata)>0:
            ppdata_mem=meminfo_ppdata.split( )[1]
            writexlwt(memppdatapath,ctime,ppdata_mem)
        # 将com.pptv.tvsport.guard的进程的mem写进内存中，内存取的是总内存
        meminfo_guard=os.popen(mem_guard).read()
        if len(meminfo_guard)>0:
            guard_mem=meminfo_guard.split( )[1]
            writexlwt(memguardpath,ctime,guard_mem)
        # global t
        # t = threading.Timer(2, catchMemCpu)
        # t.start()
    except Exception as e:
        traceback.print_exc()
        atp_log.error(traceback.format_exc())
        raise e
# def catchstop():
#     print(t)
#     t.cancel()

if __name__=="__main__":
    catchMemCpu()
    time.sleep(10)
    # catchstop()

