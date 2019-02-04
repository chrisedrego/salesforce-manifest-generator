import subprocess
import sys

#oldest
_from = ""
#latest
_to = ""


apex_cls = []
apex_page = []
trigger = []

def check(_from,_to):
    _list = getdiff(_from,_to)
    global apex_cls
    global apex_page
    global trigger
    print(_list)
    for i in range(len(_list)):
        if str(_list[i]).endswith('.cls'):
            apex_cls.append(str(_list[i]))
        if str(_list[i]).endswith('.page'):
            apex_page.append(str(_list[i]))  
        if str(_list[i]).endswith('.trigger'):
            trigger.append(str(_list[i]))      

def getdiff(_from,_to):
    cmd = "git diff "+_from+" "+_to+" --name-only"
    returned_output  = subprocess.check_output(cmd,shell=True)
    data = returned_output.decode("utf-8")
    # print("FILE CHANGED" +data)
    print(data)
    _list = []
    _list = data.split()
    return _list

def getCommitID():
    cmd = "git log --pretty=format:%h\" | \"%s"
    returned_output  = subprocess.check_output(cmd,shell=True)
    data = returned_output.decode("utf-8")
    _list = []
    _list = data.split("\n")
    return _list

def getSubject():
    _list = []
    cmd = "git log --pretty=format:\"%s\""
    returned_output  = subprocess.check_output(cmd,shell=True)
    data = returned_output.decode("utf-8")
    print(data)
    _list = data.split("\n")
    return _list

def getLatestCommit():
    _list = getCommitID()
    return _list[0] 

def getDeployedCommit():
    _list = getCommitID()
    return _list[1]

def getApexClass():
    apex_cls_f = []
    for i in range(len(apex_cls)):
        apex_cls_f.append(apex_cls[i][0:apex_cls[i].find('.cls')])
    return apex_cls_f

def getTrigger():
    trigger_f = []
    for i in range(len(trigger)):
        trigger_f.append(trigger[i][0:trigger[i].find('.trigger')])
    return trigger_f

def getApexPage():
    apex_page_f = []
    for i in range(len(apex_page)):
        apex_page_f.append(apex_page[i][0:apex_page[i].find('.page')])
    return apex_page_f

# git log --pretty=format:"%h"

# getCommitID()
# getLatestCommit()
########################################################
# CHCK_OU = str(subprocess.check_output(cmd,shell=True))
# print("CHECKOUT: "+CHCK_OU)

# print("RUN: "+str(subprocess.run(cmd,shell=True)))

# print("CALL: "+str(subprocess.call(cmd,shell=True)))
