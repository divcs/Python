# 1 func taking args and returning a value
def findMax(a, b):
    if a > b:
        return a
    else:
        return b


print("Max number between 100 and 20 is ", findMax(100, 20))


# 2 func with default arg
def hello(name, msg=" , how are you?"):
    print("Hello", name, msg)


hello("Divya", ",have a nice day.")
hello("Divya")
