try:
    with open('test.tx') as file:
        print(file.read()) #close file automatically
except FileNotFoundError:
    print("File tidak ditemukan")
