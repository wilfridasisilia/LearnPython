# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to devide: "))
    denominator = int(input("Enter a nnumber to devide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't devide by zero! Idiot!")
except ValueError as e:
    print("Enter only numbers please")
except Exception:
    print("something went wrong!!")
else:
    print(result)
finally:
    print("This will always execute ")