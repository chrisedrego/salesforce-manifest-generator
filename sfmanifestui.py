from tkinter import *
import json
import xml.etree.cElementTree as ET

root = Tk()

metadata = []

_len  = 0
var = []
list_pkg = []

# Sets the xmlns value 
xmlns = ""

# Sets the type of encoding
_encoding = ""

# Sets the version for the package.xml
version = ""

# Gets the list of Metadata from the config.json
_list = []  

#Name for the output of the XML file to be generated
file_name= ""



# Function is used to set the displayed properties of the application
def display_setting(width=300, height=200):
    root.title('Salesforce Manifest Generator')
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    Button(root, text='Submit', command=XML_Dump).grid(row=4, sticky=W, pady=4)
    Button(root, text='Quit', command=root.quit).grid(row=10, sticky=W, pady=4)

#Loads the config.json
def loadConfig(filePathName):
    with open(filePathName,'r')  as fp:
        return json.load(fp)

#Sets the value of the elements read from config.json
def getConfig():
    configObj = loadConfig("./config.json")
    global _encoding 
    _encoding = configObj.get("encoding","")
    global xmlns 
    xmlns = configObj.get("xmlns","")
    global version
    version = configObj.get("version","")
    global file_name
    file_name = configObj.get("file_name","")
    global metadata
    metadata = configObj.get("metadata","")
    global _len
    _len = len(metadata)  
    global var
    var = [None] * _len
    for i in range(_len):
        var[i] = IntVar()
        Checkbutton(root, text=str(metadata[i]), variable=var[i]).grid(row=i, sticky=W)
    mainloop()

def XML_Dump():
    root = ET.Element("Package",xmlns = xmlns)
    for i in range(len(metadata)):
        if(var[i].get()==1):
            types = ET.SubElement(root,"types")
            members = ET.SubElement(types,"members").text = '*'
            name = ET.SubElement(types,"names").text = metadata[i]
            tree = ET.ElementTree(root)
    ET.SubElement(root, "version").text = version
    tree = ET.ElementTree(root)
    tree.write(file_name,encoding=_encoding,xml_declaration=True)

def flow():
    display_setting(500, 400) 
    getConfig()

if __name__ == "__main__":
    flow()