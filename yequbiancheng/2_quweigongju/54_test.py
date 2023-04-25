# 导入pyautogui模块
import pyautogui

# 定义一个openWechat()函数来打开微信
def openWechat():
    # 使用hotkey()函数，操作按键"command", "e"
    #pyautogui.hotkey("command", "e")
    pyautogui.hotkey("ctrl", "alt", "w")
    # 使用time.sleep()设置停顿1秒
    time.sleep(1)

# 导入pyperclip模块
import pyperclip

# 定义一个查询联系人的函数chatWho()，参数为name
def chatWho(name):
    # 使用pyperclip模块中的copy函数，复制name到剪贴板
    pyperclip.copy(name)
    # 使用hotkey函数，操作按键"command","f"，打开搜索
    pyautogui.hotkey("ctrl", "f")
    # 使用time.sleep()设置停顿1秒
    time.sleep(1)
    # 使用hotkey函数，操作按键"command", "v"，粘贴微信号
    pyautogui.hotkey("ctrl", "v")
    # 使用time.sleep()设置停顿1秒
    time.sleep(1)
    # 使用hotkey函数，操作按键"return"，确认搜索
    pyautogui.hotkey("return")
    # 使用time.sleep()设置停顿1秒
    time.sleep(1)

# 定义一个发送信息的函数setMsg()，参数为msg
def sentMsg(msg):
    # 使用pyperclip模块中的copy函数，复制Msg到剪贴板
    pyperclip.copy(msg)
    # 使用hotkey函数，操作按键"command", "v"，粘贴msg
    pyautogui.hotkey("ctrl", "v")
    # 使用time.sleep()设置停顿1秒
    time.sleep(1)
    # 使用hotkey函数，操作按键"return"，确认搜发送
    pyautogui.hotkey("return")
    
# TODO 导入time模块
import time
# TODO 导入datetime模块
import datetime

# TODO 定义变量flag控制循环，并将flag赋值为1
flag = 1
# 创建while循环，当flag = 1的时候循环不跳出
while flag:
    # TODO 使用datetime.datetime.now()获取当前时间
    # 赋值给变量now_time
    now_time = datetime.datetime.now()
    # TODO 使用now_time.strftime('%Y-%m-%d %H:%M:%S')将当前时间转换为字符串格式
    # 赋值给变量format_time
    format_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
    # TODO 设置定时发送微信的时间，时间格式为'2021-12-10 09:30:00',赋值给变量target_time
    target_time = "2023-04-20 15:27:00"
    print(format_time[:-1])
    # 判断当前时间是否跟设置时间一致
    if format_time[:-1] == target_time[:-1]:
        # TODO 执行完后将flag赋值为0，跳出循环
        flag = 0
# TODO 调用函数openWechat()打开微信
openWechat()
# TODO 调用函数chatWho()，提醒对象为"lili"
chatWho("ChemYS")
# TODO 调用函数sentMsg()，提醒内容为"别忘了上班打卡哦~"
sentMsg('别忘了上班打卡哦~')
# 使用time.sleep()设置停顿1秒
time.sleep(1)