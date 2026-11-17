import random


def getNumber():
       return random.randrange(1,46)


lotto=[]
num=0


print("**로또 추첨을 시작합니다.**\n");

while True:
    num=getNumber()

    if lotto.count(num)==0:
        lotto.append(num)

    if len(lotto)>=6:
        break

print("추첨된 로또 번호==> ",end='')
lotto.sort()
for i in range(0,6):
    print("%d "%lotto[i],end='')








from tkinter import *
from tkinter import messagebox
window=Tk()


def myFunc():
    if chk.get()==0:
          messagebox.showinfo("","체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("","체크박스가 켜졌어요.")


chk=IntVar()
cb1=Checkbutton(window,text="클릭하세요",variable=chk,command=myFunc)

cb1.pack()

window.mainloop()