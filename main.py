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
    #C:\Users\didxo\Desktop\pollution.xml
    global xmlFile,root
    try:
        xmlFile = ET.parse(address)
    except IOError:
        print("IOError")
    else:
        try:
            root = xmlFile.getroot()
        except Exception:
            print("loading fail")
    return None

def checkDocument():#xml파일이 파싱됬는지 확인하는 함수
    global xmlFile
    if xmlFile == None:
        print("Error : Document is empty")
        return False
    return True

def main():
<<<<<<< HEAD
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
    items = root.findall("row")
    print(items)
    for data in items:
        for item in data.iter():
            if item.tag=="MSRDT":
                continue
            print(item.text,end=" ")





main()
=======
    a=0
    b=0
    c=1
>>>>>>> refs/remotes/origin/master
