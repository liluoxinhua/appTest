import subprocess
import time
import app.config.globalparameter as gl
def connectDevice():
    ipport=gl.ipport()
    for i in range(5):
        time.sleep(3)
    connectTask=subprocess.Popen('adb connect '+ipport,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    connectResult=connectTask.stdout.read().decode()
    print(connectResult)
    if 'connected' in connectResult and 'offline' not in connectResult:
        time.sleep(3)
        return True
if __name__=='__main__':
    cn=connectDevice()
    print(cn)
