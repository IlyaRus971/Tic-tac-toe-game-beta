a = int(input("Режим игры(1/2):"))

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

if a == 1:
    print("В разработке!")
else:
    tf = True
    while tf:                                     #Начало цикла 
        print("---- ХОД ИГРОКА X ----") 
        primer()
        date = int(input("Введите номер клетки:"))
        print(f"logs -> Игрок X ввел: {date}")
        if check_kletka(cells, date):
            continue
        
        
                
        if date == 0:     #0
            cells[0] = "X"

        elif date == 1:   #1
            cells[1] = "X"

        elif date == 2:   #2
            cells[2] = "X"
            
        elif date == 3:   #3
            cells[3] = "X"

        elif date == 4:   #4
            cells[4] = "X"

        elif date == 5:   #5
            cells[5] = "X"

        elif date == 6:   #6
            cells[6] = "X"

        elif date == 7:   #7
            cells[7] = "X"

        elif date == 8:   #8
            cells[8] = "X"

        winner = check_win(cells)
        if winner:
            tf = False
            print(f"Победил {winner}!")


        print("---- ХОД ИГРОКА O ----") 
        primer()
        date = int(input("Введите номер клетки:"))
        
        if check_kletka(cells, date):
            continue
       

        if date == 0:     #0
            cells[0] = "O"
        
        elif date == 1:   #1
            cells[1] = "O"
        
        elif date == 2:   #2
            cells[2] = "O"
                    
        elif date == 3:   #3
            cells[3] = "O"
        
        elif date == 4:   #4
            cells[4] = "O"
        
        elif date == 5:   #5
            cells[5] = "O"
        
        elif date == 6:   #6
            cells[6] = "O"
        
        elif date == 7:   #7
            cells[7] = "O"
        
        elif date == 8:   #8
            cells[8] = "O"
        
        winner = check_win(cells)
        if winner:
            tf = False
            print(f"Победил {winner}!")
        

