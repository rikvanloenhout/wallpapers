import os
import subprocess

directory = "./src"

processes = {}

for filename in os.listdir(directory):
    if filename.endswith(".asm") or filename.endswith(".py"): 
        print("[ ] " + os.path.splitext(os.path.basename(filename))[0])
        processes[filename] = subprocess.Popen(['python', os.path.join(directory,filename)])


while True:
    for filename in processes:
        state = processes[filename].poll()
        if state is not None:
            processes.remove(filename)
            print('done', filename)

    if len(processes) < 1:
        break

        