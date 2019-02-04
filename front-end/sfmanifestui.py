from tkinter import *
import xml.etree.cElementTree as ET
import getChanges as GC
import os
import tkinter.messagebox
import math
import pyperclip
import json
#import the required packages

root = Tk()
# root.geometry("900x900")root.geometry("900x900")
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

    width = 5
    height = math.ceil(14/width)

    for i in range(height):
        for j in range(width):
            var[i] = IntVar()
            Checkbutton(list_block, text=str(metadata[i]), variable=var[i],bg="#252526",fg="#007ACC").grid(row=i,column=j,sticky=W,padx=10,pady=5)

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
    tkinter.messagebox.showinfo("Manifest Creation","Base Manifest package.xml is created, using the selected component")

def XML_DIFF():
    from_v = F_commitID_E.get()
    to_v = T_commitID_E.get()

    GC.check(from_v,to_v)
    root = ET.Element("Package",xmlns = xmlns)
    metadata = []
    if len(GC.getApexClass())>0:
        metadata.append("ApexClass")
    if len(GC.getApexPage())>0:
        metadata.append("ApexPage")
    if len(GC.getTrigger())>0:
        metadata.append("ApexTrigger")

    for i in range(len(metadata)):
            types = ET.SubElement(root,"types")
            print("Current value:\t",metadata[i])
            if metadata[i]=="ApexClass":
                print("Value ApexClass:\t",metadata[i])
                apex_list = GC.getApexClass()
                for o in range(len(GC.getApexClass())):
                    members = ET.SubElement(types,"members").text = str(apex_list[o])
                    print("CLASSES",apex_list[o])
            if metadata[i]=="ApexPage":
                ape_page_list = GC.getApexPage()
                print(ape_page_list)
                for p in range(len(GC.getApexPage())):
                    members = ET.SubElement(types,"members").text = str(ape_page_list[p])
                    # print("CLASSES",apex_list)
            if metadata[i]=="ApexTrigger":
                apex_trigger_list = GC.getTrigger()
                for t in range(len(GC.getTrigger())):
                    members = ET.SubElement(types,"members").text = str(apex_trigger_list[t])
                    print("CLASSES",apex_list)            
            name = ET.SubElement(types,"names").text = metadata[i]
            tree = ET.ElementTree(root)
    ET.SubElement(root, "version").text = version
    tree = ET.ElementTree(root)
    tree.write(file_name,encoding=_encoding,xml_declaration=True)    

def delete_manifest():
    if os.path.exists("package.xml"):
        os.remove("package.xml")
        tkinter.messagebox.showinfo("Deleted","Manifest Package.xml is deleted")
    else:
        tkinter.messagebox.showwarning("File not found","Manifest Package.xml is not found")

def backup_manifest():
    print("Backing up Manifest")
    if os.path.exists("package.xml"):
        os.rename("package.xml","package_backup_1.xml")
        tkinter.messagebox.showinfo("New File","Manifest Package.xml is deleted")
    else:
        print("package.xml")    

def auto_manifest():
    print("Generating the file autoamtically")
    latest_commit = GC.getLatestCommit()
    print("latest Commit",latest_commit)
    deployed_commit = GC.getDeployedCommit()
    print("deployed commit",deployed_commit)

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))
    value = value[0:value.find(" | ")]
    pyperclip.copy(value)

def getcommit():
    print("Get the Commit")
    list_commit_ID = []
    list_commit_ID =GC.getCommitID()
    print(list_commit_ID)

    len_max = 0
    for m in list_commit_ID:
        if len(m)>len_max:
            len_max = len(m)

    Lb = Listbox(rightbar,width=len_max,bg="#252526",fg="#007ACC") 
    Lb.config(highlightbackground="black")
    for i in range(len(list_commit_ID)):
        Lb.insert(i, list_commit_ID[i])
    Lb.bind("<<ListboxSelect>>",onselect)
    Lb.grid(row=1,column=1,padx=20) 
    # Lb.pack(side="left", fill="y")

def flow():
    getConfig()

def exit_f():
    response = tkinter.messagebox.askquestion("Exit","Do you like to quit?")
    if response == "yes":
        root.quit()

# Intialize to set the displayed properties of the application
root.title('Salesforce Manifest Generator')
topbar = Frame(root,bg="#1E1E1E",height=100)
topbar.pack(side=TOP,fill=X)

leftbar = Frame(root,bg="#383838",width=800)
leftbar.pack(side=LEFT,fill=Y)

list_block = Frame(leftbar,bg="#252526",height=300,width=800)
list_block.pack(side=TOP)

rightbar = Frame(root,bg="#333333",width=800)
rightbar.pack(side=LEFT,fill=Y)

CommitIDFrame = Label(rightbar, text="Commit ID List",bg="#252526",fg="#007ACC")
CommitIDFrame.config(width=20)
CommitIDFrame.grid(row=0,column=1,sticky=S, pady=4,padx=10)

gen_base_manifest =  Button(topbar, text='Generate Base Manifest', command=XML_Dump,bg="#007ACC",fg="white")
gen_base_manifest.grid(row=1,column=0,sticky=S, pady=4,padx=10)
  
F_commitID = Label(topbar, text="From Commit ID",bg="#252526",fg="#007ACC")
F_commitID.grid(row=1,column=1,sticky=W,pady=4,padx=10)

F_commitID_E = Entry(topbar, bd=2)
F_commitID_E.grid(row=1,column=2,sticky=W,pady=4,padx=10)

T_commitID = Label(topbar, text="To Commit ID",bg="#252526",fg="#007ACC")
T_commitID.grid(row=1,column=3,sticky=W,pady=4,padx=10)

T_commitID_E = Entry(topbar, bd=2)
T_commitID_E.grid(row=1,column=4,sticky=W,pady=4,padx=10)

gen_changes = Button(topbar, text='Generate on Changes', command=XML_DIFF,bg="#007ACC",fg="white")
gen_changes.grid(row=1,column=5,sticky=W, pady=4,padx=10)

GetCommitID_B = Button(topbar, text='Get Commit ID', command=getcommit,bg="#007ACC",fg="white")
GetCommitID_B.grid(row=1,column=6,sticky=W,pady=4,padx=10)

Delete_Manifest_B = Button(topbar, text='Delete Manifest', command=delete_manifest,bg="#007ACC",fg="white")
Delete_Manifest_B.grid(row=1,column=7,sticky=W,pady=4,padx=10)

Auto_Gen = Button(topbar, text='Auto-Gen-Manifest', command=auto_manifest,bg="#007ACC",fg="white")
Auto_Gen.grid(row=1,column=8,sticky=W,pady=4,padx=10)

Delete_All_Manifest_B = Button(topbar, text='Delete All Manifest', command=delete_manifest,bg="#007ACC",fg="white")
Delete_All_Manifest_B.grid(row=1,column=9,sticky=W,pady=4,padx=10)

Backup_Manifest_B = Button(topbar, text='Backup Manifest', command=backup_manifest,bg="#007ACC",fg="white")
Backup_Manifest_B.grid(row=1,column=10,sticky=W,pady=4,padx=10)

quit_button = Button(topbar, text='Quit', command=exit_f,bg="#007ACC",fg="white")
quit_button.grid(row=1,column=11,sticky=W,pady=4,padx=10,ipadx=10)

if __name__ == "__main__":
    flow()
    mainloop()