# Loop Control Statement = change a loops execution from it's normal sequence

# break = used to terminate the loop entirely
# continue = skip to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break
#
# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == "-":
#         continue
#     #     end="" biar tulisan print ke samping bukan ke bawah
#     print(i, end="")

for i in range(1, 21):
    if i == 15:
        pass # melewatkan

    else:
        print(i)