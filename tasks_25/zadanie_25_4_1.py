# кратен 5 7 13 и не кратен хотя бы одному из квадратов этого числа, делитель не превышающий 100000
# делитель не может быть единицей или самим собой и делитель оканчивается на 19
# array1 = []  # Числа из основного диапозона
# # array2 = []  # Числа после фильтрации по условию. Теперь с этими числами нужно работать.
# # array3 = []  #
#
# divider = 1
#
# # for i in range(224466, 664422+1):
# #     array1.append(i)
# # print(array1)
#
# for j in range(224466, 664422+1):
#     if j % 5 == 0 and j % 7 == 0 and j % 13 == 0 and (j % 25 != 0 or j % 49 != 0 or j % 169 != 0):
#         array1.append(j)
#
# print(array1)
# print(len(array1))  # 965 - несостыковка с первой версией
# # print(len(array2)) 611
for i in range(224466, 664422+1):
    if i % 5 == 0 and i % 7 == 0 and i % 13 == 0:
        if i % 25 != 0 or i % 25 != 0 or i % 169 != 0:
            for j in range(2, i):
                if i % j == 0:
                    m = j
            if m <= 100000 and m % 100 == 19:
                print(i, m)
