import tkinter as tk
import data
from data import value, dis

cell = []


def choose(event):
    global cell, value, dis
    PanelName.geometry("%dx%d+%d+%d" %
                       (PanelSide, PanelSide, PanelPlaceX, PanelPlaceY))
    name.set(data.RepeatlessChoice(value, dis, cell))


def defult(event):
    PanelName.geometry("1x1-100-100")


'''子窗口'''
BallName = tk.Tk()
PanelName = tk.Toplevel()
BallName.overrideredirect(True)
PanelName.overrideredirect(True)
BallName.wm_attributes("-topmost", 1)
PanelName.wm_attributes("-topmost", 1)
BallName.attributes("-alpha", 0.3)
PanelName.attributes("-alpha", 0.89)
BallName.config(background="#000d0e")
PanelName.config(background="#000d0e")
'''主窗口大小设置'''
MainWindowHeight, MainWindowWidth = 600, 1000
ScreenHeight, ScreenWidth =BallName.winfo_screenheight(),BallName.winfo_screenwidth()
MainWindowPlaceX, MainWindowPlaceY = (ScreenHeight - MainWindowHeight) / 2, (
    ScreenWidth - MainWindowWidth) / 2
'''子窗口大小设置'''
BallHeight, BallWeight = 50, 30
BallPlaceX, BallPlaceY = ScreenWidth - BallWeight, (ScreenHeight -
                                                    BallHeight) / 2 - 100
PanelSide = 500
PanelPlaceY, PanelPlaceX = (ScreenHeight - PanelSide) / 2, (ScreenWidth -
                                                            PanelSide) / 2
BallName.geometry("%dx%d+%d+%d" %
                  (BallWeight, BallHeight, BallPlaceX, BallPlaceY))
PanelName.geometry("1x1-100-100")
'''悬浮球图案'''
label = tk.Label(BallName,
                 text="[|",
                 font=("微软雅黑", 25),
                 fg="#00ffd6",
                 bg="#000d0e").place(relx=0.5, rely=0.4, anchor="center")
'''动态字符串'''
name = tk.StringVar()
label = tk.Label(PanelName,
                 textvariable=name,
                 font=("微软雅黑", 100),
                 fg="#00ffd6",
                 bg="#000d0e").place(relx=0.5, rely=0.5, anchor="center")
mark = tk.StringVar()
'''实现抽人'''
PanelName.bind("<Button-1>", defult)
BallName.bind("<Button-1>", choose)
'''开始主循环'''
BallName.mainloop()
