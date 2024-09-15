

new_message = "Hello World, How are you ? "

with open("myfile.txt",'a') as file:
    file.write(new_message)