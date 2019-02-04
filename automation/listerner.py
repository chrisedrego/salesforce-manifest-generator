import subprocess
import os
import time
import json
import os.path


def branch_comparison(old_branch_list,new_branch_list):
    return sorted(old_branch_list) == sorted(new_branch_list)

def scratch_org_init():
    time.sleep(30)
    os.system("sfdx force:org:create -f project-scratch-def.json")

def compare():
    temp_branch_list = gitbranchcheck()
    print("Old Branch:\t",temp_branch_list)

    while(True):
        new_branch_list = gitbranchcheck()
        time.sleep(1)
        if(branch_comparison(temp_branch_list,new_branch_list)):
            print("Branch is equal")
            print("Contents of Old:",temp_branch_list)
            print("Contents of New:",new_branch_list)
        else:
            print("Contents of the branch are not equal")
            print("Contents of Old:",temp_branch_list)
            print("Contents of New:",new_branch_list)

if __name__ == "__main__":
    gitbranchcheck()