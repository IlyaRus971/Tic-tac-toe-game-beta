#Beta version V1.1 Tic-tac-Toe game from https://github.com/IlyaRus971 
import random



print("+------------------------+")
print("|        КРЕСТИКИ        |")
print("|           +            |")
print("|         НОЛИКИ         |")
print("+------------------------+")
print()
print("Выберите режим игры:")
print("1. Битва с ботом")
print("2. Битва двух героев")
a = int(input("Введите число режима [1/2]:"))

#База знаков 
cells = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)]

#Поле для вывода в терминал
def primer():
    print(f"{cells[0]:^3}|{cells[1]:^3}|{cells[2]:^3}")
    print("-----------")
    print(f"{cells[3]:^3}|{cells[4]:^3}|{cells[5]:^3}")
    print("-----------")
    print(f"{cells[6]:^3}|{cells[7]:^3}|{cells[8]:^3}")

#Проверка на победу 
def check_win(cells):                              #По кортежам проверяем вариации победы
   for a,b,c in wins:
        if cells[a] == cells[b] == cells[c] and cells[a] not in "012345678":
            return cells[a]
        
            
#Проверка на занятость клетки 
def check_kletka(cells, date):
    if cells[date] == "X" or cells[date] == "O":
        print(f"Клетка под номером {date} занята, выбери другую!")
        return True

#Проверка на ничью 
def nowinbro(cells):
    basebro = 0
    for z in range(0, 8 + 1):
        if cells[z] not in "0123456789":
            basebro += 1
    if basebro == 9:    
        return "НИЧЬЯ!"
    return None

#БОТ 1 режим 
def bot(cells, sign, sign2):
    for a, b, c in wins:
        line = [cells[a], cells[b], cells[c]]
        base = []
        if line.count(sign) == 0 and line.count(sign2) == 2:  #OO-
            if cells[a] in "012345678":
                return a
            elif cells[b] in "012345678":
                return b
            elif cells[c] in "012345678":
                return c   
        elif line.count(sign) == 2 and line.count(sign2) == 0:
            for i in [a,b,c]:
                if cells[i] in "012345678":
                    return i
        elif line.count(sign) == 1 and line.count(sign2) == 1:    #XO-
            continue
        for i in range(0, 8 + 1):
            if cells[i] in "012345678":
                base.append(i)
        a = random.choice(base)
        return a
                
        

    
                

            



if a == 1:
    sign = str(input("Введите символ, за который хотите сыграть [X/O]:"))
    if sign == "X" or sign == "x":
        sign2 = "O"
        print("ВЫ ВЫБРАЛИ X")
        print()
    elif sign == "O" or sign == "o":
        sign2 = "X"
        print("ВЫ ВЫБРАЛИ O")
        print()
    random1 = random.randint(0, 1)
    td = True
    if random1 == 0:
        print(f"---- ХОД БОТА [{sign2}] ----")
        date2 = random.randint(0, 8)
        for i in range(0, 8 + 1): 
            if date2 == i:
                cells[i] = sign2
        primer()

        while td:
            print(f"---- ВАШ ХОД [{sign}] ----")
            primer()
            date = int(input("Введите номер клетки:"))
            if check_kletka(cells, date):
                continue
                            
            for i in range(0, 8 + 1):  #Цикл выбора строки 
                if date == i:
                    cells[i] = sign
            winner = check_win(cells)
            if winner:
                td = False
                print("----------------------------------")
                primer()
                print(f"Победил {winner}!")
                print("----------------------------------")
            if nowinbro(cells):                             #Проверка на ничью
                td = False
                print("----------------------------------")
                primer()
                print("Ничья, игра окончена.")
                print("----------------------------------")
        
            while td:
                print(f"---- ХОД БОТА [{sign2}] ----") 
                
                date = bot(cells, sign, sign2)
                            
                if check_kletka(cells, date):
                    continue
                for i in range(0, 8 + 1):
                    if date == i:
                        cells[i] = sign2
                primer()            
                winner = check_win(cells)
                if winner:
                    td = False
                    print("----------------------------------")
                    primer()
                    print(f"Победил {winner}!")
                    print("----------------------------------")
                if nowinbro(cells):                          #проверка на ничью
                    td = False
                    print("----------------------------------")
                    primer()
                    print("Ничья, игра окончена.")
                    print("----------------------------------")
                    break
                break

    elif random1 == 1:
        while td:
            print(f"---- ВАШ ХОД [{sign}] ----")
            primer()
            date = int(input("Введите номер клетки:"))
            if check_kletka(cells, date):
                continue          
            for i in range(0, 8 + 1):  #Цикл выбора строки 
                if date == i:
                    cells[i] = sign
            winner = check_win(cells)
            if winner:
                td = False
                print("----------------------------------")
                primer()
                print(f"Победил {winner}!")
                print("----------------------------------")
            if nowinbro(cells):                             #Проверка на ничью
                td = False
                print("----------------------------------")
                primer()
                print("Ничья, игра окончена.")
                print("----------------------------------")
#--------------------------------------------------------------------------------------#
            while td:
                print(f"---- ХОД БОТА [{sign2}] ----") 
                
                date = bot(cells, sign, sign2)
                    
                if check_kletka(cells, date):
                    continue
                for i in range(0, 8 + 1):
                    if date == i:
                        cells[i] = sign2
                primer()    
                winner = check_win(cells)
                if winner:
                    td = False
                    print("----------------------------------")
                    primer()
                    print(f"Победил {winner}!")
                    print("----------------------------------")
                if nowinbro(cells):                          #проверка на ничью
                    td = False
                    print("----------------------------------")
                    primer()
                    print("Ничья, игра окончена.")
                    print("----------------------------------")
                    break
                break




else:
    tf = True
#--------------------------------------------------------------------------------------#
    while tf:                    #Начало цикла 
        print("---- ХОД ИГРОКА X ----") 
        primer()
        date = int(input("Введите номер клетки:"))
        if check_kletka(cells, date):
            continue
        
        for ix in range(0, 8 + 1):  #Цикл выбора строки X
            if date == ix:
                cells[ix] = "X"
        winner = check_win(cells)
        if winner:
            tf = False
            print("----------------------------------")
            primer()
            print(f"Победил {winner}!")
            print("----------------------------------")
        if nowinbro(cells):                             #Проверка на ничью
            tf = False
            print("----------------------------------")
            primer()
            print("Ничья, игра окончена.")
            print("----------------------------------")

#-------------------------------------------------------------------------------------#
        while tf:
            print("---- ХОД ИГРОКА O ----") 
            primer()
            date = int(input("Введите номер клетки:"))
        
            if check_kletka(cells, date):
                continue
       
            for io in range(0, 8 + 1):  #Цикл выбора строки O
                if date == io:
                    cells[io] = "O"
        
            winner = check_win(cells)
            if winner:
                tf = False
                print("----------------------------------")
                primer()
                print(f"Победил {winner}!")
                print("----------------------------------")
            if nowinbro(cells):                          #проверка на ничью
                tf = False
                print("----------------------------------")
                primer()
                print("Ничья, игра окончена.")
                print("----------------------------------")
            break
#------------------------------------------------------------------------------------#
