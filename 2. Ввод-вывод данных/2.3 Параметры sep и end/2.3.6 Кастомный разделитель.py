# Напишите программу, которая считывает строку-разделитель и три строки,
# а затем выводит указанные строки через разделитель.
#
# Формат входных данных
# На вход программе подаётся строка-разделитель и три строки, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести введённые три строки через разделитель.

s1, s2, s3, s4 = input(), input(), input(), input()
print(s2, s3, s4, sep=s1)