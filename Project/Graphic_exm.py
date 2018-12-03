# coding:utf-8
import tkinter as tk

count = 0
def countUP():
    global count
    count += 1
    label1.config(text=str(count))

root = tk.Tk()
root.geometry("400x150")
root.title("해경뉴스 크롤링")
root.resizable(False, False)

label1 = tk.Label(root, text= "숫자를 입력하세요")
label1.place(x=20, y=20)

editbox1 = tk.Entry(width = 4)
editbox1.place(x=220, y=20)

button = tk.Button(root, text = "안녕", overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.place(x=220, y= 60)
root.mainloop()