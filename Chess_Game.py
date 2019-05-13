from IPython.display import clear_output
import pygame
from pygame.locals import *
import os

###################################
# CLASSES #                       #
###################################

class Peon():

    def __init__(self,location):
        self.location = location
    
    def check_move():


        return
    def move():
        return ''

class Tower():

    def __init__(self,parameter):
        self.parameter = parameter
        
    def Move():
        return ''





###################################
# FUNCTIONS #                     #
###################################

#Asks the Player 1 to choose between White or Black
def player_input():
    '''
    DEFINITION: Asks the Player 1 to choose between White or Black
    OUTPUT:     ('','')
    '''
    marker = ('','')
    answer_input = ''
    while answer_input != 'W' and answer_input != 'B':
        answer_input = input('Player 1, choose a color to start: White (W) or Black (B)').upper
        if answer_input == 'W':
            marker = ('W','B')
        elif answer_input == 'B':
            marker = ('W','B')
        else:
            pass

#Draw the game board
def draw_board_pygame(board):
    '''
    #Draw the game board
    '''
    global buttons
    buttons = []
    color = (0,0,0)
    for x in range(0,64):
        if board[x] == 'White':
            color = (255,255,255)
        elif board[x] == 'Brown':
           color = (139,69,19)
        elif board[x] == 'Black':
            color = (0,0,0)
        elif board[x] == 'Red':
            color = (255,0,0)
        elif board[x] == 'Green':
            color = (0,255,0)
        elif board[x] == 'Blue':
            color = (47,149,153)
        c = pygame.draw.rect(screen, color, pygame.Rect(square_location[x][1], square_location[x][0],60, 60))
        buttons.append(c)

#Creates the board background and inserts it to a board(list)
def twisted_colors_board(board):
    '''
    Creates the board background and inserts it to a board(list)
    '''
    twister = True
    space1 = 0
    space2 = 0
    for x in range(0,64):
        if space1 < 8:
            if twister:
                board.append('White')
                twister = False
            else:
                board.append('Brown')
                twister = True
            space1 += 1
        else:
            if not twister:
                board.append('White')
                twister = True
            else:
                board.append('Brown')
                twister = False
            space2 += 1
            if space2 == 8:
                space2 = 0
                space1 = 0
    if len(board) == 65:
        board.pop(0)
    else:
        pass
    return board

#Resets the game board and sets it to the original colors
def reset_board(board):
    '''
    Resets the game board and sets it to the original colors
    '''
    for x in range(len(board)):
        board[x] = back_board[x]

#Gets an image from a given path
def get_image(path):
    '''
    Resets the game board and sets it to the original colors
    '''
    global _image_library
    image = _image_library.get(path)
    if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            image = pygame.transform.scale(image, (60, 60))
            _image_library[path] = image
    return image    

def write_help(help_text):

    font = pygame.font.SysFont("century", 20)
    all_fonts = pygame.font.get_fonts()

    help_text1 = font.render("1 - peon", True, (0, 128, 0))
    help_text2 = font.render("2 - tower", True, (0, 128, 0))
    help_text3 = font.render("3 - horse", True, (0, 128, 0))
    help_text4 = font.render("4 - alfil", True, (0, 128, 0))
    help_text5 = font.render('5 - queen', True, (0, 128, 0))
    help_text6 = font.render("6 - king", True, (0, 128, 0))

    
    screen.blit(help_text1,(800, 10))
    screen.blit(help_text2,(800, 30))
    screen.blit(help_text3,(800, 50))
    screen.blit(help_text4,(800, 70))
    screen.blit(help_text5,(800, 90))
    screen.blit(help_text6,(800, 110))

def draw_pieces(location,pieces):
    loc = 100
    for z in range(0,2):
        for x in range(len(pieces_location)):
            for y in range(len(pieces_location[x][z])):
                locs = pieces_location[x][y]
                if z == 0:
                    screen.blit(piece_images[x][0],(square_location[locs][1], square_location[locs][0]))
                else:
                    screen.blit(piece_images[x][1],(square_location[locs][1], square_location[locs][0]))

def check_piece_in_location(position):
    global selected_piece_type
    selected_piece_type = [100,'White']
    location_full = False
    for z in range(0,2):
        for x in range(len(pieces_location)):
            for y in range(len(pieces_location[x][z])):
                if pieces_location[x][z][y] == position:
                    if z == 0:
                        location_full = True
                        selected_piece_type = [x,'White']
                    else:
                        location_full = True
                        selected_piece_type = [x,'Black']
                else:
                    pass
    return location_full

def check_location():
    pos = pygame.mouse.get_pos()
    # For every location of the buttons
    for x in range(0,64):
        cell = buttons[x]
        # If mouse clicking point matches with a cell position
        if cell.collidepoint(pos):
            #Check if there is a piece in that position
            #pieceinloc = check_piece_in_location(x)
            return int(x)
                #highlight and select the choose
        else:
            #emptyinloc = check_piece_in_location(xindex)
            pass


def movements():
    global movement
    type1 = [0]
    type2 = [0]
    type3 = [0]
    type4 = [0]
    type5 = [0]
    type6 = [0]

    #Peon movements
    type1.append(8)
    type1.append(-8)
    type1.pop(0)
    #Tower movements
    for x in range(0,6):
        type2.append(8*(x+1))
        type2.append(-8*(x+1))
    for x in range(0,6):
        type2.append(1*(x+1))
        type2.append(-1*(x+1))
    type2.pop(0)
    #Horse movements
    #Horse movement to the north
    type3.append(-17)
    type3.append(-15)
    #Horse movement to the South
    type3.append(17)
    type3.append(15)
    #Horse movement to the East
    type3.append(-6)
    type3.append(10)
    #Horse movement to the West
    type3.append(6)
    type3.append(-10)
    type3.pop(0)
    #Alfil movements
    type4.append(8)
    type4.append(-8)
    type4.pop(0)
    #Queen movements
    type5.append(8)
    type5.append(-8)
    type5.pop(0)
    #King movements
    type6.append(8)
    type6.append(-8)
    type6.pop(0)


    movement.append(type1)
    movement.append(type2)
    movement.append(type3)
    movement.append(type4)
    movement.append(type5)
    movement.append(type6)

def check_pice_type():
    pass

def create_square_location():
    for x in range(0,64):
        square_location.append([10 + x//8*65, 10 + (x-(x//8)*8)*65])
    square_location.pop(0)

def select_movement(location, typeofpiece):
    global blue_cells
    blue_cells = [0]
    loc = 0
    movementloc = 100
    for x in range(len(movement[typeofpiece[0]])):
        loc =  movement[typeofpiece[0]][x]
        if typeofpiece[0] == 0:
            if typeofpiece[1] == player[0]: 
                if x < ((len(typeofpiece))/2):
                    movementloc = location + loc
                else:
                    pass
            else:
                if x > ((len(typeofpiece)+1)/2):
                    movementloc = location + loc
                else:
                    pass
        else:
            loc =  movement[typeofpiece[0]][x]
            movementloc = location + loc
        if movementloc < 0:
            pass
        else:
            game_board[movementloc] = 'Blue'
            blue_cells.append(movementloc)
    blue_cells.pop(0)

def check_if_wall():
    pass


def check_movement_cell():
    '''
    OUTPUT: Will return the value of the cell you are willing to move the piece depending on if there is a empty cell, a friend piece or an enemy piece
    '''
def check_click_in_blue_cell():
    pos = pygame.mouse.get_pos()
    # For every location of the buttons
    for x in range(len(blue_cells)):
        cells = buttons[blue_cells[x]]
        print(blue_cells)
        # If mouse clicking point matches with a cell position
        if cells.collidepoint(pos):
            #Check if there is a piece in that position
            #pieceinloc = check_piece_in_location(x)
            return int(x)
                #highlight and select the choose
        else:
            #emptyinloc = check_piece_in_location(xindex)
            return 100
def check_piece(piece):
    for x in range(len(pieces_location)):
        for y in range(len(pieces_location[x])):
            if pieces_location[x][y] == piece:
                return [x,y]

###################################


square_location = ['']
back_board=['']
game_board=['']
_image_library = {}
movement = []
moving_piece_type = [100,'White']

towerblackim = get_image('C:/Users/elain/Desktop/Python 3 Notes/Chess_Game/Pygame/Images/tower_black.png')
horseblackim = get_image('C:/Users/elain/Desktop/Python 3 Notes/Chess_Game/Pygame/Images/horse_black.png')
peonblackim = get_image('C:/Users/elain/Desktop/Python 3 Notes/Chess_Game/Pygame/Images/peon_black.png')
alfilblackim = get_image('C:/Users/elain/Desktop/Python 3 Notes/Chess_Game/Pygame/Images/alfil_black.png')
queenblackim = get_image('C:/Users/elain/Desktop/Python 3 Notes/Chess_Game/Pygame/Images/queen_black.png')
kingblackim = get_image('C:/Users/elain/Desktop/Python 3 Notes/Chess_Game/Pygame/Images/king_black.png')

towerwhiteim = get_image('C:/Users/elain/Desktop/Python 3 Notes/Chess_Game/Pygame/Images/tower_black.png')
horsewhiteim = get_image('C:/Users/elain/Desktop/Python 3 Notes/Chess_Game/Pygame/Images/horse_black.png')
peonwhiteim = get_image('C:/Users/elain/Desktop/Python 3 Notes/Chess_Game/Pygame/Images/peon_black.png')
alfilwhiteim = get_image('C:/Users/elain/Desktop/Python 3 Notes/Chess_Game/Pygame/Images/alfil_black.png')
queenwhiteim = get_image('C:/Users/elain/Desktop/Python 3 Notes/Chess_Game/Pygame/Images/queen_black.png')
kingwhiteim = get_image('C:/Users/elain/Desktop/Python 3 Notes/Chess_Game/Pygame/Images/king_black.png')

create_square_location()
twisted_colors_board(back_board)
twisted_colors_board(game_board)
movements()
blue_cells = [0]

#Pieces location list in order: peon, tower, horse, alfil, queen, king
pieces_starting_location =  [[[8,9,10,11,12,13,14,15],[48,49,50,51,52,53,54,55]],[[0,7],[56,63]],[[1,6],[57,62]],[[2,5],[58,61]],[[3],[59]],[[4],[60]]]
pieces_location          =  [[[8,9,10,11,12,13,14,15],[48,49,50,51,52,53,54,55]],[[0,7],[56,63]],[[1,6],[57,62]],[[2,5],[58,61]],[[3],[59]],[[4],[60]]]

#

player = ('White','Black')





    
piece_images = [[peonblackim,peonwhiteim],[towerblackim,towerwhiteim],[horseblackim,horsewhiteim],[alfilblackim,alfilwhiteim],[queenblackim,queenwhiteim],[kingblackim,kingwhiteim]]



pygame.init()
screen = pygame.display.set_mode((1000, 540))
done = False
piece_selected = False
move_pos = 100
draw_board_pygame(back_board)
write_help('help_text')
draw_pieces(square_location,pieces_location)

while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                done = True

        # If there is a click on the game
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Get the position of the mouse
            if not piece_selected:
                selected_piece = check_location()

                if check_piece_in_location(selected_piece):
                    reset_board(game_board)
                    piece_loc = check_piece(selected_piece)
                    game_board[selected_piece] = 'Green'
                    moving_piece_type = selected_piece_type
                    
                #    piece_selected = True
                else:
                    reset_board(game_board)
                    draw_pieces(square_location,pieces_location)

                select_movement(selected_piece, moving_piece_type)
                move_pos = check_click_in_blue_cell()
                if move_pos in range(0,64):
                    pieces_location[piece_loc[0]][piece_loc[1]] = move_pos                  
                draw_board_pygame(game_board)
                draw_pieces(square_location,pieces_location)


    pygame.display.flip()            

    
