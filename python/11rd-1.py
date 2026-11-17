from tkinter import *
from tkinter import messagebox


def clickLeft(event):
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 두번 클릭됨")



window=Tk()

window.bind("<Double-Button-1>",clickLeft)

window.mainloop()

from tkinter import*

def clickMouse(event):
    txt=""
    if event.num==1:
        txt+="마우스 왼쪽 버튼이 ("
    elif event.num==3:
        txt+="마우스 오른쪽 버튼이 ("

    txt+=str(event.y)+","+str(event.x)+")에서 클릭됨"
    labell.configure(text=txt)

window=Tk()
window.bind("<Button>",clickMouse)
labell.pack(expand=1,anchor=CENTER)
window.mainloop()
