import tkinter

window = tkinter.Tk()

window.title("Min Byung Chan") # 타이틀 설정
window.geometry("640x480+100+100") # 윈도우 사이즈 설정 
window.resizable(False, False) # 윈도우 사이즈 변경

label = tkinter.Label(window, text="안녕하세요")
label.pack()

window.mainloop()
