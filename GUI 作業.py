# z87823xxx所有 #
"""
==== 1. =====
請參考 73-tkinter-label-2文字擺放place.py

使用tkinter 建立
一個視窗
上面顯示label
產品的資料

"""

import tkinter as tk # 在Python 3.x 匯入該tkinter 函式庫

win = tk.Tk()                            # 建立GUI 應用程式的主視窗
win.wm_title("Android手機")                 # 設定主視窗標題
win.resizable(width=False, height=False) # 設定主視窗不可以被調整大小
win.minsize(width=640, height=480)       # 最小尺寸
win.maxsize(width=640, height=480)       # 最大尺寸

label1 =tk.Label(win,text="產品:Android11")  # 建立文字
label1.place(x=20, y=60)                 # 指定元件位置 x=20, y=60 的位置

label2 =tk.Label(win,text="價格:500")    # 建立文字
label2.place(x=20, y=80)

label3 = tk.Label(win, text="庫存:2")  # 建立文字
label3.place(x=20, y=100)             # 指定元件位置 x=20, y=60 的位置

win.mainloop()                        # 最後步驟：程式做無限循環


"""

==== 2. ======

使用 class 建立
一個class
儲存

產品的相關資料
"""

"""
==== 3. ======
請參考
65-class-properties.py

把第一題的Label 上的文字
改成讀取 class properties

"""
class productClass(object):  # 繼承Python 最上層的object 類別
   productName="Android"                           # 屬性 Property
   productPrice="500"                              # 屬性 Property
   productItems="2"                               # 屬性 Property
   def __init__(self,name,price,items):    # 類別初始化的函數 initialize 一開始要做的函數
       self.productName = name
       self.productPrice = price
       self.productItems = items

   def info(self):                                 # 函數 Function
       print("產品名稱:",self.productName)
       print("價格:",self.productPrice)
       print("庫存:",self.productItems)


productClass1=productClass(name="Android",price="500",items="2")                    # 全域變數
productClass1.info()

import tkinter as tk # 在Python 3.x 匯入該tkinter 函式庫

win = tk.Tk()                            # 建立GUI 應用程式的主視窗
win.wm_title("Android" )                 # 設定主視窗標題
win.resizable(width=False, height=False) # 設定主視窗不可以被調整大小
win.minsize(width=640, height=480)       # 最小尺寸
win.maxsize(width=640, height=480)       # 最大尺寸

label1 =tk.Label(win,text="產品名稱:"+productClass1.productName)  # 建立文字
label1.place(x=20, y=60)                 # 指定元件位置 x=20, y=60 的位置
label2 =tk.Label(win,text="價格:"+str(productClass1.productPrice))  # 建立文字
label2.place(x=20, y=80)                 # 指定元件位置 x=20, y=80 的位置
label3 =tk.Label(win,text="庫存:"+str(productClass1.productItems))  # 建立文字
label3.place(x=20, y=100)                 # 指定元件位置 x=20, y=100 的位置
win.mainloop()       # 最後步驟：程式做無限循環





