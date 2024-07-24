# nested loops = the "inner loop" will be finish all of it's iterations
# before finishing one iteration of the "outer loop"

rows = int(input("How Many Rows?: "))
columns = int(input("How Many Columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()