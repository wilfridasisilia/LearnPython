# copyfile() = copies content of a file
# copy() = copyfile + permission mode + destination can be directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil
shutil.copy2('test.txt', 'C:\\Users\\user\\PycharmProjects\\LearnPython\\copy2.txt') #src,dst(destination)