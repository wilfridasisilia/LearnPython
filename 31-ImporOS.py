import os
path = "C:\\Users\\user\\PycharmProjects\\LearnPython"
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("that is a directory!")
else:
    print("That location doesn't exists")