import tkinter
import threading
import random

windows = tkinter.Tk()
windows.title('硬件技术联盟抽奖')
windows.geometry('1000x500')
label1 = tkinter.Label(windows, text='请输入抽奖人数')  # 标签
label1.pack()
e = tkinter.Entry()
e.pack()

starts = 0

# 是否停止标志

notround = False


# 定义开始函数


def round():
    t = threading.Thread(target=started)
    t.start()


def started():

    global notround

    while True:

        # 检测停止按钮是否被按下
        if notround == True:
            notround = False

            return starts
        # 程序延时
        number = e.get()
        number = int(number)
        things = range(1, number + 1)
        maxvalue = len(things)
        luckboy = random.choice(things)
        label3 = tkinter.Label(windows, fg='red', text='中奖号码为')
        label3.place(x=450, y=250)
        label2 = tkinter.Label(windows, fg='red', text=luckboy, font=('Arial', 20), width=15, height=5)
        label2.place(x=350, y=300)
        print(luckboy)


def stops():
    global notround

    notround = True


btn1 = tkinter.Button(windows, text='开始', bg='white', command=round)
btn1.place(x=450, y=100, width=130, height=40)

btn2 = tkinter.Button(windows, text='停止', bg='white', command=stops)
btn2.place(x=450, y=150, width=130, height=40)

windows.mainloop()
