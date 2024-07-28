import os
import shutil

path = "testing.txt"
try:
    os.remove(path) #delete a file
    os.rmdir(path) #delete an empty directory
    shutil.rmtree(path) #delete a dictionary constanning
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have pemrmission to delete that")
except OSError:
    print("You can not delete that using function")
else:
    print(path+" was deleted")