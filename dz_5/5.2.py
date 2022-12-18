# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def input_sweet(name):
    x = int(input(f"{name}, какое количество конфет возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, вы ввели неверное количество конфет: "))
    return x


def massage_print(name, k, counter, max):
    print(f"Игрок {name} взял {k}, и теперь у него {counter}. Осталось {max} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
max = 2021

flag = randint(0,2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while max > 28:
    if flag:
        k = input_sweet(player1)
        counter1 += k
        max -= k
        flag = False
        massage_print(player1, k, counter1, max)
    else:
        k = input_sweet(player2)
        counter2 += k
        max -= k
        flag = True
        massage_print(player2, k, counter2, max)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

