# importing os.path module
import os.path
from typing import List

# Path
path = 'C:/Users/shaha/Desktop/Python/pythonProject1/trial/tuition/merge'

# Check whether the
# specified path is an
# existing directory or not
isdir = os.path.isdir(path)
print(isdir)
dir = os.listdir(path)
listFileName: list[str]=[]
if len(dir) != 0:
    for fileName in dir:
        fileExtension = os.path.splitext(fileName)[1]
        if (fileExtension == '.pdf'):
            listFileName.append(fileName)
    print(listFileName)
else:
    print("Empty directory")
