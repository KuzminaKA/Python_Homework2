#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
#Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

S = int(input("введите сумму загаданных чисел: "))
P = int(input("введите произведение загадагных чисел: "))
for x in range(1,1000):
    for y in range(1,1000):
        if x+y==S and x*y==P:
            print(x, y)
            break