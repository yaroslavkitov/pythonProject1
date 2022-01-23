n = int(input("Введите целое положительное число"))
str_n = str(n)
str_nn = str_n + str_n
str_nnn = str_n + str_n + str_n
x = n + int(str_nn) + int(str_nnn)
print(x)