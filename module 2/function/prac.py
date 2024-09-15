def multiplication_table():
    for number in range(1, 11): 
        print(f"Multiplication Table for {number}:")
        for i in range(1, 11): 
            result = number * i
            print(f"{number} x {i} = {result}")
        print("")  

multiplication_table()
