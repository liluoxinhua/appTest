import os
import re
import subprocess
import time
import collections
import app.config.globalparameter as gl
from app.log.log import atp_log
def getlog():
    try:
        ipport = gl.ipport()
        #获取测试路径
        filepath=gl.newreport()
        #获取测试机器机型
        global device
        device=os.popen('adb -s '+ipport+' shell getprop ro.product.model').read().strip()
        print(device)
        #获取android版本
        androidVersion=os.popen('adb -s '+ipport+' shell getprop to.build.version.release').read().strip()
        #生成log目录
        filename=filepath+device+'_'+'.log'
        log_file=open(filename,'w',encoding='utf-8')
        #抓取log，并保存到log中
        logcmd='adb -s '+ipport+' logcat -v threadtime'
        os.system('adb -s '+ipport+' logcat -c ')
        time.sleep(3)
        global Poplog
        Poplog=subprocess.Popen(logcmd,stdout=log_file,stderr=subprocess.PIPE)
    except Exception as e:
        print(e)
        atp_log.error(e)
    #停止抓取log
def stoplog():
    Poplog.terminate()
#读取log
def readlog():
    try:
        #获取日志路径
        new_report=gl.newreport()
        print(new_report)
        global logerrornumber
        logpath=new_report+device+'_'+'.log'
        error_log_path=new_report+'error.log'
        #将错误日志写到error中
        error_file=open(error_log_path,'w',encoding='utf-8')
        logcat_file=open(logpath,'r',encoding='utf-8',errors='ignore')
        #统计错误日志数量
        logerrornumber=0
        for line in logcat_file.readlines():
            if 'FATAL EXCEPTION' in line or 'Out of memmory' in line or 'Application Not Responding：com.pptv.tvsports' in line or 'ANR in com.pptv.tvsports' in line or 'D GlobalCrashHandler' in line or 'Record By Bugly' in line or 'not enough mem'in line or 'crash occur' in line or 'anr error' in line or 'CRASH：com.pptv.tvsports.a' in line:
                print('error')
                logerrornumber+=1
                error_file.write(line)
        error_file.close()
        logcat_file.close()
        f_error=open(error_log_path,'r',encoding='utf-8')
        txt=f_error.read()
        #统计出现各类异常的次数
        global countFatal
        global countOutofMemory
        global countANR
        global countCrash
        patt=re.compile('Process com.pptv.tvsports.a(.*?) has died')
        counter=collections.Counter(patt.findall(txt))
        countCrash=sum(counter.values())+txt.count('crash occur')+txt.count('CRASH：com.pptv.tvsports.aa')
        countOutofMemory=txt.count('Out of memory')+txt.count('not enough mem')
        countFatal=txt.count('FATAL EXCEPTION')
        countANR=txt.count("Application Not Responding: com.pptv.tvsports")+txt.count("ANR in com.pptv.tvsports") + txt.count('anr error')
        print(countFatal)
        print(countOutofMemory)
        print(countANR)
        print(countCrash)
        f_error.close()
    except Exception as e:
        print(e)
        atp_log.error(e)
if __name__=="__main__":
    getlog()
    time.sleep(5)
    stoplog()
    readlog()
