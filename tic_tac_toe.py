


game_matrix = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
game_matrix_1 = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]

flag = True
first_player = 'X'
second_player = 'O'
current_player = first_player

def get_game_matrix_str():
    return ' '.join(game_matrix[0])+ '\n' + ' '.join(game_matrix[1]) + '\n' + ' '.join(game_matrix[2])

def get_game_matrix():
    return ' '.join(game_matrix_1[0])+ '\n' + ' '.join(game_matrix_1[1]) + '\n' + ' '.join(game_matrix_1[2])

    


def print_field():
    print(get_game_matrix_str())


def print_point():
    return ('Введіть координати точки. x - стовпчик(0-2), y - рядок(0-2)') #тут має бути print

def coordinates_point():
    point = input().split()
    x, y = int(point[0]), int(point[1])
    if game_matrix[x][y] == first_player or game_matrix[x][y] == second_player:
        print('Ця точка вже занята')
        main_game()
    else:
        change_field(x, y)
        print_field()


def main_game():
    global current_player
    global game_matrix
    audit_field()
    for i in range(3):
        if game_matrix[0][i] == current_player and game_matrix[1][i] == current_player and game_matrix[2][i] == current_player:
            win(current_player) # має бути win(current_player1)
        elif game_matrix[i][0] == current_player and game_matrix[i][1] == current_player and game_matrix[i][2] == current_player:
            win(current_player)# має бути win()
    if game_matrix[0][0] == current_player and game_matrix[1][1] == current_player and game_matrix[2][2] == current_player:
        win(current_player)# має бути win()
    elif game_matrix[0][2] == current_player and game_matrix[1][1] == current_player and game_matrix[2][0] == current_player:
        win(current_player)# має бути win()

def change_player():
    global current_player
    global first_player
    global second_player
    if current_player == first_player:
        current_player = second_player
    else:
        current_player = first_player
    return current_player

def audit_field():
    global flag
    if any('+' in sl for sl in game_matrix) is False:
        flag = False
        return flag



def change_field(x,y):
    game_matrix[x][y] = current_player

  

def win(winner):
    global flag
    flag = False
    return current_player + ' виграв'




if __name__ == '__main__':
    print_field() 
    print()              
    while flag == True:
        main_game()
        print()
    print('Гра закінчилась')








    