# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
print(food)
print(food[1])
food[0] = "sushi"
print(food)

# nambahin data
food.append("ice cream")
# menghapus data / remove bisa memilih
food.remove("pudding")
# menghapus data dengan ketentuan / pop
food.pop()
# menambah data
food.insert(3, "sashimi")
# sort / mengurutkan list sesuai alphabet
food.insert(2, "bakso")
# mengapus data secara keseluruhan
food.clear()
for i in food:
    print(i)