from tkinter import * # 파이썬 GUI용 툴킷 Tkinter를 import
import subprocess
import cv2

root = Tk() # Tkinter 윈도우 객체 생성

root.title("test1") #타이틀 설정
root.geometry("480x640") # 창 크기 설정

#백그라운드 이미지
wall = PhotoImage(file = "start_background.png") 
wall_label = Label(image = wall)
wall_label.place(x = -2,y = 0)

#Game Start 버튼 상호작용
def btncmd():
    subprocess.call("PyShooting.py", shell=True)

def btncmd2():
    subprocess.call("test.py", shell=True)

#Game start 버튼
btn1 = Button(text="Game start", font=("consolas", 15), width=20, command = btncmd)
btn1.place(x=125, y=290)

#스코어 보드 버튼
btn2 = Button(text="Git_test ", font=("consolas", 15), width=20)
btn2.place(x=125, y=370)

#엔딩 크레딧 버튼
btn3 = Button(text="Ending Credits ", font=("consolas", 15), width=20, command = btncmd2)
btn3.place(x=125, y=450)

#출력
root.mainloop()
