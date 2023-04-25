# 导入pyautogui模块
import pyautogui
# 导入pyperclip模块
import pyperclip
# 导入time模块
import time
# 使用import导入requests模块
import requests
# 使用import导入json模块
import json

# 定义一个openWechat()函数打开微信
def openWechat():
    # 使用hotkey()函数，操作按键"command", "e"，打开微信
    pyautogui.hotkey("ctrl", "alt", "w")
    # 停顿一秒
    time.sleep(1)

# 定义一个查询联系人chatWho()函数，参数为name
def chatWho(name):
    # 使用hotkey函数，操作按键"command","f"，打开搜索
    pyautogui.hotkey("ctrl","f")
    # 停顿一秒
    time.sleep(1)
    # 使用pyperclip模块中的copy函数，复制联系人微信号到剪贴板
    pyperclip.copy(name)
    # 使用hotkey函数，操作按键"command", "v"，粘贴联系人微信号
    pyautogui.hotkey("ctrl", "v")
    # 停顿一秒
    time.sleep(1)
    # 使用hotkey函数，操作按键"return"，确认搜索
    pyautogui.hotkey("return")
    # 停顿一秒
    time.sleep(1)
    
# 定义一个提交信息的sentMsg()函数，参数为msg
def sentMsg(msg):
    # 使用pyperclip模块中的copy函数，复制msg到剪贴板
    pyperclip.copy(msg)
    # 使用hotkey函数，操作按键"command", "v"，粘贴msg
    pyautogui.hotkey("ctrl", "v")
    # 停顿一秒
    time.sleep(1)
    # 使用hotkey函数，操作按键"return"，确认搜发送
    pyautogui.hotkey("return")
    

# TODO 定义一个getStock()函数查今日股票情况
def getStock():
    # 将API链接赋值给url
    url = "https://www.futunn.com/search-stock/hot-stocks?lang=zh-CN&_=1639104860925"
    # 将User-Agent以字典键对形式赋值给header
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"}
    # TODO 使用requests.get()，赋值给变量response
    # 传入url
    # 传入参数headers，值为字典header
    response = requests.get(url,headers=header)
    # TODO 访问.text属性获取返回数据文本，并赋值给data
    data = response.text
    # TODO 使用json.loads()将str转换成dict，赋值给stock_json
    stock_json = json.loads(data)
    # TODO 定义列表stock_name、stock_change_ratio，用来存储股票名称、变化率
    stock_name = []
    stock_change_ratio = []
    # TODO 通过字典层层索引，找到股票名称、变化率，并分别添加到列表stock_name、stock_change_ratio中
    for info in stock_json["data"]:
        stock_name.append(info["stock_name"])
        stock_change_ratio.append(info["change_ratio"])
    # 返回(stock_name、stock_change_ratio)
    return (stock_name,stock_change_ratio)

    
# 调用openWechat()函数打开桌面微信
openWechat() 
# 调用chatWho(name)函数查找联系人"曹叔"
chatWho("ChemYS")
# TODO 调用getStock()函数将第一个元素赋值给stock_name
# 将第二个元素赋值给stock_change_ratio
stock_name = getStock()[0]
stock_change_ratio = getStock()[1]
# for循环遍历range()函数以len(stock_name)长度的整数
for stock in range(len(stock_name)):
    # TODO 格式化字符串输出f"{股票名称}今日变化率为{变化率}"，并赋值给text
    text = f"{stock_name[stock]}今日变化率为{stock_change_ratio[stock]}"
    # TODO 调用sentMsg(msg)函数逐条发送
    sentMsg(text)