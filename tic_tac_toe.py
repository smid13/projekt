rules = """
Each player can place one mark (or stone)
per turn on the board. You can choose size
of the board. The WINNER is who succeeds 
in placing their marks in a:
* horizontal,
* vertical or
* diagonal row
"""


def welcome():
    mezera = " "
    oddelovac = "="
    print(f"{mezera * 14}Welcome to Tic Tac Toe")
    print(f"{oddelovac * 50}")
    print(f"{mezera * 20}GAME RULES")
    print(oddelovac * 50)
    print(rules)
    print(oddelovac * 50)

welcome()
oddelovac = 50 * "="
player_1 = input("Player 1 name: ")
print(oddelovac)
player_2 = input("Player 2 name: ")
print(oddelovac)
mark_1 = input(f"Greetings {player_1} choose your mark (must contain only one character): ")
print(oddelovac)
while len(mark_1) > 1:
    print("MUST BE ONLY ONE CHARACTER")
    mark_1 = input(f"{player_1} choose your mark: ")
mark_2 = input(f"Greetings {player_2} choose your mark (must contain only one character): ")
print(oddelovac)
while len(mark_2) > 1:
    print("MUST BE ONLY ONE CHARACTER")
    mark_2 = input(f"{player_2} choose your mark: ")
zadani_poli = input("Choose the board size(for 3x3 enter 3): ")
print(oddelovac)
while zadani_poli.isalpha():
    print("MUST BE DIGIT")
    zadani_poli = input("Choose your board(for 3x3 enter 3): ")
zadani_poli = int(zadani_poli)
pocet_poli = zadani_poli * zadani_poli


list_slovniku = []
def vytvoreni_slovniku():
    for i in range(zadani_poli):
        for i in range(zadani_poli):
            i = dict()
            list_slovniku.append(i)


def vytvoreni_radku(list_slovniku):
    for i in range(len(list_slovniku)):
        list_slovniku[i].setdefault(i + 1, " ")


vytvoreni_slovniku()
vytvoreni_radku(list_slovniku)


# tisk tabulky
def tisk_tabulky():
    seznam_hodnot = []
    a = 1
    for i in list_slovniku:
        seznam_hodnot.append(i.get(a))
        a += 1
    oddelovac = "+---"
    a = 0
    b = zadani_poli
    for i in range(zadani_poli):
        print(f"{oddelovac * zadani_poli}" + "+")
        tisk = seznam_hodnot[a:b]
        print("|" + "", "   ".join(tisk) + " |")
        a = a + zadani_poli
        b = b + zadani_poli
    print(f"{oddelovac * zadani_poli}" + "+")


def kontrola_sloupce_pl_1():
    for a in range(zadani_poli):
        for i in range(zadani_poli):
            if list_slovniku[a][a + 1] == mark_1:
                a += zadani_poli
            else:
                continue
            if i == zadani_poli - 1:
                print(f"{player_1.upper()} IS WINNER")
                exit()


def kontrola_sloupce_pl_2():
    for a in range(zadani_poli):
        for i in range(zadani_poli):
            if list_slovniku[a][a + 1] == mark_2:
                a += zadani_poli
            else:
                continue
            if i == zadani_poli - 1:
                print(f"{player_2.upper()} IS WINNER")
                exit()


def kontrola_radku_pl_1():
    a = 0
    for d in range(zadani_poli):
        for i in range(zadani_poli):
            if list_slovniku[a][a + 1] == mark_1:
                a += 1
            else:
                continue
            if i == zadani_poli - 1:
                print(f"{player_1.upper()} IS WINNER")
                exit()
        a += zadani_poli


def kontrola_radku_pl_2():
    a = 0
    for d in range(zadani_poli):
        for i in range(zadani_poli):
            if list_slovniku[a][a + 1] == mark_2:
                a += 1
            else:
                continue
            if i == zadani_poli - 1:
                print(f"{player_2.upper()} IS WINNER")
                exit()
        a += zadani_poli

def kontrola_diagonaly_pl_1():
    a=0
    b=2
    for i in range(zadani_poli):
        if list_slovniku[a][a+1] == mark_1:
            a+= zadani_poli+1
        else:
            continue
        if i == zadani_poli - 1:
            print(f"{player_1.upper()} IS WINNER")
            exit()
    for i in range(zadani_poli):
        if list_slovniku[b][b+1] == mark_1:
             b += zadani_poli-1
        else:
            continue
        if i== zadani_poli - 1:
            print(f"{player_1.upper()} IS WINNER")
            exit()

def kontrola_diagonaly_pl_2():
    a=0
    b=2
    for i in range(zadani_poli):
        if list_slovniku[a][a+1] == mark_2:
            a+= zadani_poli+1
        else:
            continue
        if i == zadani_poli - 1:
            print(f"{player_2.upper()} IS WINNER")
            exit()
    for i in range(zadani_poli):
        if list_slovniku[b][b+1] == mark_1:
             b += zadani_poli-1
        else:
            continue
        if i== zadani_poli - 1:
            print(f"{player_2.upper()} IS WINNER")
            exit()



def kontrola_pl_1():
    kontrola_radku_pl_1()
    kontrola_sloupce_pl_1()
    kontrola_diagonaly_pl_1()

def kontrola_pl_2():
    kontrola_radku_pl_2()
    kontrola_sloupce_pl_2()
    kontrola_diagonaly_pl_2()

def game():
    pocet_tahu = pocet_poli // 2
    game_number = 0
    oddelovac = 40 * "="
    for i in range(pocet_tahu + 1):
        print(oddelovac)
        tah_1 = input(f"{player_1} Please enter your move number: ")
        print(oddelovac)
        while tah_1.isalpha():
            print("MUST BE DIGIT")
            tah_1 = input(f"{player_1} Please enter your move number: ")
        tah_1 = int(tah_1)
        while tah_1 == 0 or tah_1 > pocet_poli:
            tah_1 = int(input("Your move is out of board, move to which place?: "))
        if list_slovniku[tah_1 - 1][tah_1] == " ":
            list_slovniku[tah_1 - 1][tah_1] = mark_1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        tisk_tabulky()
        game_number += 1
        if game_number == pocet_poli:
            print("GAME OVER, IT'S DRAW")
            exit()
        kontrola_pl_1()
        print(oddelovac)
        tah_2 = input(f"{player_2} Please enter your move number: ")
        print(oddelovac)
        while tah_2.isalpha():
            print("MUST BE DIGIT")
            tah_2 = input(f"{player_2} Please enter your move number: ")
        tah_2 = int(tah_2)
        while tah_2 == 0 or tah_2 > pocet_poli:
            tah_2 = int(input("Your move is out of board, move to which place?: "))
        while list_slovniku[tah_2 - 1][tah_2] == mark_1:
            tah_2 = int(input("That place is already filled.\nMove to which place?: "))
        list_slovniku[tah_2 - 1][tah_2] = mark_2

        tisk_tabulky()
        game_number += 1
        if game_number == pocet_poli:
            print("GAME OVER, IT'S DRAW")
            exit()
        kontrola_pl_2()



tisk_tabulky()
game()
