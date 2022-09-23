from tkinter import*
from tkinter import messagebox
import pyscreeze
import pyautogui, pyperclip, random, time

win = Tk()
win.title('Đồi Nợ')
win.geometry('475x230')
win.resizable(False,False)

so_tin = IntVar()
delay = StringVar()
noi_dung = StringVar()
box_1 = Text(win, width=50, height=4, font=('arial',13))
box_1.place(x=10, y=77)

def thuc_hien():
    noidung = noi_dung.get()
    Delay = delay.get()
    sotin = so_tin.get()
    Inp = box_1.get(1.0, END)
    if int(sotin) == 0: messagebox.askokcancel('Cảnh báo', 'Số tin không được phép bằng 0')
    if float(Delay)<0.2: messagebox.askokcancel('Cảnh báo', 'Delay không được nhỏ hơn 0.2')
    if str(Inp) == '':messagebox.askokcancel('Cảnh báo', 'Chưa nhập nội dung, nếu nhiều câu thì các câu cách nhau bằng |')
    else:
        noi__dung = Inp.split('\n')
        for i in range(sotin+1):
            pyperclip.copy(random.choice(noi__dung))
            pyautogui.hotkey("ctrl","v")
            pyautogui.press("enter")
            time.sleep(float(Delay))
               
Label(win, text = 'Số tin Spam',fg = 'blue', font=('arial',12)).place(x= 20, y= 20)
Entry(win, width=15, textvariable= so_tin, font=('arial',10)).place(x=135, y= 21)
Label(win, text = 'Nội dung',fg = 'blue' ,font=('arial',12)).place(x= 20, y= 50)
Label(win, text = 'Delay',fg = 'blue' ,font=('arial',12)).place(x=280, y= 20)
Entry(win, width=10, textvariable= delay).place(x=340, y= 20)
Button(win, text = 'Thực hiện', fg = 'blue',bg = 'yellow', font=('arial',10), command= thuc_hien).place(x= 220, y =195)

win.mainloop()