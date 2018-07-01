import os
import random
import time
import sys


# pick random place for player spawn
# pick random place for monster spawn
# pick exit
# draw player in grid
# take input for movement
# move player, unless invalid move, past edges
# win or loss
# clear screen and recreate it

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), (16, 0), (17, 0), (18, 0), (19, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (13, 4), (14, 4), (15, 4), (16, 4), (17, 4), (18, 4), (19, 4),
         (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5), (13, 5), (14, 5), (15, 5), (16, 5), (17, 5), (18, 5), (19, 5),
         (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6), (19, 6),
         (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (17, 7), (18, 7), (19, 7),
         (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), (17, 8), (18, 8), (19, 8),
         (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9), (15, 9), (16, 9), (17, 9), (18, 9), (19, 9),
         (0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10), (16, 10), (17, 10), (18, 10), (19, 10),
         (0, 11), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11), (13, 11), (14, 11), (15, 11), (16, 11), (17, 11), (18, 11), (19, 11),
         (0, 12), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12), (13, 12), (14, 12), (15, 12), (16, 12), (17, 12), (18, 12), (19, 12),
         (0, 13), (1, 13), (2, 13), (3, 13), (4, 13), (5, 13), (6, 13), (7, 13), (8, 13), (9, 13), (10, 13), (11, 13), (12, 13), (13, 13), (14, 13), (15, 13), (16, 13), (17, 13), (18, 13), (19, 13),
         (0, 14), (1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (6, 14), (7, 14), (8, 14), (9, 14), (10, 14), (11, 14), (12, 14), (13, 14), (14, 14), (15, 14), (16, 14), (17, 14), (18, 14), (19, 14),
         (0, 15), (1, 15), (2, 15), (3, 15), (4, 15), (5, 15), (6, 15), (7, 15), (8, 15), (9, 15), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (16, 15), (17, 15), (18, 15), (19, 15),
         (0, 16), (1, 16), (2, 16), (3, 16), (4, 16), (5, 16), (6, 16), (7, 16), (8, 16), (9, 16), (10, 16), (11, 16), (12, 16), (13, 16), (14, 16), (15, 16), (16, 16), (17, 16), (18, 16), (19, 16),
         (0, 17), (1, 17), (2, 17), (3, 17), (4, 17), (5, 17), (6, 17), (7, 17), (8, 17), (9, 17), (10, 17), (11, 17), (12, 17), (13, 17), (14, 17), (15, 17), (16, 17), (17, 17), (18, 17), (19, 17),
         (0, 18), (1, 18), (2, 18), (3, 18), (4, 18), (5, 18), (6, 18), (7, 18), (8, 18), (9, 18), (10, 18), (11, 18), (12, 18), (13, 18), (14, 18), (15, 18), (16, 18), (17, 18), (18, 18), (19, 18),
         (0, 19), (1, 19), (2, 19), (3, 19), (4, 19), (5, 19), (6, 19), (7, 19), (8, 19), (9, 19), (10, 19), (11, 19), (12, 19), (13, 19), (14, 19), (15, 19), (16, 19), (17, 19), (18, 19), (19, 19)
         ]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#def check_monster(possible_moves, x, y, other_monster, another_monster):

    #return possible_moves


def check_boundry(possible_moves, monster_x, monster_y):
    if monster_x == 0:
        possible_moves.remove('LEFT')
    if monster_x == 19:
        possible_moves.remove('RIGHT')
    if monster_y == 0:
        possible_moves.remove('UP')
    if monster_y == 19:
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
    return random.sample(CELLS, 8)


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
    if x == 19:
        moves.remove('D')
    if y == 0:
        moves.remove('W')
    if y == 19:
        moves.remove('S')
    return moves


def draw_map(player, monster, door, monster1, monster2, monster3, monster4, monster5):
    print(' -'*20)
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
            elif cell == monster1:
                output = tile.format('M')
            elif cell == monster2:
                output = tile.format('M')
            elif cell == monster3:
                output = tile.format('M')
            elif cell == monster4:
                output = tile.format('M')
            elif cell == monster5:
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
            elif cell == monster1:
                output = tile.format('M|')
            elif cell == monster2:
                output = tile.format('M|')
            elif cell == monster3:
                output = tile.format('M|')
            elif cell == monster4:
                output = tile.format('M|')
            elif cell == monster5:
                output = tile.format('M|')
            else:
                output = tile.format('_|')
        print(output, end=line_end)


def move_monster(monster, player, start_time, name, door, monster1, monster2, monster3, monster4, monster5, wins, losses):
    possible_moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = monster
    check_boundry(possible_moves, x, y)
    check_door(possible_moves, x, y, door)
    check_monster(possible_moves, x, y, monster1)
    check_monster(possible_moves, x, y, monster2)
    check_monster(possible_moves, x, y, monster3)
    check_monster(possible_moves, x, y, monster4)
    check_monster(possible_moves, x, y, monster5)

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
                                        """.format(name, hms_string(time.time() - start_time)))
        losses +=1
        if input('Play again? [Y/n] '.lower()) != 'n':
            game_loop(name, wins, losses)
        print('Thanks for playing, see you next time!')
        sys.exit()
    return monster


def game_loop(name, wins, losses):
    hp = 100
    monster, monster1, monster2, monster3, monster4, monster5, door, player = get_locations()
    start_time = time.time()
    playing = True
    while playing:
        clear_screen()
        monster = move_monster(monster, player, start_time, name, door, monster1, monster2, monster3, monster4, monster5, wins, losses)
        monster1 = move_monster(monster1, player, start_time, name, door, monster, monster2, monster3, monster4, monster5, wins, losses)
        monster2 = move_monster(monster2, player, start_time, name, door, monster, monster1, monster3, monster4, monster5, wins, losses)
        monster3 = move_monster(monster3, player, start_time, name, door, monster, monster1, monster2, monster4, monster5, wins, losses)
        monster4 = move_monster(monster4, player, start_time, name, door, monster, monster1, monster2, monster3, monster5, wins, losses)
        monster5 = move_monster(monster5, player, start_time, name, door, monster, monster1, monster2, monster3, monster4, wins, losses)

        draw_map(player, monster, door, monster1, monster2, monster3, monster4, monster5)
        valid_moves = get_moves(player)
        print('Wins: {} Losses: {}'.format(wins, losses))
        print(' ** You are currently at {}, {}. **'.format(player, name))
        print(' ** You can move {}. **'.format(', '.join(valid_moves)))
        print(" ** Enter 'Quit' to quit, {}. **".format(name))
        print(' ** X marks the spot, get out of the dungeon as fast as possible {}! **'.format(name))
        print(' ** Watch out for the monsters {}, they will kill you on first sight! **'.format(name))
        print(' ** {}, you are the \'O\' on the dungeon board! **'.format(name))
        print(' ** Watch out for spelling errors {}, giving wrong commands to your player can cause errors **'.format(name))
        print(' ** Your current health is {}, keep it as high as possible {}! **'.format(hp, name))

        move = input("> ")
        move = move.upper()

        if move == 'QUIT':
            print(' \n ** See you next time! ** \n ')
            break
        if move in valid_moves:
            player = move_player(player, move)

            if player == monster:
                print('\n ** Oh no! The monster got you, {}, better luck next time! ** \n'.format(name))
                input("""
                                    R.I.P
                                  {}
                                Time Alive: {}
                Died because of a monster that lives under my bed
                                """.format(name, hms_string(time.time() - start_time)))
                playing = False
                losses += 1
            if player == monster1:
                print('\n ** Oh no! The monster got you, {}, better luck next time! ** \n'.format(name))
                input("""
                                                    R.I.P
                                                  {}
                                            Time Alive: {}
                                Died because of a monster that lives under my bed
                                                """.format(name, hms_string(time.time() - start_time)))
                playing = False
                losses += 1
            if player == monster2:
                print('\n ** Oh no! The monster got you, {}, better luck next time! ** \n'.format(name))
                input("""
                                                    R.I.P
                                                  {}
                                            Time Alive: {}
                                Died because of a monster that lives under my bed
                                                """.format(name, hms_string(time.time() - start_time)))
                playing = False
                losses += 1
            if player == monster3:
                print('\n ** Oh no! The monster got you, {}, better luck next time! ** \n'.format(name))
                input("""
                                    R.I.P
                                  {}
                                Time Alive: {}
                Died because of a monster that lives under my bed
                                """.format(name, hms_string(time.time() - start_time)))
                playing = False
                losses += 1
            if player == monster4:
                print('\n ** Oh no! The monster got you, {}, better luck next time! ** \n'.format(name))
                input("""
                                    R.I.P
                                  {}
                                Time Alive: {}
                Died because of a monster that lives under my bed
                                """.format(name, hms_string(time.time() - start_time)))
                playing = False
                losses += 1
            if player == monster5:
                print('\n ** Oh no! The monster got you, {}, better luck next time! ** \n'.format(name))
                input("""
                                    R.I.P
                                  {}
                                Time Alive: {}
                Died because of a monster that lives under my bed
                                """.format(name, hms_string(time.time() - start_time)))
                playing = False
                losses += 1
            if player == door:
                clear_screen()
                if playing != False:
                    print('\n ** Congratulations! You have escaped the dungeon {}! ** \n  ** It only took you {}!'.format(name, hms_string(time.time() - start_time)))
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
      Died because of too much concussions
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
