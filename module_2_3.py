# Пухаева Алина Александровна
# Code style part II. The While loop.
# 10.09.2024
# Notes: ctrl+alt+L
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_ = 0
while index_ <  len(my_list):
    if my_list[index_] < 0:
        break
    elif my_list[index_] == 0:
        index_ += 1
        continue
    else:
        print(my_list[index_])
    index_ += 1