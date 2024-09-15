# a = 10
# b = 2

# print(a/b)


a = int(input("Enter a number"))
b = int(input("Enter the second number"))
# print(a/b)

try: 
    ans = a/b
    print (ans)
except Exception as e:
    print(e)


finally: # finally block ma exceptional handling bhayeni nabhayeni run huncha
    print("Hello World")

