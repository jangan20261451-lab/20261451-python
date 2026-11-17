window=Tk()
window.geometry("210x210")

for i in range(0,9):
    photoList[i]=photoImage(file="gif/"+fnameList[i])
    btnList[i]=Button(window, image=photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[num].place(x=xPos,y=yPos)
        num+=1
        xPos=0
    xPos=0
    yPos+=70

window.mainloop()







