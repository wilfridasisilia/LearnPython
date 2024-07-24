# Tuple = collection which is ordered and unchangeable
# used to group together related data

student = ("Frida",19,"Female")
# menghitung seberapa banyak muncul
print(student.count("Frida"))
# index ke berapa data yg dicari
print(student.index("Female"))

for x in student:
    print(x)
if "Frida" in student:
    print("Frida is here")