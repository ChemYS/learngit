# 导入所需模块
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
# pip install PyEmail 文件报名与import名字冲突

# 连接邮箱，然后使用QQ邮箱账号和授权码登录邮箱
qqMail = smtplib.SMTP_SSL("smtp.qq.com", 465)
mailUser = "260410399@qq.com" 
mailPass = "hjvvpnabvdpccaci"  
qqMail.login(mailUser, mailPass)

# 设置收发件人
sender = "260410399@qq.com" 
receiver = "260410399@qq.com.com"
message = MIMEMultipart()
# 整合主题和收发件人到邮件对象中
message["Subject"] = Header("给夜曲的一封信--ChemYS") 
message["From"] = Header(f"ChemYS<{sender}>") 
message["To"] = Header(f"yqbc<{receiver}>") 

# 设置邮件的内容
textContent = '''
在这几天的学习过程中，感觉课程编排得很好，循序渐进，使我能充分利用碎片时间学习并通过练习掌握知识点。不足之处就是部分课程内容存在错别字，希望继续改进。
特别表扬助教叨叨老师，非常耐心服务大家。
'''
mailContent = MIMEText(textContent, "plain", "utf-8")
# 读取图片文件
# filePath = r"C:\Users\ChemYS\learngit\yequbiancheng\ChemYS.jpg"
filePath = r"C:/Users/ChemYS/learngit/yequbiancheng/ChemYS.jpg"
with open(filePath, "rb") as imageFile:
    fileContent = imageFile.read()
# 设置邮件附件，并添加标题
attachment = MIMEImage(fileContent)
attachment.add_header("Content-Disposition", "attachment", filename="入门课成绩单.jpg")

# 添加正文和附件
message.attach(mailContent)
message.attach(attachment)
# 发送邮件
qqMail.sendmail(sender, receiver, message.as_string())
print("发送成功")