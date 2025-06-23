# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     file.close()

with open("my_file.txt", mode='w') as file:
    file.write('\n New text')