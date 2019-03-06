import yagmail
import app.log.log as log
from app.config.globalparameter import smtp_server,email_name,email_password,email_to

def sendmail(title,content,attrs=None):
    try:
        m=yagmail.SMTP(host=smtp_server,user=email_name,password=email_password,smtp_ssl=True)
        m.send(to=email_to,
               subject=title,
               contents=content,
               attachments=attrs)
    except Exception as e:
        log.atp_log.error('邮件发送失败')
if __name__=='__main__':
    title='test1'

    content='C:\\Users\\cherrylixh\PycharmProjects\\appTest\\app\\report\\201903022151\\result.html'
    sendmail(title,content)
