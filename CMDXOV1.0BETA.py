#Beta version V1.0 Tic-tac-Toe game from https://github.com/IlyaRus971 
print("+------------------------+")
print("|        КРЕСТИКИ        |")
print("|           +            |")
print("|         НОЛИКИ         |")
print("+------------------------+")
print()
print("Выберите режим игры:")
print("1. Битва с ИИ (в разработке)")
print("2. Битва двух героев")
a = int(input("Введите число режима [1/2]:"))

#База знаков 
cells = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

#Поле для вывода в терминал
def primer():
    print(f"{cells[0]:^3}|{cells[1]:^3}|{cells[2]:^3}")
    print("-----------")
    print(f"{cells[3]:^3}|{cells[4]:^3}|{cells[5]:^3}")
    print("-----------")
    print(f"{cells[6]:^3}|{cells[7]:^3}|{cells[8]:^3}")

#Проверка на победу 
def check_win(cells):                              #По кортежам проверяем вариации победы
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
            (0, 3, 6), (1, 4, 7), (2, 5, 8), 
            (0, 4, 8), (2, 4, 6)]

    for a,b,c in wins:
                if cells[a] == cells[b] == cells[c] and cells[a] not in "012345678":
                    return cells[a]
    return None
            
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

if a == 1:
    print("В разработке!")
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