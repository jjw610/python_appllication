import tkinter as tk

from tkinter import *

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
bicycleBigTable = ttk.LabelFrame(tab1, text='자전거 보관소 위치 검색창')
bicycleBigTable.grid(column=0, row=0, padx=8, pady=4)

bicycleTable1 = ttk.LabelFrame(bicycleBigTable)
bicycleTable1.grid(column=0, row=0)

bicycleLabel = Label(bicycleTable1, text = "검색")
bicycleLabel.grid(column=0, row=0)
bicycleEntry = Entry(bicycleTable1, bg="yellow", fg="black")
bicycleEntry.grid(column=1, row=0)
bicycleButton = Button(bicycleTable1, text = "검색",command=sicuation)
bicycleButton.grid(column=2, row=0)

bicycleTable2 = ttk.LabelFrame(bicycleBigTable)
bicycleTable2.grid(column=0, row=1)

bicycleText = Text(bicycleTable2)
bicycleText.grid(column=0, row=0, sticky='W')


weatherBigTable = ttk.LabelFrame(tab2, text='날씨정보 검색창')
weatherBigTable.grid(column=0, row=0, padx=8, pady=4)
weatherTable1 = ttk.LabelFrame(weatherBigTable)
weatherTable1.grid(column=0, row=0)

weatherLabel = Label(weatherTable1, text = "검색")
weatherLabel.grid(column=0, row=0, sticky='W')
weatherComboBox = ttk.Combobox(weatherTable1)
weatherComboBox['values'] = ('서울', '인천', '강원도', '충청도', '전라도','경상도')
weatherComboBox.grid(column=1, row=0)
weatherButton = Button(weatherTable1, text = "검색")
weatherButton.grid(column=2, row=0, sticky='W')

weatherTable2 = ttk.LabelFrame(weatherBigTable)
weatherTable2.grid(column=0, row=1)

weatherText = Text(weatherTable2)
weatherText.grid(column=0, row=1, sticky='W')


dustBigTable = ttk.LabelFrame(tab3, text='미세먼지정보 검색창')
dustBigTable.grid(column=0, row=0, padx=8, pady=4)
dustTable1 = ttk.LabelFrame(dustBigTable)
dustTable1.grid(column=0, row=0)

dustLabel = Label(dustTable1, text = "검색")
dustLabel.grid(column=0, row=0, sticky='W')
dustComboBox = ttk.Combobox(dustTable1)
dustComboBox['values'] = ('강동구', '강서구', '강동구', '강북구')
dustComboBox.grid(column=1, row=0)
dustButton = Button(dustTable1, text = "검색")
dustButton.grid(column=2, row=0, sticky='W')

dustTable2 = ttk.LabelFrame(dustBigTable)
dustTable2.grid(column=0, row=1)

dustText = Text(dustTable2)
dustText.grid(column=0, row=1, sticky='W')

pictureBigTable = ttk.LabelFrame(tab4, text='사진 정보창')
pictureBigTable.grid(column=0, row=0, padx=8, pady=4)
#-------------------------------------------------------------------------------------

win.mainloop()