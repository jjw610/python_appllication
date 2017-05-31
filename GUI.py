import tkinter as tk

from tkinter import ttk

win = tk.Tk()
win.geometry("593x440") #600x400
win.title("퍼킹 파이썬 하핳")
tabControl = ttk.Notebook(win)
#-------------------------------------------------------------------------------------  버튼 눌럿을 때의 함수를 추가해주길
def sicuation():
    si = int(e1.get())
    if(si<=3 & si>=0):
        t1.insert(INSERT, "1")
        t1.edit_undo()
        t1.insert(INSERT,"자전거타기 딱 좋은 미세먼지네")
    if(si <= 6 & si >= 4):
        t1.insert(INSERT, "1")
        t1.edit_undo()
        t1.insert(INSERT, "어기 거기! 가기전에 스카프 하나 챙겨주라!")
    if (si <= 10 & si >= 7):
        t1.insert(INSERT, "1")
        t1.edit_undo()
        t1.insert(INSERT, "자전거 타다 죽기 딱 좋은 미세먼지네")
#-------------------------------------------------------------------------------------  탭을 추가부분
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 자전거 보관소 위치')
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='날씨정보')
tabControl.pack(expand=1, fill="both")

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='미세먼지')
tabControl.pack(expand=1, fill="both")

tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='사쥔')
tabControl.pack(expand=1, fill="both")
#------------------------------------------------------------------------------------- 탭안에 뭐 넣을지 각각 정해주기
monty1 = ttk.LabelFrame(tab1, text='자전거 보관소 위치 검색창')
monty1.grid(column=0, row=0, padx=8, pady=4)

monty11 = ttk.LabelFrame(monty1)
monty11.grid(column=0, row=0)
l1 = Label(monty11, text = "검색").grid(column=0, row=0, sticky='W')
e1 = Entry(monty11, bg="yellow", fg="black").grid(column=1, row=0, sticky='W')
b1 = Button(monty11, text = "검색",command=sicuation).grid(column=2, row=0, sticky='W')

monty12 = ttk.LabelFrame(monty1)
monty12.grid(column=0, row=1)
t1 = Text(monty12).grid(column=0, row=0, sticky='W')


monty2 = ttk.LabelFrame(tab2, text='날씨정보 검색창')
monty2.grid(column=0, row=0, padx=8, pady=4)
monty21 = ttk.LabelFrame(monty2)
monty21.grid(column=0, row=0)
l2 = Label(monty21, text = "검색").grid(column=0, row=0, sticky='W')
e2 = Entry(monty21, bg="yellow", fg="black").grid(column=1, row=0, sticky='W')
b2 = Button(monty21, text = "검색", command=sicuation).grid(column=2, row=0, sticky='W')

monty22 = ttk.LabelFrame(monty2)
monty22.grid(column=0, row=1)
t2 = Text(monty22).grid(column=0, row=1, sticky='W')


monty3 = ttk.LabelFrame(tab3, text='미세먼지정보 검색창')
monty3.grid(column=0, row=0, padx=8, pady=4)
monty31 = ttk.LabelFrame(monty3)
monty31.grid(column=0, row=0)
l3 = Label(monty31, text = "검색").grid(column=0, row=0, sticky='W')
e3 = Entry(monty31, bg="yellow", fg="black").grid(column=1, row=0, sticky='W')
b3 = Button(monty31, text = "검색").grid(column=2, row=0, sticky='W')

monty32 = ttk.LabelFrame(monty3)
monty32.grid(column=0, row=1)
t3 = Text(monty32).grid(column=0, row=1, sticky='W')

monty4 = ttk.LabelFrame(tab4, text='사진 정보창')
monty4.grid(column=0, row=0, padx=8, pady=4)
#-------------------------------------------------------------------------------------

win.mainloop()
