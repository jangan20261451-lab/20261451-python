from tkinter import*
from tkinter.filedialog import askopenfilename
def fun_open():
    filepath=askopenfilename(
        title = "gif 이미지 로드",filetypes = (("gif이미지","*.gif"),("png이미지","*.png"))
    )
    tk_img = PhotoImage(filepath)
    image_label.config(image=tk_img)
    Image_label.image = tk_img

window = Tk()
window.title("Gif 뷰어")

image_label = Label(window)
image_label.pack(expand=True)

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일",menu = fileMenu)
fileMenu.add_command(label="열기",command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료",command=func_exit)


window.mainloop()


