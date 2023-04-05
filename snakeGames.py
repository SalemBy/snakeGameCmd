from pytimedinput import timedInput
from sys import platform
from random import randint
from colorama import Fore, init
import os
# python "C:\Users\Usuario\OneDrive\Estudos\Programação\Python\Projetos\Snake Game\snakeGames.py"


def createField():
    for cell in CELLS:
        
        if cell in body:
            print(Fore.GREEN + 'X', end='')
        
        elif cell[0] in (0, FILD_WIDTH - 1) or cell[1] in (0,FILD_HEIGTH - 1):
            print('#', end='')

        elif cell == applePosition:
            print(Fore.RED + 'a', end='')
        
        else:
            print(' ', end= '')

        if cell[0] == FILD_WIDTH- 1:
            print('')


def reloadSnake():
    global eaten
    newHead = body[0][0] + direction[0], body[0][1] + direction[1]
    body.insert(0,newHead)
    if not eaten: body.pop(-1)
    eaten = False

def newApple():
    col = randint(1,FILD_WIDTH - 2)
    row = randint(1, FILD_HEIGTH - 2)
    while (col, row) in body:
        
        col = randint(1,FILD_WIDTH - 2)
        row = randint(1, FILD_HEIGTH - 2)
    return (col, row)

def appleCollision():
    global applePosition, eaten
    if applePosition == body[0]:
        applePosition = newApple()
        eaten = True

init(autoreset= True)


# Fild
FILD_WIDTH = 32
FILD_HEIGTH = 16
CELLS = [(col,row) for row in range(FILD_HEIGTH) for col in range(FILD_WIDTH)]
if platform == "win32" or platform == "cygwin":
	clearcmd = "cls"
else:
	clearcmd = "clear"


# Snake
body = [(5, FILD_HEIGTH // 2),(4, FILD_HEIGTH // 2),(3, FILD_HEIGTH // 2)]
DIRECTIONS = {'left': (-1,0), 'right': (1,0), 'up': (0,-1), 'down': (0,1)}
direction = DIRECTIONS['right']
eaten = False

# Apple
applePosition = (5,10)




while True:
    # Clear Terminal
    os.system(clearcmd)

    # Creating Field
    createField()

    # Controls
    txt,_ = timedInput('input:', timeout= 0.3)
    match txt:
        case 'w': 
            direction = DIRECTIONS['up']
       
        case 'a':
            direction = DIRECTIONS['left']
       
        case 's':
            direction = DIRECTIONS['down']
        
        case 'd':
            direction = DIRECTIONS['right']
       
        case 'q':
            os.system(clearcmd)
            break

    # Reload Game
    reloadSnake()
    appleCollision()

    # Game Over
    if body[0][0] in (0, FILD_WIDTH - 1) or body[0][1] in (0, FILD_HEIGTH - 1) or body[0] in body[1:]:
        os.system(clearcmd)
        print('YOU LOSE') 
        break



    