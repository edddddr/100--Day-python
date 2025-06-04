
# Describe problem
# def my_function():
#     for n in range(1,21):
#         if n == 20:
#             print("You got it")

# my_function()


# Reproduce the Bug
from random import randint
dice_imgs = ['1️', ' 2️⃣', '3️⃣', '4️⃣','5️⃣', '6️⃣']
dice_num = randint(1,5)
print(dice_num)
print(dice_imgs[dice_num])
