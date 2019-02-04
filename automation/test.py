import subprocess

local_branch_list = []
local_branches = subprocess.check_output("git branch -l",shell=True).decode("utf-8")
local_branch_list = local_branches.split("\n")

for i in range(len(local_branch_list)):
    local_branch_list[i] = local_branch_list[i].strip()
    if local_branch_list[i].startswith('* '):
        print(local_branch_list[i])
        local_branch_list[i] = local_branch_list[i][2:(len(local_branches)-1)]
    
del local_branch_list[len(local_branch_list)-1]
    
print(local_branch_list)