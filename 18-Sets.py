# Sets = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "spoon"}
# utensils.add("napkin")
# utensils.remove("spoon")
# utensils.clear()
# menambahkan data dishes ke utensils
# utensils.update(dishes)
# menggabungkan
dinnertable = utensils.union(dishes)
# mencari data apa yang ada didishes tetapi tidak ada di utensils/perbedaan
print(utensils.difference(dishes))
print(utensils.intersection(dishes))
# for x in utensils:
#     print(x)