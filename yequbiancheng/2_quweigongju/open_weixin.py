# 导入pyautogui模块
import pyautogui
# 定义一个openWechat()函数来打开微信
def openWechat():
    # 使用hotkey()函数，操作按键"command", "e"
    pyautogui.hotkey("ctrl", "alt","w")
# 调用openWechat()函数打开桌面微信
openWechat()