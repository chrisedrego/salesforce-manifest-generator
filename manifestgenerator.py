import xml
import xml.etree.cElementTree as ET
import json
import os

xmlns = ""
_encoding = ""
version = ""
_list = ['ApexClass', 'ApexComponent', 'ApexPage', 'ApexTrigger']  
file_name= ""

def getConfig(filePathName):
    with open(filePathName,'r')  as fp:
        return json.load(fp)

def setter():
    configObj = getConfig("./config.json")
    global _encoding 
    _encoding = configObj.get("encoding","")
    global xmlns 
    xmlns = configObj.get("xmlns","")
    global version
    version = configObj.get("version","")
    global file_name
    file_name = configObj.get("file_name","")

def XML_Dump():
    root = ET.Element("Package",xmlns = xmlns)
    for i in range(len(_list)):
        types = ET.SubElement(root,"types")
        members = ET.SubElement(types,"members").text = '*'
        name = ET.SubElement(types,"names").text = _list[i]
        tree = ET.ElementTree(root)
    ET.SubElement(root, "version").text = version
    tree = ET.ElementTree(root)
    tree.write(file_name,encoding=_encoding,xml_declaration=True)

def call_stack():
    setter()
    print("HERE")
    os.remove("package.xml")
    XML_Dump()

