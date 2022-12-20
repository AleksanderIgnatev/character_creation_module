[33mcommit b41ff653ce9872c8a7f98518cecbf11e3cab48f9[m[33m ([m[1;36mHEAD -> [m[1;32mmain[m[33m, [m[1;31morigin/main[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: Andrew Gorlov <Gorlov.a@mail.ru>
Date:   Tue Aug 30 21:04:57 2022 +0300

    Изменены реплики

[1mdiff --git a/main.py b/main.py[m
[1mindex 1c75598..1f468d6 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -2,73 +2,73 @@[m [mfrom random import randint[m
 [m
 [m
 def attack(char_name, char_class):[m
[31m-    if char_class == 'warior':[m
[31m-        return (f'{char_name} нанес урон противнику равный {5 + randint(3, 5)}')[m
[32m+[m[32m    if char_class == 'warrior':[m
[32m+[m[32m        return (f'{char_name} нанёс урон противнику равный {5 + randint(3, 5)}')[m
     if char_class == 'mage':[m
[31m-        return (f'{char_name} нанес урон противнику равный {5 + randint(5, 10)}')[m
[32m+[m[32m        return (f'{char_name} нанёс урон противнику равный {5 + randint(5, 10)}')[m
     if char_class == 'healer':[m
[31m-        return (f'{char_name} нанес урон противнику равный {5 + randint(-3, -1)}')[m
[32m+[m[32m        return (f'{char_name} нанёс урон противнику равный {5 + randint(-3, -1)}')[m
 def defence(char_name, char_class):[m
[31m-    if char_class == 'warior':[m
[32m+[m[32m    if char_class == 'warrior':[m
         return (f'{char_name} блокировал {10 + randint(5, 10)} урона')[m
     if char_class == 'mage':[m
         return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')[m
     if char_class == 'healer':[m
         return (f'{char_name} блокировал {10 + randint(2, 5)} урона')[m
 def special(char_name, char_class):[m
[31m-    if char_class == 'warior': [m
[31m-        return (f'{char_name} примернил специальное умение  - выпосливось {80 + 25}')[m
[32m+[m[32m    if char_class == 'warrior':[m[41m [m
[32m+[m[32m        return (f'{char_name} применил специальное умение «Выносливость {80 + 25}»')[m
     if char_class == 'mage':[m
[31m-        return (f'{char_name} примернил специальное умение -  атака {5 + 40}')[m
[32m+[m[32m        return (f'{char_name} применил специальное умение «Атака {5 + 40}»')[m
     if char_class == 'healer':[m
[31m-        return (f'{char_name} примернил специальное умение - защита {10 + 30}')[m
[32m+[m[32m        return (f'{char_name} применил специальное умение «Защита {10 + 30}»')[m
 [m
 [m
 [m
 [m
 def start_training(char_name, char_class):[m
     if char_class == 'warrior':[m
[31m-        print(f'{char_name}, ты Воитель - отличный боец ближнего боя.')[m
[32m+[m[32m        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')[m
     if char_class == 'mage':[m
[31m-        print(f'{char_name}, ты Маг - превосходный укротитель стихий.')[m
[32m+[m[32m        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')[m
     if char_class == 'healer':[m
[31m-        print(f'{char_name}, ты Лекарь - чародей способный исцелять раны.')[m
[31m-    print('Теперь можно потренироваться в управлении полученными навыками.')[m
[31m-    print('Введи одну из команд: attack для проведения атаки, defence - блокирование атаки противника и special - активация специальной возможности класса.')[m
[31m-    print('Чтобы пропустить тренировку введите - skip')[m
[32m+[m[32m        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')[m
[32m+[m[32m    print('Потренируйся управлять своими навыками.')[m
[32m+[m[32m    print('Введи одну из команд: attack — чтобы атаковать противника, defence — чтобы блокировать атаку противника или special — чтобы использовать свою суперсилу.')[m
[32m+[m[32m    print('Если не хочешь тренироваться, введи команду skip.')[m
     cmd = None[m
     while cmd != 'skip':[m
[31m-        cmd = input('Введите команду: ')[m
[32m+[m[32m        cmd = input('Введи команду: ')[m
         if cmd == 'attack':[m
             print(attack(char_name, char_class))[m
         if cmd == 'defence':[m
             print(defence(char_name, char_class))[m
         if cmd == 'special':[m
             print(special(char_name, char_class))[m
[31m-    return 'Тренировка окончена'[m
[32m+[m[32m    return 'Тренировка окончена.'[m
 [m
 def choice_char_class():[m
     approve_choice = None[m
     char_class = None[m
     while approve_choice != 'y':[m
[31m-        char_class = input('Для выбора класса персонажа введите его название (warrior, mage, healer): ')[m
[32m+[m[32m        char_class = input('Введи название персонажа, за которого хочешь играть: Воитель — warrior, Маг — mage, Лекарь — healer: ')[m
         if char_class == 'warrior':[m
[31m-            print('Описание воителя ....')[m
[32m+[m[32m            print('Воитель — дерзкий воин ближнего боя. Сильный, выносливый и отважный.')[m
         if char_class == 'mage':[m
[31m-            print('Описание мага ....')[m
[32m+[m[32m            print('Маг — находчивый воин дальнего боя. Обладает высоким интеллектом.')[m
         if char_class == 'healer':[m
[31m-            print('Опиание лекаря ....')[m
[31m-        approve_choice = input('Подтвердите (Y) или повторите (any key) выбор ').lower()[m
[32m+[m[32m            print('Лекарь — могущественный заклинатель. Черпает силы из природы, веры и духов.')[m
[32m+[m[32m        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, чтобы выбрать другого персонажа ').lower()[m
     return char_class[m
 [m
 [m
 def main():[m
[31m-    print('Приветствую тебя искатель приключений!')[m
[31m-    print('Прежде чем войти в игру')[m
[31m-    char_name = input('Назови себя: ')[m
[32m+[m[32m    print('Приветствую тебя, искатель приключений!')[m
[32m+[m[32m    print('Прежде чем начать игру...')[m
[32m+[m[32m    char_name = input('...назови себя: ')[m
     print(f'Здравствуй, {char_name}! '[m
[31m-          'Сейчас твоя выносливость 80, атака 5 и защита 10.')[m
[31m-    print('Но ты можешь выбрать один из трех путей силы.')[m
[32m+[m[32m          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')[m
[32m+[m[32m    print('Ты можешь выбрать один из трёх путей силы:')[m
     print('Воитель, Маг, Лекарь')[m
     char_class = choice_char_class()[m
     print(start_training(char_name, char_class))[m
