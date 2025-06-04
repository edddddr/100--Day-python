
# Describe problem
# def my_function():
#     for n in range(1,21):
#         if n == 20:
#             print("You got it")

# my_function()


# Reproduce the Bug
# from random import randint
# dice_imgs = ['1️', ' 2️⃣', '3️⃣', '4️⃣','5️⃣', '6️⃣']
# dice_num = randint(1,5)
# print(dice_num)
# print(dice_imgs[dice_num])


# Play with computer
# year = int(input("What is year of birth? "))
# if year > 1980 and year < 1994:
#     print("you are mellenial.")
# elif year >= 1994:
#     print("You are Gen Z. ")

# Fix the Error
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}")

# Fix the Bug with print method
# pages = 0
# word_per_page = 0
# page = int(input("Number of page : "))
# word_per_page = int(input("Number of words per page: "))
# total_words = page * word_per_page
# print(total_words)

# Use a debuger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)

mutate([1,2,3,4,8,13])
        