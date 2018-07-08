import os
import random
import time
import sys

CELLS = []
for i in range(0, 20):
    for j in range(0, 20):
        CELLS.append((j, i))


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_boundry(possible_moves, monster_x, monster_y):
    if monster_x == 0:
        possible_moves.remove('LEFT')
    elif monster_x == 19:
        possible_moves.remove('RIGHT')
    elif monster_y == 0:
        possible_moves.remove('UP')
    elif monster_y == 19:
        possible_moves.remove('DOWN')
    return possible_moves


def check_door(possible_moves, monster_x, monster_y, door):
    door_x, door_y = door
    if monster_x + 1 == door_x:
        if 'RIGHT' in possible_moves:
            possible_moves.remove('RIGHT')
    if monster_x - 1 == door_x:
        if 'LEFT' in possible_moves:
            possible_moves.remove('LEFT')
    if monster_y + 1 == door_x:
        if 'DOWN' in possible_moves:
            possible_moves.remove('DOWN')
    if monster_y - 1 == door_x:
        if 'UP' in possible_moves:
            possible_moves.remove('UP')
    return possible_moves


def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60.
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)


def get_locations():
    return random.sample(CELLS, 12)


def move_player(player, move):
    x, y = player
    if move == 'A':
        x -= 1
    if move == 'D':
        x += 1
    if move == 'W':
        y -= 1
    if move == 'S':
        y += 1
    return x, y


def check_monster(possible_moves, x, y, other_monster):
    x1, y1 = other_monster
    if x + 1 == x1:
        if 'RIGHT' in possible_moves:
            possible_moves.remove('RIGHT')
    if x - 1 == x1:
        if 'LEFT' in possible_moves:
            possible_moves.remove('LEFT')
    if y + 1 == y1:
        if 'DOWN' in possible_moves:
            possible_moves.remove('DOWN')
    if y - 1 == y1:
        if 'UP' in possible_moves:
            possible_moves.remove('UP')
    return possible_moves


def get_moves(player):
    moves = ['W', 'A', 'S', 'D']
    x, y = player
    if x == 0:
        moves.remove('A')
    elif x == 19:
        moves.remove('D')
    elif y == 0:
        moves.remove('W')
    elif y == 19:
        moves.remove('S')
    return moves


def draw_map(player, monster, door, monster1, monster2, monster3, monster4, monster5, monster6, monster7, monster8,
             monster9):
    print(' -' * 20)
    tile = '|{}'
    for cell in CELLS:
        x, y = cell
        if x < 19:
            line_end = ''
            if cell == player:
                output = tile.format('O')
            elif cell == monster:
                output = tile.format('M')
            elif cell == door:
                output = tile.format('X')
            elif cell == monster1 or cell == monster2 or cell == monster3 or cell == monster4 or cell == monster5 or \
                    cell == monster6 or cell == monster7 or cell == monster8 or cell == monster9:
                output = tile.format('M')
            else:
                output = tile.format('_')
        else:
            line_end = '\n'
            if cell == player:
                output = tile.format('O|')
            elif cell == monster:
                output = tile.format('M|')
            elif cell == door:
                output = tile.format('X|')
            elif cell == monster1 or cell == monster2 or cell == monster3 or cell == monster4 or cell == monster5 or \
                    cell == monster6 or cell == monster7 or cell == monster8 or cell == monster9:
                output = tile.format('M|')
            else:
                output = tile.format('_|')
        print(output, end=line_end)


def move_monster(monster, player, start_time, greg, door, monster1, monster2, monster3, monster4, monster5, monster6,
                 monster7, monster8, monster9, lims, chicken):
    possible_moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = monster
    possible_moves = check_boundry(possible_moves, x, y)
    possible_moves = check_door(possible_moves, x, y, door)
    list_of_monsters = [monster1, monster2, monster3, monster4, monster5, monster6, monster7, monster8, monster9]
    for monsters in list_of_monsters:
        check_monster(possible_moves, x, y, monsters)

    if len(possible_moves) >= 1:
        monster_move = random.sample(possible_moves, 1)
        if monster_move == ['LEFT']:
            x -= 1
        if monster_move == ['RIGHT']:
            x += 1
        if monster_move == ['UP']:
            y -= 1
        if monster_move == ['DOWN']:
            y += 1
    monster = (x, y)
    if monster == player:
        print('\n ** Oh no! The monster got you, {}, better luck next time! ** \n'.format(name))
        input("""
                                            R.I.P
                                          {}
                                        Time Alive: {}
                        Died because of a monster that lives under my bed
                                        """.format(greg, hms_string(time.time() - start_time)))
        chicken += 1
        if input('Play again? [Y/n] '.lower()) != 'n':
            game_loop(name, lims, chicken)
        print('Thanks for playing, see you next time!')
        sys.exit()
    return monster


def game_loop(name, wins, losses):
    hp = 100
    monster, monster1, monster2, monster3, monster4, monster5, monster6, monster7, monster8, monster9, door, player = \
        get_locations()
    start_time = time.time()
    playing = True
    while playing:
        clear_screen()
        monster = move_monster(monster, player, start_time, name, door, monster1, monster2, monster3, monster4, monster5
                               , monster6, monster7, monster8, monster9, wins, losses)
        monster1 = move_monster(monster1, player, start_time, name, door, monster, monster2, monster3, monster4,
                                monster5, monster6, monster7, monster8, monster9, wins, losses)
        monster2 = move_monster(monster2, player, start_time, name, door, monster, monster1, monster3, monster4,
                                monster5, monster6, monster7, monster8, monster9, wins, losses)
        monster3 = move_monster(monster3, player, start_time, name, door, monster, monster1, monster2, monster4,
                                monster5, monster6, monster7, monster8, monster9, wins, losses)
        monster4 = move_monster(monster4, player, start_time, name, door, monster, monster1, monster2, monster3,
                                monster5, monster6, monster7, monster8, monster9, wins, losses)
        monster5 = move_monster(monster5, player, start_time, name, door, monster, monster1, monster2, monster3,
                                monster4, monster6, monster7, monster8, monster9, wins, losses)
        monster6 = move_monster(monster6, player, start_time, name, door, monster, monster1, monster2, monster3,
                                monster4, monster5, monster7, monster8, monster9, wins, losses)
        monster7 = move_monster(monster7, player, start_time, name, door, monster, monster1, monster2, monster3,
                                monster4, monster5, monster6, monster8, monster9, wins, losses)
        monster8 = move_monster(monster8, player, start_time, name, door, monster, monster1, monster2, monster3,
                                monster4, monster5, monster6, monster7, monster9, wins, losses)
        monster9 = move_monster(monster9, player, start_time, name, door, monster, monster1, monster2, monster3,
                                monster4, monster5, monster6, monster7, monster8, wins, losses)

        draw_map(player, monster, door, monster1, monster2, monster3, monster4, monster5, monster6, monster7, monster8,
                 monster9)
        valid_moves = get_moves(player)
        print('Wins: {} Losses: {}'.format(wins, losses))
        print(' ** You are currently at {}, {}. **'.format(player, name))
        print(' ** You can move {}. **'.format(', '.join(valid_moves)))
        print(" ** Enter 'Quit' to quit, {}. **".format(name))
        print(' ** X marks the spot, get out of the dungeon as fast as possible {}! **'.format(name))
        print(' ** Watch out for the monsters {}, they will kill you on first sight! **'.format(name))
        print(' ** {}, you are the \'O\' on the dungeon board! **'.format(name))
        print(' ** Watch out for spelling errors {}, giving wrong commands to your player can cause errors **'.format(
            name))
        print(' ** Your current health is {}, keep it as high as possible {}! **'.format(hp, name))

        move = input("> ")
        move = move.upper()

        if move == 'QUIT':
            print(' \n ** See you next time! ** \n ')
            break
        if move in valid_moves:
            player = move_player(player, move)
            if player == monster or player == monster1 or player == monster2 or player == monster3 or player == \
                    monster4 or player == monster5 or player == monster6 or player == monster7 or player == \
                    monster8 or player == monster9:
                print('\n ** Oh no! The monster got you, {}, better luck next time! ** \n'.format(name))
                input("""
                                    R.I.P
                                  {}
                                Time Alive: {}
                        A monster swallowed him whole!
                                """.format(name, hms_string(time.time() - start_time)))
                playing = False
                losses += 1
            if player == door:
                clear_screen()
                if playing:
                    print('\n ** Congratulations! You have escaped the dungeon {}! It was pretty easy. ** \n'
                          '  ** It only took you {}!'.format(name, hms_string(time.time() - start_time)))
                    playing = False
                    wins += 1
        else:
            input('\n **  Walls are hard! Don\'t run into them {}!  ** \n'.format(name))
            hp -= 5
            if hp <= 0:
                input("""
                    RIP
                  {}
            Time Alive: {}
How are you dumb enough to hit walls and spell WASD wrong?
                """.format(name, hms_string(time.time() - start_time)))
                playing = False
                losses += 1
    else:
        if input('Play again? [Y/n] '.lower()) != 'n':
            game_loop(name, wins, losses)
        else:
            print(' \n ** See you next time! ** \n ')


clear_screen()
print('Welcome to the Dungeon!')
input('Press enter/return to start the game!')
clear_screen()
name = input('What is your username?     ')
wins = 0
losses = 0
game_loop(name, wins, losses)
