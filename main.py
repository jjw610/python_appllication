import time
import http.client
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import xml.etree.ElementTree as ET
from xml.dom.minidom import parse


xmlFile = None
root=None
def LoadingXml():
    address = str(input("파일 경로 입력: "))
    #C:\Users\원종주\Desktop\GitHub 사용처\pollution.xml
    #C:\Users\원종주\Desktop\GitHub 사용처\every bik.xml
    #C:\Users\원종주\Desktop\GitHub 사용처\bcycl-dpstry-std.xml

    global xmlFile,root
    try:
        xmlFile = ET.parse(address)
    except IOError:
        print("파일을 못 찾았뜸")
    else:
        try:
            root = xmlFile.getroot()
        except Exception:
            print("로딩에서 오류가 났뜸")
    return None

def checkDocument():#xml파일이 파싱됬는지 확인하는 함수
    global xmlFile
    if xmlFile == None:
        print("파싱이 안됬뜸")
        return False
    return True

def main():

    global xmlFile
    LoadingXml()
    PrintXml()
    #reList = FindAuthor()
    #print(reList)
def FindAuthor():
    target = str(input("찾으려는 이름 입력: "))
    global bookData
    retlist = []
    if(not checkDocument()):
        return None
    try:
        tree =  ET.fromstring(str(bookData.toxml()))
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
    bookElements= tree.getiterator("book")
    for data in bookElements:
        strTitle = data.find("title")
        if (strTitle.text.find(target) >=0 ):
            retlist.append((data.attrib["ISBN"], strTitle.text))
    return retlist
def PrintXml():
    global xmlFile
    list = []
    if(not checkDocument()):
        print("xmlFile is None")
        return None
    items = root.findall("list")
    print(items)
    for data in items:
        for item in data.iter():
            if item.tag=="string":
                print(items)


main()

