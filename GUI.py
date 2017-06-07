import tkinter as t1
from tkinter import *
from tkinter import ttk
import Mungi
import Weather
import bicycle

win = t1.Tk()
win.geometry("897x400") #600x400
win.title("퍼킹 파이썬 하핳")
tabControl = ttk.Notebook(win)
#-------------------------------------------------------------------------------------  버튼 눌럿을 때의 함수를 추가해주길
def WeatherProcess():
    weatherText.delete('1.0 ',END )
    select=weatherComboBox.get()
    returnList = []
    photo = PhotoImage(file="clean.gif")
    if select=="서울":
        returnList = Weather.ConnectServer("seoul")
    elif select =="인천":
        returnList = Weather.ConnectServer("Incheon")
    elif select =="강원도":
        returnList = Weather.ConnectServer("Gangwon")
    elif select =="충청도":
        returnList = Weather.ConnectServer("Daesun")
    elif select =="경상도":
        returnList = Weather.ConnectServer("busan")
    elif select =="전라도":
        returnList = Weather.ConnectServer("Junrado")
    for i in range(0,5,1):
        weatherText.insert(INSERT,returnList[i])
        weatherText.insert(INSERT, "\n")
    if (returnList[2] == '날씨: 맑음'):
        photo = PhotoImage(file="clean.gif")
    elif (returnList[2] == '날씨: 구름 조금' or returnList[2] == '날씨: 구름 많음' or returnList[2] == '날씨: 흐림'):
        photo = PhotoImage(file="cloud.gif")
    elif (returnList[2] == '날씨: 비'):
        photo = PhotoImage(file="rain.gif")
    elif (returnList[2] == '날씨: 눈/비' or returnList[2] == '날씨: 눈'):
        photo = PhotoImage(file="snow.gif")
    weatherImage.configure(image = photo)
    weatherImage.image = photo
#----------------------------------------------------------------------------------------날씨
def DustProcess():
    dustText.delete("1.0",END)
    tag = dustComboBox.get()
    Mungi.ConnectServer()
    returnData = Mungi.Findlocation(tag)
    print(returnData)
    for i in range(0,6,1):
        dustText.insert(INSERT,returnData[i])
        dustText.insert(INSERT,"\n")
#----------------------------------------------------------------------------------------미세먼지
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
vBigTable = ttk.LabelFrame(tab1, text='빅프레임')
vBigTable.grid(column=0, row=0)

titleTable = ttk.LabelFrame(vBigTable, text='타이틀프레임')
titleTable.grid(column=0, row=0)

mainTable = ttk.LabelFrame(vBigTable, text='메인프레임')
mainTable.grid(column=0, row=1)

bicycleBigTable = ttk.LabelFrame(mainTable, text='자전거 보관소 위치 검색창')
bicycleBigTable.grid(column=0, row=0)

bicycleTable1 = ttk.LabelFrame(bicycleBigTable)
bicycleTable1.grid(column=0, row=0)

bicycleLabel = Label(bicycleTable1, text = "검색")
bicycleLabel.grid(column=0, row=0)
bicycleEntry = Entry(bicycleTable1, bg="yellow", fg="black")
bicycleEntry.grid(column=1, row=0)
bicycleButton = Button(bicycleTable1, text = "검색")
bicycleButton.grid(column=2, row=0)

bicycleTable2 = ttk.LabelFrame(bicycleBigTable)
bicycleTable2.grid(column=0, row=1)

bicycleText = Text(bicycleTable2, width = 40, height = 10)
bicycleText.grid(column=0, row=0, sticky='W')


weatherBigTable = ttk.LabelFrame(mainTable, text='날씨정보 검색창')
weatherBigTable.grid(column=1, row=0)
weatherTable1 = ttk.LabelFrame(weatherBigTable)
weatherTable1.grid(column=0, row=0)
weatherTableForImage = ttk.LabelFrame(weatherBigTable)
weatherTableForImage.grid(column=0, row=0)

#photo = PhotoImage(file="clean.gif")
#weatherImage =Label(weatherTable1,image=photo)
#weatherImage.grid(column=0,row=0)

weatherLabel = Label(weatherTable1, text = "검색")
weatherLabel.grid(column=1, row=0, sticky='W')


weatherComboBox = ttk.Combobox(weatherTable1)
weatherComboBox['values'] = ('서울', '인천', '강원도', '충청도', '전라도','경상도')
weatherComboBox.grid(column=2, row=0)
weatherButton = Button(weatherTable1, text = "검색",command=WeatherProcess)
weatherButton.grid(column=3, row=0, sticky='W')

weatherTable2 = ttk.LabelFrame(weatherBigTable)
weatherTable2.grid(column=0, row=1)

weatherText = Text(weatherTable2, width = 40, height = 10)
weatherText.grid(column=0, row=1, sticky='W')


dustBigTable = ttk.LabelFrame(mainTable, text='미세먼지정보 검색창')
dustBigTable.grid(column=2, row=0)
dustTable1 = ttk.LabelFrame(dustBigTable)
dustTable1.grid(column=0, row=0)

dustLabel = Label(dustTable1, text = "검색")
dustLabel.grid(column=0, row=0, sticky='W')
dustComboBox = ttk.Combobox(dustTable1)
dustComboBox['values'] = ('강동구', '강서구', '강동구', '강북구')
dustComboBox.grid(column=1, row=0)
dustButton = Button(dustTable1, text = "검색",command=DustProcess)
dustButton.grid(column=2, row=0, sticky='W')

dustTable2 = ttk.LabelFrame(dustBigTable)
dustTable2.grid(column=0, row=1)

dustText = Text(dustTable2, width = 40, height = 10)
dustText.grid(column=0, row=1, sticky='W')


bottomTable = ttk.LabelFrame(vBigTable, text='바텀프레임')
bottomTable.grid(column=0, row=2)

mailIDLabel = Label(bottomTable, text = "ID입력")
mailIDLabel.grid(column=0, row=0)
mailIDEntry = Entry(bottomTable, bg="yellow", fg="black", width = 30)
mailIDEntry.grid(column=1, row=0, padx = 50)

mailPasswordLabel = Label(bottomTable, text = "PASSWORD입력")
mailPasswordLabel.grid(column=0, row=1)
mailPasswordEntry = Entry(bottomTable, bg="yellow", fg="black", width = 30)
mailPasswordEntry.grid(column=1, row=1, padx = 50)

mailLabel = Label(bottomTable, text = "메일주소입력")
mailLabel.grid(column=0, row=2)
mailEntry = Entry(bottomTable, bg="yellow", fg="black", width = 100)
mailEntry.grid(column=1, row=2)
mailButton = Button(bottomTable, text = "전송!")
mailButton.grid(column=2, row=2)



pictureBigTable = ttk.LabelFrame(tab4, text='사진 정보창')
pictureBigTable.grid(column=0, row=0,)
#-------------------------------------------------------------------------------------

win.mainloop()