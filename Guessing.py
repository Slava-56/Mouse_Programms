import time #Импорт библиотеки

print("") #Небольшой отступ
print("") #Небольшой отступ
print("!?_Угадайка_?!") #Название игры
print("") #Небольшой отступ

num = 56 #Загаданное число

while True:

    UserNum = int(input("Введите число: ")) #Получение от пользователя числа

    if UserNum == num:
        print("") #Небольшой отступ
        print("Число угадано! Вы победили!!!")
        print("") #Небольшой отступ
        break

    elif UserNum < num:
        print("") #Небольшой отступ
        print("Загаданное число побольше вашего.")
        print("") #Небольшой отступ

    else:
        print("") #Небольшой отступ
        print("Загаданное число поменьше вашего.")
        print("") #Небольшой отступ


print("") #Небольшой отступ
print("Я на github: https://github.com/Slava-56 ")
print("") #Небольшой отступ

time.sleep(3) #Задержка с помощью библиотеки time
