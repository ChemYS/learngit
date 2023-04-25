# 导入pyautogui模块
import pyautogui
# 导入pyperclip模块
import pyperclip
# 导入time模块
import time

# 定义一个openWechat()函数打开微信
def openWechat():
    # 使用hotkey()函数，操作按键"command", "e"
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

# TODO 导入xlrd模块
import xlrd
# TODO 将Excel文件路径/yequ/StudentsPerformance.xlsx，赋值给变量path
path = "C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/57/StudentsPerformance.xlsx"

# 定义一个getData()函数获取每门课的最高分、最低分和及格率
def getData(list_,name):
    """
    list_：所需计算的列表
    name:考试的科目名,为math,reading或者writing
    """   
    # TODO 最高分
    top = max(list_)
    # TODO 最低分
    lowest = min(list_)
    # 及格率
    # TODO 定义count用于计数
    count = 0
    # TODO 记录总人数
    total = len(list_)
    # TODO 判断是否及格并更新count
    for info in list_:
        if info >= 60:
            count += 1
        
            
    # TODO 计算及格率（保留两位小数）并赋给pass_percent
    pass_percent = "{:.2%}".format(count/total)
        
    # 返回 f"本次{name}测验中,最高分为{top},最低分为{lowest},及格率为{pass_percent}"
    text =  f"本次{name}测验中,最高分为{top},最低分为{lowest},及格率为{pass_percent}"
    return text

# TODO 定义一个getText()函数,得到需要发送的测验文本信息：分别获取每门课的最高分、最低分和及格率
def getText(path):
    # TODO  导入数据
    data = xlrd.open_workbook(path)
    # TODO  使用sheets()获取工作表对象，索引第一个元素赋值给变量table
    table = data.sheets()[0]

    # TODO 找到数学成绩除列名外的所有数据，赋值给math_score
    math_score = table.col_values(0)[1:]
    # TODO  找到阅读成绩除列名外的所有数据，赋值给reading_score
    reading_score = table.col_values(1)[1:]
    # TODO  找到数学成绩除列名外的所有数据，赋值给writing_score
    writing_score = table.col_values(2)[1:]
    
    # TODO  调用getData()函数获取每门课的信息，并分别赋值给math_text，reading_text和writing_text
    math_text = getData(math_score,"math")
    reading_text = getData(reading_score,"reading")
    writing_text = getData(writing_score,"writing")
        
    # TODO 定义字典text，键分别定义为"math_text","reading_text","writing_text"，值为其对应的值
    text =   {"math_text":math_text,"reading_text":reading_text,"writing_text":writing_text}
    # 返回字典text
    return text

# TODO 调用getText()函数获取考试信息的文本并赋值给text
text = getText(path)

# TODO 调用openWechat()函数打开桌面微信
openWechat()
# TODO 调用chatWho(name)函数查找联系人"家长群"
chatWho("ChemYS")
# TODO 停顿1s
time.sleep(1)
# TODO 发送"今日测验成绩已公布，全班总体情况如下"                  
sentMsg("今日测验成绩已公布，全班总体情况如下")
# 停顿1s
time.sleep(1)
# TODO 发送数学成绩的信息                    
sentMsg(text["math_text"])
# 停顿1s
time.sleep(1)
# TODO 发送阅读成绩的信息                     
sentMsg(text["reading_text"])
# 停顿1s
time.sleep(1)
# TODO 发送写作成绩的信息 
sentMsg(text["writing_text"])