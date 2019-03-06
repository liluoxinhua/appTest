#coding=utf-8
import matplotlib.pyplot as plt
import matplotlib.image as mping
from datetime import datetime as dt
import matplotlib.dates as mdates
import xlrd
from pylab import *
import app.config.globalparameter as gl
from app.log.log import atp_log
def paint(picname,title):
    try:
        #获取图片所在路径
        global newreportpath
        newreportpath=gl.newreport()
        print('.........draw picture.......')
        plt.figure(picname)
        filename=newreportpath+picname+'.csv'
        #获取csv中的数据，转化为x,y轴数据
        x, y = get_weight_data(filename)
        x = range(len(x))
        maxy=int(max(y))
        average=int(sum(y)/len(y))
        #plot绘制折线图，设置标题，线条尺寸和颜色
        plt.plot(x, y, label=title, linewidth=1, color='r')
        if 'CPU' in picname:
            # 设置图片的名称
            plt.title('Max:'+str(maxy)+'% Average:'+str(average)+'%')
            #设置x轴的标签
            plt.xlabel(title)
            #设置y轴标签
            plt.ylabel('CPU Percent')
        else:
            plt.title('Max:'+str(maxy)+'KB Average:'+str(average)+'KB')
            plt.xlabel(title)
            plt.ylabel('PSS(KB)')
        #设置y轴高度
        if picname=='a':
            plt.ylim(0.0,400000)
        elif picname=='MEM_a':
            plt.ylim(0.0,450000)
        elif 'CPU' in picname:
            plt.ylim(0.0,250)
        else:
            plt.ylim(0.0,150000)
        #将图片保存在本地
        plt.savefig(newreportpath+picname+'.png')
    except Exception as e:
        print(e)
        atp_log.error(e)
#读取csv文件的数据
def get_weight_data(filename):
    time=[]
    weight=[]
    f=xlrd.open_workbook(filename)
    sheet_one=f.sheet_by_index(0)
    ncolsn=sheet_one.ncols
    nrowsn=sheet_one.nrows
    for i in range(nrowsn):
        nrowdata=sheet_one.cell(i,0).value
        time.append(float(nrowdata))
        ncoldata=sheet_one.cell(i,1).value
        weight.append(float(ncoldata))
    return time,weight
if __name__=="__main__":
    paint('CPU_a', 'com.pptv.tvsports.a')
    paint('CPU_ppdata', 'com.pptv.tvsports:ppdata')
    #paint('CPU_guard', 'com.pptv.tvsports:guard')
    paint('MEM_a', 'com.pptv.tvsports(total)')
    paint('MEM_ppdata', 'com.pptv.tvsports')
    #paint('MEM_guard', 'com.pptv.tvsports:guard')

